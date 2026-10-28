"""Map the extracted tokens to Figma collections, modes, aliases and scopes, and list the frontend issues.

Usage: python3 plan_tokens.py <tokens.json> <plan.json>
"""
import json, re, sys
T = json.load(open(sys.argv[1]))
core = dict(T['core']); sem_l = dict(T['semantic_light']); sem_d = dict(T['semantic_dark'])
leg_l = dict(T['legacy_light']); leg_d = dict(T['legacy_dark'])
issues = []
def hexrgba(h):
    h=h.lstrip('#')
    if len(h)==3: h=''.join(c*2 for c in h)
    r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    a=int(h[6:8],16)/255 if len(h)==8 else 1
    return {"r":round(r,6),"g":round(g,6),"b":round(b,6),"a":a}
def parse_color(v, rgbmap):
    v=v.strip()
    if v.startswith('#'): return hexrgba(v)
    if v=='transparent': return {"r":0,"g":0,"b":0,"a":0}
    m=re.match(r'rgba?\(\s*var\((--[\w-]+)\)\s*,\s*([\d.]+)\s*\)$',v)
    if m:
        trip=rgbmap.get(m.group(1))
        if not trip: return None
        r,g,b=[int(x)/255 for x in trip.split(',')]
        return {"r":round(r,6),"g":round(g,6),"b":round(b,6),"a":float(m.group(2))}
    m=re.match(r'rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+))?\s*\)$',v)
    if m:
        r,g,b=[float(m.group(i))/255 for i in (1,2,3)]
        a=float(m.group(4)) if m.group(4) else 1
        return {"r":round(r,6),"g":round(g,6),"b":round(b,6),"a":a}
    return None
def varref(v):
    # returns referenced css var name for var(--x) or var(--x, var(--y)) (fallback)
    v=v.strip()
    m=re.match(r'var\((--[\w-]+)\)$',v)
    if m: return m.group(1), None
    m=re.match(r'var\((--[\w-]+)\s*,\s*var\((--[\w-]+)\)\)$',v)
    if m: return m.group(1), m.group(2)
    return None, None
def ha_name(css):  # --ha-color-primary-05 -> color/primary/05
    n=css[len('--ha-'):]
    parts=n.split('-')
    return parts  # caller groups
# ---------- Core ----------
core_vars=[]
for css,v in T['core']:
    n=css[len('--ha-'):]            # color-primary-05
    if n in ('color-black','color-white'): name='color/'+n.split('-')[1]
    else:
        p=n.split('-'); name=f"{p[0]}/{p[1]}/{p[2]}"
    core_vars.append({"name":name,"css":css,"value":hexrgba(v)})
core_by_css={c["css"]:c["name"] for c in core_vars}
# ---------- Semantic ----------
def sem_scopes(n):
    if n.startswith('color/text/') or n=='color/on-surface/default': return ['TEXT_FILL']
    if n.startswith('color/border/') or n=='color/focus': return ['STROKE_COLOR']
    if n.startswith('color/on/'): return ['TEXT_FILL','SHAPE_FILL','STROKE_COLOR']
    if n.startswith('color/shadow/'): return ['EFFECT_COLOR']
    return ['FRAME_FILL','SHAPE_FILL']
def sem_name(css):
    n=css[len('--ha-color-'):]
    for g in ('text','border','fill','on-surface','on','surface','form','shadow'):
        if n==g: return 'color/'+g
        if n.startswith(g+'-'): return 'color/'+g+'/'+n[len(g)+1:]
    return 'color/'+n
sem_vars=[]; sem_names=set()
allsem=[css for css,_ in T['semantic_light']]
for css,_ in T['semantic_dark']:
    if css not in allsem: allsem.append(css)
for css in allsem:
    name=sem_name(css); entry={"name":name,"css":css,"scopes":sem_scopes(name),"light":None,"dark":None,"notes":[]}
    for mode,src in (('light',sem_l),('dark',sem_d)):
        if css not in src:
            if mode=='dark': entry['dark']=('same','') ; continue
            entry['notes'].append('no light value in semantic.globals.ts (dark only)')
            issues.append(f"{css}: defined only in the dark block of semantic.globals.ts; no light value. Light mode left at Figma default.")
            continue
        v=src[css]; ref,fb=varref(v)
        if ref:
            if ref in core_by_css: entry[mode]=('alias',core_by_css[ref])
            elif ref=='--white-color':
                entry[mode]=('alias','color/white'); entry['notes'].append(f'{mode}: frontend references legacy --white-color (#ffffff); aliased to core color/white')
            else:
                entry['notes'].append(f'{mode}: references {ref}, which does not exist in core.globals.ts; value left unset')
                issues.append(f"{css} ({mode}): references {ref}, which does not exist in core.globals.ts. Mode left at Figma default.")
                entry[mode]=('unset','')
        else:
            c=parse_color(v,{})
            entry[mode]=('raw',c) if c else ('unset','')
            if not c: issues.append(f"{css} ({mode}): value {v} not representable")
    if entry['dark']==('same',''): entry['dark']=entry['light']
    sem_vars.append(entry); sem_names.add(name)
