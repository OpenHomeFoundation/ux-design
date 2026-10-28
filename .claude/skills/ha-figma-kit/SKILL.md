---
name: ha-figma-kit
description: Update, extend or check the Home Assistant Design Kit in Figma. Use when asked to sync the kit with a frontend release, add or change a component, card, example screen, variable or icon in the kit, fix a kit component, or check the kit before it is published.
---

# Home Assistant Design Kit

The kit is a Figma library generated from the Home Assistant frontend. This skill keeps it in sync and extends it. The manual in `design-kit/MANUAL.md` holds the decisions; read its decisions table before you change anything.

## Inputs

Ask for what you do not have. Do not guess.

- **Figma file link** of the team library "Home Assistant Design Kit". Never write it to a file in this repo, a commit, or a pull request.
- **Frontend clone path** and the release tag or commit to build from. If there is no clone, ask before you clone one.
- **Scope**: reconcile a release, add or change a component, add an example screen, or the pre-publish check.

## Before the first Figma call

1. Load the Figma skills: `figma-use` always; `figma-generate-library` for components, variables and styles; `figma-generate-design` for example screens. Follow their rules.
2. Read `design-kit/state.json`. It maps names to node IDs, variable IDs and text style keys. Never rebuild what it lists.
3. Read [references/conventions.md](references/conventions.md) for page layout and writing rules, and [references/figma-gotchas.md](references/figma-gotchas.md) for the Plugin API traps that cost time before.
4. Copy the helpers you need from [references/helpers.js](references/helpers.js) into each `use_figma` script.

## Working rules

- Run one `use_figma` call at a time. Never run them in parallel.
- Switch page at most once per call with `await figma.setCurrentPageAsync(page)`.
- Build from kit components and variables only. Bind colors, spacing and radius to variables; do not hard-code a value that has a variable.
- Never delete a published variable or component. Rename it with a `deprecated/` prefix.
- Never publish the library or the Community file. A person does that.
- After each visible change, take a screenshot with `get_screenshot`, look at it, and fix what is wrong before you go on.
- Every component description ends with a Docs line and a Source line (see conventions).

## Tasks

### Reconcile a frontend release

1. In the frontend clone, run `design-kit/scripts/extract_tokens.py` at the commit in `state.json` (`frontendCommit`) and at the new tag. Compare the two outputs.
2. Run `plan_tokens.py` on the new output to get collections, aliases and the frontend issues.
3. Diff the documented components: the contributor component pages and `src/components` files against the sets in `state.json`.
4. Apply the diff on a Figma branch named after the tag, if branches are available; otherwise ask where to work. Change variable values in place so bindings survive.
5. Report variables added, changed and deprecated, descriptions changed, components missing, and new frontend issues.

### Add or change a component

1. Check whether the contributor site documents it. If it does, the description and guideline come from that page. If it does not, the kit leads: write them from the source file and mark the Docs line as not on the site yet.
2. Read the source file: properties, states, sizes, slots, CSS custom properties.
3. Build the component set in a new section on the right group page, with Guidelines, Examples (Light and Dark) and the set, as in conventions.
4. Wire component properties (text, boolean, instance swap) and expose nested instances that people need to change.
5. Add a Code Connect template with `scripts/gen_code_connect.py`, if the component maps to one element.

### Add an example screen

Build it in the section of its window size class on the Examples page, from instances only. Use the screen sizes and grid styles in conventions. Use invented data, never data from a real home.

### Pre-publish check

Run the `checkProperties` helper on every page except Icons. Fix every hit:

- A non-variant property that no layer references: bind it or delete it.
- A property name that is also a variant axis name: rename the property, for example `Description text`.

Figma refuses to publish a library with either problem.

## Close out

1. Patch `design-kit/state.json` with the new IDs, the frontend commit and the completed steps (`scripts/patch_state.py`).
2. Add the change to `design-kit/CHANGELOG.md` and to the Changelog page in Figma.
3. Add a row to the decisions table in `design-kit/MANUAL.md` for every new decision.
4. Update the Getting started page in Figma when pages or groups change.
5. Add new Plugin API lessons to `references/figma-gotchas.md`.
6. Tell the person what changed, what to check in Figma, and that they must publish.
