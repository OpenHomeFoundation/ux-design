// Helpers for use_figma scripts that build the Home Assistant Design Kit.
// Copy the parts a script needs; use_figma calls do not share state.
// IDs come from design-kit/state.json (entities.variables, entities.textStyles,
// entities.collections, entities.modes, icons.ids).

// ---- Setup ----------------------------------------------------------------

const VAR_IDS = {
  text: 'VariableID:7:2',        // Legacy color/base/primary-text-color
  secondary: 'VariableID:7:3',   // Legacy color/base/secondary-text-color
  primary: 'VariableID:7:7',     // Legacy color/base/primary-color
  divider: 'VariableID:7:12',    // Legacy color/base/divider-color
  cardBg: 'VariableID:7:21',     // Legacy color/base/card-background-color
  primaryBg: 'VariableID:7:22',  // Legacy color/base/primary-background-color
  white: 'VariableID:2:10',      // Core color/color/white
  link: 'VariableID:6:6',        // Semantic color/color/text/link
};
const TEXT_STYLE = {
  s: 'S:411114e360e42378ac86c8184aaaba62590195a2,',    // Normal/Normal/s
  m: 'S:eeff40fe1a3e8a63b677213f87533bf7e0a9c969,',    // Normal/Normal/m
  l: 'S:525bd25bfb08de18793313068178f4d17d1011ec,',    // Normal/Normal/l
  mMed: 'S:08b3a98731151155aec9fbc9530b3e4acedecf4c,', // Normal/Medium/m
};
const rgb = (r, g, b) => ({ type: 'SOLID', color: { r: r / 255, g: g / 255, b: b / 255 } });
const GRAY_CANVAS = rgb(125, 125, 125); // #7D7D7D
const GRAY_SET = rgb(142, 142, 142);    // #8E8E8E
const GRAY_EXAMPLES = rgb(164, 164, 164); // #A4A4A4

async function loadVars() {
  const vars = {};
  for (const [k, id] of Object.entries(VAR_IDS)) vars[k] = await figma.variables.getVariableByIdAsync(id);
  return vars;
}
async function loadFonts() {
  for (const style of ['Regular', 'Medium', 'Bold']) await figma.loadFontAsync({ family: 'Roboto', style });
}
// setBoundVariableForPaint returns a new paint and needs the variable object.
const paintV = (v) => figma.variables.setBoundVariableForPaint({ type: 'SOLID', color: { r: 0, g: 0, b: 0 } }, 'color', v);

// ---- Text and icons -------------------------------------------------------

async function text(parent, chars, styleKey, colorVar, name) {
  const t = figma.createText();
  parent.appendChild(t);
  await t.setTextStyleIdAsync(TEXT_STYLE[styleKey] || styleKey);
  t.characters = chars;
  t.fills = [paintV(colorVar)];
  t.autoRename = false;
  t.name = name || chars.slice(0, 40);
  return t;
}

// Loads the Icons page once and returns { name: component } for the MDI names asked.
async function loadIcons(names) {
  const iconsPage = figma.root.children.find((p) => p.name === 'Icons');
  await iconsPage.loadAsync();
  const wanted = new Set(names.map((n) => 'Icons / mdi / ' + n));
  const out = {};
  for (const c of iconsPage.findAllWithCriteria({ types: ['COMPONENT'] })) {
    if (wanted.has(c.name)) out[c.name.slice(13)] = c;
  }
  const missing = names.filter((n) => !out[n]);
  if (missing.length) throw new Error('Missing icons: ' + missing.join(', '));
  return out;
}

async function icon(parent, comp, size, colorVar) {
  const i = comp.createInstance();
  parent.appendChild(i);
  i.resize(size, size);
  i.name = 'icon';
  i.constraints = { horizontal: 'MIN', vertical: 'MIN' };
  const vec = i.findOne((n) => n.name === 'icon' && n.type === 'VECTOR');
  if (vec) vec.fills = [paintV(colorVar)];
  return i;
}

// Sets an instance property by its name without the #id suffix.
function setProp(inst, name, value) {
  const key = Object.keys(inst.componentProperties).find((k) => k === name || k.startsWith(name + '#'));
  if (!key) return null;
  inst.setProperties({ [key]: value });
  return key;
}

// ---- Section building blocks ----------------------------------------------

// Guidelines card: 800px, Semantic color mode Dark so the link shows the dark-mode blue.
async function guidelines(parent, vars, title, body, linkLabel, linkUrl) {
  const semantic = await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:2:3');
  const g = figma.createAutoLayout('VERTICAL', { name: 'Guidelines', itemSpacing: 16 });
  parent.appendChild(g);
  g.fills = [];
  g.resize(800, 10);
  g.primaryAxisSizingMode = 'AUTO';
  g.counterAxisSizingMode = 'FIXED';
  g.setExplicitVariableModeForCollection(semantic, '2:2');
  const add = (chars, size, style, fill, lineHeight, name) => {
    const t = figma.createText();
    g.appendChild(t);
    t.fontName = { family: 'Roboto', style };
    t.fontSize = size;
    t.characters = chars;
    t.fills = [fill];
    t.lineHeight = { unit: 'PERCENT', value: lineHeight };
    t.textAutoResize = 'HEIGHT';
    t.resize(800, t.height);
    t.name = name;
    return t;
  };
  add(title, 32, 'Bold', rgb(255, 255, 255), 120, 'label');
  add(body, 18, 'Regular', rgb(255, 255, 255), 150, 'label');
  const l = add(linkLabel, 18, 'Medium', paintV(vars.link), 150, 'link');
  l.setRangeHyperlink(0, linkLabel.length, { type: 'URL', value: linkUrl });
  return g;
}

