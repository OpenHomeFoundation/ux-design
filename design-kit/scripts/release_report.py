"""Write the issue body for a new frontend release.

Usage: python3 release_report.py <old frontend> <new frontend> <old tokens.json> <new tokens.json> <old ref> <new tag>

The two frontend folders are checkouts of the commit the kit was built from and
of the new release. The token files come from extract_tokens.py.
"""
import json
import os
import sys

old_dir, new_dir, old_tokens, new_tokens, old_ref, new_tag = sys.argv[1:7]
REPO = "https://github.com/home-assistant/frontend"
# Source folders whose changes can affect the kit.
WATCHED = [
    "src/resources/theme",
    "src/components",
    "src/layouts",
    "src/panels/lovelace/cards",
    "src/panels/lovelace/views",
]
MAX_FILES = 100
MAX_BODY = 60000  # GitHub refuses issue bodies over 65536 characters.

out = []


def token_diff():
    old = json.load(open(old_tokens))
    new = json.load(open(new_tokens))
    rows = []
    for group in sorted(set(old) | set(new)):
        a = dict(old.get(group, []))
        b = dict(new.get(group, []))
        for name in sorted(set(a) | set(b)):
            if name not in a:
                rows.append((group, name, "added", "", b[name]))
            elif name not in b:
                rows.append((group, name, "removed", a[name], ""))
            elif a[name] != b[name]:
                rows.append((group, name, "changed", a[name], b[name]))
    return rows


def files(root):
    found = {}
    for top in WATCHED:
        base = os.path.join(root, top)
        for dirpath, _, names in os.walk(base):
            for n in names:
                full = os.path.join(dirpath, n)
                found[os.path.relpath(full, root)] = full
    return found


def file_diff():
    a = files(old_dir)
    b = files(new_dir)
    changes = []
    for path in sorted(set(a) | set(b)):
        if path not in a:
            changes.append(("added", path))
        elif path not in b:
            changes.append(("removed", path))
        elif open(a[path], "rb").read() != open(b[path], "rb").read():
            changes.append(("changed", path))
    return changes


def mdi_version(root):
    try:
        pkg = json.load(open(os.path.join(root, "package.json")))
    except (OSError, ValueError):
        return None
    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
    return deps.get("@mdi/svg")


def cell(value):
    return "`%s`" % value.replace("|", "\\|") if value else ""


out.append(
    "Frontend [%s](%s/releases/tag/%s) is out. The kit was built from `%s`. [Compare the source](%s/compare/%s...%s)."
    % (new_tag, REPO, new_tag, old_ref[:10], REPO, old_ref, new_tag)
)

out.append("\n## Token changes\n")
tokens = token_diff()
if tokens:
    out.append("CSS custom properties in `src/resources/theme` that changed. Each one maps to the kit variable with the same code syntax.\n")
    out.append("| Group | Property | Change | Old | New |")
    out.append("| --- | --- | --- | --- | --- |")
    for group, name, change, a, b in tokens:
        out.append("| %s | `%s` | %s | %s | %s |" % (group, name, change, cell(a), cell(b)))
else:
    out.append("No token changes.")

old_mdi, new_mdi = mdi_version(old_dir), mdi_version(new_dir)
out.append("\n## Icons\n")
if old_mdi != new_mdi:
    out.append("`@mdi/svg` changed from `%s` to `%s`. Import the new icons into the Icons page." % (old_mdi, new_mdi))
else:
    out.append("`@mdi/svg` is still `%s`." % new_mdi)

out.append("\n## Changed source files\n")
changes = file_diff()
if changes:
    out.append("Files in %s. Check the ones that match a kit component.\n" % ", ".join("`%s`" % w for w in WATCHED))
    for change, path in changes[:MAX_FILES]:
        link = "%s/blob/%s/%s" % (REPO, new_tag, path) if change != "removed" else "%s/blob/%s/%s" % (REPO, old_ref, path)
        out.append("- %s [`%s`](%s)" % (change, path, link))
    if len(changes) > MAX_FILES:
        out.append("- and %d more; see the comparison link above" % (len(changes) - MAX_FILES))
else:
    out.append("No changes in the watched folders.")

out.append(
    """
## To do

- [ ] Start Claude Code in a clone of this repo and run: `Reconcile the Home Assistant Design Kit with the frontend release %s in <path to the frontend clone>.`
- [ ] Review the changed components and foundations in Figma, in Light and Dark mode.
- [ ] Run the pre-publish check of the skill.
- [ ] Publish the team library and the Figma Community update.
- [ ] Merge the pull request that updates `design-kit/state.json` (`latestReleaseTag`, `frontendCommit`) and `design-kit/CHANGELOG.md`.

Opened by the design kit release check workflow."""
    % new_tag
)

body = "\n".join(out)
if len(body) > MAX_BODY:
    body = body[:MAX_BODY] + "\n\n_The report was cut off. See the comparison link above._"
print(body)
