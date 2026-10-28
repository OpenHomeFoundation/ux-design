"""Read the CSS custom properties of the frontend theme files into one JSON file.

Usage: python3 extract_tokens.py <frontend clone> <output.json>
"""
import re, json, sys, os
root = os.path.join(sys.argv[1], "src/resources/theme/")
def block(path, exportname):
    src = open(root + path).read()
    m = re.search(r"export const " + exportname + r"\s*=\s*css`(.*?)`;", src, re.S)
    body = m.group(1)
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)
    out = []
    for mm in re.finditer(r"(--[a-zA-Z0-9_-]+)\s*:\s*([^;]+);", body):
        out.append((mm.group(1), mm.group(2).strip()))
    return out
data = {
  "core": block("color/core.globals.ts", "coreColorStyles"),
  "semantic_light": block("color/semantic.globals.ts", "semanticColorStyles"),
  "semantic_dark": block("color/semantic.globals.ts", "darkSemanticColorStyles"),
  "legacy_light": block("color/color.globals.ts", "colorStyles"),
  "legacy_dark": block("color/color.globals.ts", "darkColorStyles"),
  "wa_color": block("color/wa.globals.ts", "waColorStyles"),
  "wa_main": block("wa.globals.ts", "waMainStyles"),
  "core_sizes": block("core.globals.ts", "coreStyles"),
  "typography": block("typography.globals.ts", "typographyStyles"),
  "main": block("main.globals.ts", "mainStyles"),
}
# core_sizes: the reduced-motion block duplicates names; keep first occurrence
seen=set(); cs=[]
for k,v in data["core_sizes"]:
    if k in seen: continue
    seen.add(k); cs.append((k,v))
data["core_sizes"]=cs
for k,v in data.items(): print(k, len(v))
json.dump(data, open(sys.argv[2], "w"), indent=1)