// Examples frame with a Light and a Dark panel; build(panel, mode) fills each panel.
async function examples(parent, vars, build) {
  const semantic = await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:2:3');
  const legacy = await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:2:4');
  const ex = figma.createAutoLayout('HORIZONTAL', { name: 'Examples', itemSpacing: 40, paddingTop: 40, paddingBottom: 40, paddingLeft: 40, paddingRight: 40 });
  parent.appendChild(ex);
  ex.fills = [GRAY_EXAMPLES];
  ex.cornerRadius = 0;
  ex.clipsContent = false;
  for (const mode of ['Light', 'Dark']) {
    const p = figma.createAutoLayout('VERTICAL', { name: 'Examples / ' + mode, itemSpacing: 16, paddingTop: 24, paddingBottom: 24, paddingLeft: 24, paddingRight: 24 });
    ex.appendChild(p);
    p.fills = [paintV(vars.cardBg)];
    p.cornerRadius = 12;
    p.clipsContent = false;
    if (mode === 'Dark') {
      p.setExplicitVariableModeForCollection(semantic, '2:2');
      p.setExplicitVariableModeForCollection(legacy, '2:4');
    }
    const label = figma.createText();
    p.appendChild(label);
    label.fontName = { family: 'Roboto', style: 'Medium' };
    label.fontSize = 12;
    label.characters = mode;
    label.fills = [paintV(vars.secondary)];
    label.name = 'label';
    await build(p, mode);
  }
  return ex;
}

function row(panel, name, gap = 16) {
  const r = figma.createAutoLayout('HORIZONTAL', { name, itemSpacing: gap });
  panel.appendChild(r);
  r.fills = [];
  r.counterAxisAlignItems = 'CENTER';
  return r;
}

// Lays out the variants of a set in a grid on the set gray.
function layoutSet(set, cols, gx = 40, gy = 40) {
  set.layoutMode = 'NONE';
  const kids = set.children;
  let cw = 0;
  let ch = 0;
  kids.forEach((c) => { cw = Math.max(cw, c.width); ch = Math.max(ch, c.height); });
  const rows = Math.ceil(kids.length / cols);
  set.resizeWithoutConstraints(80 + cols * cw + (cols - 1) * gx, 80 + rows * ch + (rows - 1) * gy);
  set.fills = [GRAY_SET];
  set.cornerRadius = 0;
  kids.forEach((c, i) => { c.x = 40 + (i % cols) * (cw + gx); c.y = 40 + Math.floor(i / cols) * (ch + gy); });
}

// Puts a single component on the set gray inside a Components frame.
function componentsFrame(page, comp) {
  const f = figma.createFrame();
  page.appendChild(f);
  f.name = 'Components';
  f.fills = [GRAY_SET];
  f.cornerRadius = 0;
  f.appendChild(comp);
  comp.x = 40;
  comp.y = 40;
  f.resize(comp.width + 80, comp.height + 80);
  return f;
}

// New section to the right of the existing ones: Guidelines, Examples 120px below, blocks 80px below.
async function buildSection(page, vars, name, guide, buildExamples, blocks) {
  let x = 0;
  for (const c of page.children) if (c.type === 'SECTION') x = Math.max(x, c.x + c.width);
  const sec = figma.createSection();
  page.appendChild(sec);
  sec.name = name;
  sec.x = x + 240;
  sec.y = 284;
  const g = await guidelines(sec, vars, ...guide);
  g.x = 40;
  g.y = 40;
  const ex = await examples(sec, vars, buildExamples);
  ex.x = 40;
  ex.y = g.y + g.height + 120;
  let bx = 40;
  for (const b of blocks) {
    sec.appendChild(b);
    b.x = bx;
    b.y = ex.y + ex.height + 80;
    bx += b.width + 40;
  }
  fitSection(sec);
  return sec;
}

function fitSection(s) {
  let w = 0;
  let h = 0;
  for (const c of s.children) { w = Math.max(w, c.x + c.width); h = Math.max(h, c.y + c.height); }
  s.resizeWithoutConstraints(w + 40, h + 40);
}

// ---- Pre-publish check ----------------------------------------------------

// Run once per page (skip Icons). Returns sets with unused properties or names
// that clash with a variant axis; Figma refuses to publish either.
function checkProperties(page) {
  const out = [];
  const owners = page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })
    .filter((n) => n.type === 'COMPONENT_SET' || n.parent.type !== 'COMPONENT_SET');
  for (const o of owners) {
    const defs = o.componentPropertyDefinitions;
    const keys = Object.keys(defs);
    if (!keys.length) continue;
    const used = new Set();
    for (const n of o.findAll(() => true)) {
      const refs = n.componentPropertyReferences;
      if (refs) for (const v of Object.values(refs)) used.add(v);
    }
    const unused = keys.filter((k) => defs[k].type !== 'VARIANT' && !used.has(k));
    const names = keys.map((k) => k.split('#')[0]);
    const clashes = [...new Set(names.filter((n, i) => names.indexOf(n) !== i))];
    if (unused.length || clashes.length) out.push({ page: page.name, id: o.id, name: o.name, unused, clashes });
  }
  return out;
}