sem_by_css={e['css']:e['name'] for e in sem_vars}
# ---------- Legacy ----------
GROUPS=['state','energy','mdc','input','codemirror','sidebar','label-badge','table','data-table','ha-button','ha-assist-chip','slider','app-header','history','scrollbar','markdown','chip','rgb','color']
def leg_name(css):
    n=css[2:]
    if re.match(r'color-\d+$',n): return 'chart/'+n.replace('-','/')
    for g in GROUPS:
        if n.startswith(g+'-'): return g+'/'+n[len(g)+1:]
    return 'base/'+n
rgbmap={css:v for css,v in T['legacy_light'] if css.startswith('--rgb-')}
alll=[css for css,_ in T['legacy_light']]
for css,_ in T['legacy_dark']:
    if css not in alll: alll.append(css)
leg_vars=[]; skipped=[]
leg_css=set(alll)
def leg_scopes(name,css):
    if 'text' in css or 'ink' in css: return ['TEXT_FILL','SHAPE_FILL']
    if 'border' in css or 'line-color' in css or 'outline' in css or 'divider' in css: return ['STROKE_COLOR']
    if 'shadow' in css: return ['EFFECT_COLOR']
    if 'background' in css or 'fill' in css: return ['FRAME_FILL','SHAPE_FILL']
    return ['FRAME_FILL','SHAPE_FILL','TEXT_FILL','STROKE_COLOR']
for css in alll:
    if css.startswith('--rgb-'): skipped.append((css,'rgb triplet, not a colour')); continue
    name=leg_name(css); entry={"name":name,"css":css,"scopes":leg_scopes(name,css),"light":None,"dark":None,"notes":[]}
    ok=True
    for mode,src in (('light',leg_l),('dark',leg_d)):
        if css not in src:
            if mode=='dark': entry['dark']=entry['light']; continue
            entry['notes'].append('no light value in color.globals.ts (dark only)')
            issues.append(f"{css}: defined only in the dark block of color.globals.ts. Light mode left at Figma default.")
            continue
        v=src[css]; ref,fb=varref(v)
        if ref:
            target = fb if (fb and ref not in leg_css and ref not in sem_by_css and ref not in core_by_css) else ref
            if fb and target==fb: entry['notes'].append(f'{mode}: var({ref}) with fallback; {ref} is not defined in the theme files, aliased to the fallback {fb}')
            if target in core_by_css: entry[mode]=('alias-core',core_by_css[target])
            elif target in sem_by_css: entry[mode]=('alias-semantic',sem_by_css[target])
            elif target in leg_css and not target.startswith('--rgb-'): entry[mode]=('alias-legacy',leg_name(target))
            else:
                ok=False; skipped.append((css,f'references {target}, not a colour variable')); break
        else:
            c=parse_color(v,rgbmap)
            if c: entry[mode]=('raw',c)
            else: ok=False; skipped.append((css,f'value not a colour: {v}')); break
    if ok:
        if entry['dark'] is None: entry['dark']=entry['light']
        leg_vars.append(entry)
# ---------- Spacing / Radius / Typography / Layout ----------
cs=dict(T['core_sizes'])
spacing=[{"name":f"space/{i}","css":f"--ha-space-{i}","value":int(cs[f'--ha-space-{i}'][:-2])} for i in range(1,21)]
radius=[]
for k in ['sm','md','lg','xl','2xl','3xl','4xl','5xl','6xl','pill','circle','square']:
    v=cs[f'--ha-border-radius-{k}']
    if v.endswith('px'): val=int(v[:-2]); note=None
    elif v=='50%': val=9999; note='CSS value is 50%. Figma has no percentage radius; 9999 renders a circle on square nodes.'
    else: val=int(v); note=None
    radius.append({"name":f"border-radius/{k}","css":f"--ha-border-radius-{k}","value":val,"scopes":["CORNER_RADIUS"],"note":note})
radius.append({"name":"picture-border-radius/default","css":"--ha-picture-border-radius","alias":"border-radius/lg","scopes":["CORNER_RADIUS"]})
radius.append({"name":"picture-border-radius/sm","css":"--ha-picture-border-radius-sm","alias":"border-radius/sm","scopes":["CORNER_RADIUS"]})
for k in ['sm','md','lg']:
    radius.append({"name":f"border-width/{k}","css":f"--ha-border-width-{k}","value":int(cs[f'--ha-border-width-{k}'][:-2]),"scopes":["STROKE_FLOAT"]})
