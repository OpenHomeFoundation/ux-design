# Home Assistant Design Kit

The [Home Assistant Design Kit](https://www.figma.com/community/file/1697311104929761103/home-assistant-design-kit) on Figma Community is the official Figma library for the Home Assistant interface, maintained by the Open Home Foundation. Its variables, text styles, and components are generated from the [frontend](https://github.com/home-assistant/frontend) source, so what you design matches what ships. It includes light and dark modes, the [components](https://contributors.home-assistant.io/design/components/) documented on the contributor site, and usage guidelines with links to the docs and source for each one. Mockups that start from it stay close to what can be built.

This folder holds what you need to maintain the kit. To use the kit, duplicate it from Figma Community.

## Where the kit lives

- **Figma Community.** The public file at the link above. A duplicate is a snapshot: duplicate it again to get a newer version. The cover and the Changelog page show which version you have.
- **Team library.** The source file is "Home Assistant Design Kit" in the Design System project of the Open Home Foundation Figma team. It is published as a team library. Its link is not in this repo. Ask a team admin for access.

## What is in this folder

| File | What it is for |
| --- | --- |
| [MANUAL.md](MANUAL.md) | Decisions, sources of truth, page conventions, and the maintenance steps |
| [CHANGELOG.md](CHANGELOG.md) | One entry per kit version, with the frontend commit it matches |
| [state.json](state.json) | Node IDs of every page, section, component set, variable, style and icon in the team library, plus the frontend issues found |
| [scripts/](scripts/) | Token extraction, the state patch helper and the Code Connect generator |
| [code-connect/](code-connect/) | Code Connect templates, ready but not published |

The Claude Code skill that updates the kit is in [.claude/skills/ha-figma-kit](../.claude/skills/ha-figma-kit/SKILL.md).

## Update the kit

You need a Full seat on the Open Home Foundation Figma team, Claude Code with the Figma connector, a clone of this repo and a clone of `home-assistant/frontend`.

1. Start Claude Code in the clone of this repo, so the skill loads.
2. Ask for the change. For example:
   - `Reconcile the Home Assistant Design Kit with the frontend release <tag> in <path to the frontend clone>.`
   - `Add the <name> component to the Home Assistant Design Kit from src/components/ha-<name>.ts.`
   - `Run the pre-publish check on the Home Assistant Design Kit.`
3. Give the link of the team library file when the skill asks for it.
4. Review the changes in Figma in Light and Dark mode.
5. Publish the library and the Community update yourself. The skill never publishes.
6. Commit the updated `state.json`, `CHANGELOG.md` and `MANUAL.md` in a pull request.

The [maintenance manual](MANUAL.md#maintenance-manual) has the full steps.

## Scripts

Run them with Python 3. They have no dependencies.

```sh
# Read the CSS custom properties of the theme files
python3 design-kit/scripts/extract_tokens.py <frontend clone> tokens.json

# Map them to Figma collections, modes and scopes, and list frontend issues
python3 design-kit/scripts/plan_tokens.py tokens.json plan.json

# Merge a JSON patch into state.json
python3 design-kit/scripts/patch_state.py design-kit/state.json patch.json

# Regenerate the Code Connect templates
python3 design-kit/scripts/gen_code_connect.py design-kit/code-connect
```

To see what changed between two frontend releases, run `extract_tokens.py` on both and compare the two JSON files.

## Request a change

Start a discussion in the [Design system](https://github.com/OpenHomeFoundation/ux-design/discussions) category of this repo. Link the frontend pull request or the contributor page when there is one.