durations=[(k,v) for k,v in T['core_sizes'] if 'animation' in k]
ty=dict(T['typography'])
typo=[]
typo.append({"name":"font-family/body","css":"--ha-font-family-body","type":"STRING","value":"Roboto","scopes":["FONT_FAMILY"],"note":"CSS: Roboto, Noto, sans-serif"})
typo.append({"name":"font-family/code","css":"--ha-font-family-code","type":"STRING","value":"monospace","scopes":[],"note":"CSS: monospace (generic family, no Figma font)"})
typo.append({"name":"font-family/longform","css":"--ha-font-family-longform","type":"STRING","value":"ui-sans-serif","scopes":[],"note":"CSS: ui-sans-serif, system-ui, sans-serif (system font, no Figma font)"})
typo.append({"name":"font-family/heading","css":"--ha-font-family-heading","type":"STRING","alias":"font-family/body","scopes":["FONT_FAMILY"]})
typo.append({"name":"font-size/scale","css":"--ha-font-size-scale","type":"FLOAT","value":1,"scopes":[],"note":"Multiplier applied to every font size in CSS"})
for k in ['xs','s','m','l','xl','2xl','3xl','4xl','5xl']:
    px=int(re.search(r'calc\((\d+)px',ty[f'--ha-font-size-{k}']).group(1))
    typo.append({"name":f"font-size/{k}","css":f"--ha-font-size-{k}","type":"FLOAT","value":px,"scopes":["FONT_SIZE"]})
for k in ['light','normal','medium','bold']:
    typo.append({"name":f"font-weight/{k}","css":f"--ha-font-weight-{k}","type":"FLOAT","value":int(ty[f'--ha-font-weight-{k}']),"scopes":["FONT_WEIGHT"]})
for k,t in [('body','normal'),('heading','bold'),('action','medium')]:
    typo.append({"name":f"font-weight/{k}","css":f"--ha-font-weight-{k}","type":"FLOAT","alias":f"font-weight/{t}","scopes":["FONT_WEIGHT"]})
for k in ['condensed','normal','expanded']:
    v=float(ty[f'--ha-line-height-{k}'])
    typo.append({"name":f"line-height/{k}","css":f"--ha-line-height-{k}","type":"FLOAT","value":v*100,"scopes":["LINE_HEIGHT"],"note":f"CSS value is unitless {v}; stored as {v*100:g}% for Figma"})
mn=dict(T['main'])
layout=[{"name":"header-height","css":"--header-height","value":56,"scopes":["WIDTH_HEIGHT"]}]
for k in ['dark-divider-opacity','dark-disabled-opacity','dark-secondary-opacity','dark-primary-opacity','light-divider-opacity','light-disabled-opacity','light-secondary-opacity','light-primary-opacity']:
    g,rest=k.split('-',1)
    layout.append({"name":f"opacity/{g}/{rest.replace('-opacity','')}","css":f"--{k}","value":float(mn['--'+k]),"scopes":["OPACITY"]})
for n,css,v,sc in [("view-sections/row-height","--ha-view-sections-row-height",56,["WIDTH_HEIGHT"]),("view-sections/row-gap","--ha-view-sections-row-gap",24,["GAP"]),("view-sections/column-gap","--ha-view-sections-column-gap",32,["GAP"]),("view-sections/narrow-column-gap","--ha-view-sections-narrow-column-gap",8,["GAP"]),("view-sections/column-min-width","--ha-view-sections-column-min-width",320,["WIDTH_HEIGHT"]),("view-sections/column-max-width","--ha-view-sections-column-max-width",500,["WIDTH_HEIGHT"]),("view-sections/extra-top-margin","--ha-view-sections-extra-top-margin",80,["GAP"])]:
    layout.append({"name":n,"css":css,"value":v,"scopes":sc,"note":"Default from src/panels/lovelace/views/hui-sections-view.ts"})
plan={"core":core_vars,"semantic":sem_vars,"legacy":leg_vars,"spacing":spacing,"radius":radius,"typography":typo,"layout":layout,"durations":durations,"issues":issues,"legacySkipped":skipped}
json.dump(plan,open(sys.argv[2],'w'),indent=1)
for k in plan: print(k,len(plan[k]))
print('\nISSUES'); [print('-',i) for i in issues]
print('\nSKIPPED'); [print('-',s) for s in skipped]
print('\nSEM NOTES'); [print('-',e['css'],e['notes']) for e in sem_vars if e['notes']]
print('\nLEG NOTES'); [print('-',e['css'],e['notes']) for e in leg_vars if e['notes']]
