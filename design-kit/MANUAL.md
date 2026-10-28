# Home Assistant Design Kit: manual

How the Home Assistant Design Kit in Figma is built, what was decided, and how to keep it in sync with the frontend. Kit 1 was built on 27 and 28 October 2026 in four phases: foundations, components, dashboard cards, and examples.

## Goal and constraints

The kit is a published Figma library of the Home Assistant frontend as it ships today: variables from the frontend's CSS tokens, components from the contributor component list and the frontend source, and example screens based on the demo. Community members duplicate it from Figma Community; OHF designers maintain it; a Claude Code session reconciles it with each frontend release.

| Constraint | Consequence for the kit |
| --- | --- |
| OHF Figma team is on the Professional plan | Library publishing, branching and Code Connect work. No Variables REST API, so token sync goes through the Figma MCP (Plugin API), not a server-side script. ([Code Connect plans](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect), [Variables API](https://developers.figma.com/docs/rest-api/variables)) |
| Frontend visuals are the source of truth | HomeCore stays a separate file. The kit follows `src/resources/theme/` and the shipped components, not the new design language. |
| Community members use a duplicate, not the live library | A duplicate is a snapshot; they re-duplicate to get updates. Versioning must be visible inside the file (cover page, changelog page). ([Publish to Community](https://help.figma.com/hc/en-us/articles/360040035974)) |
| Free Community files are CC BY 4.0 | Matches the open-source nature of the frontend. OHF can add a second license on top but cannot remove attribution. ([Community licensing](https://help.figma.com/hc/en-us/articles/360042296374-Figma-Community-copyright-and-licensing)) |
| Low maintenance wanted | Everything a human would retype is generated from code by the reconciliation run: variables, code syntax, component descriptions, links, the changelog. Humans review and publish. |
| Colleagues must be able to update it | The team profile owns the Community listing, so any team admin can publish updates. The maintenance manual below is written for a colleague who has never opened the file. |

## Decisions made while building kit 1

Taken during the build sessions of 27 and 28 October 2026. Where they differ from the sections below, the decisions win.

| Topic | Decision |
| --- | --- |
| Icons | All 7447 Material Design Icons (`@mdi/svg` 7.4.47, the version pinned in `package.json`) and the three Home Assistant custom icons are components in the kit, named `Icons / mdi / <name>` and `Icons / ha / <name>`, deprecated ones under `Icons / mdi / deprecated /`. Community members cannot reach a colleague's file, and a linked library does not travel with a duplicate. A version bump regenerates one SVG from `node_modules/@mdi/svg`, imports it, and converts only the missing names. The Pictogrammers plugin covers icons newer than the pinned version. |
| Icon slots | Every icon slot is an INSTANCE_SWAP with the icon the source imports (close, menu-down, magnify, and so on). Alert has no shared icon property because its icon differs per type. |
| Writing style | Kit text follows the style guide on contributors.home-assistant.io: American English, sentence case, "Home Assistant" in full, no Latin abbreviations, "select" not "click", people-first wording. The collections are named Core color, Semantic color, and Legacy color. The style guide itself is not copied into the kit. |
| Pages | Cover, Getting started, ---, Examples, ---, Color, Typography, Spacing and radius, Layout, Icons, ---, Actions, Input, Pickers, Forms, Feedback and status, Showing values, Layout and content, Controls, App shell, ---, Dashboard cards, ---, Changelog, License (24 pages). There is no _Build page. |
| Page organization | One page per group of the contributor components index, with a group guideline card at the top (two or three sentences on how to pick between the group's components, and a link per component that jumps to its section) and one Figma section per component below it, side by side 240px apart. A section holds what a component page held before: Guidelines, Examples, Components frame, sets. The frame of states is named Examples (Examples / Light, Examples / Dark), not Review: it shows every state as an instance, it is not something awaiting approval. The published library groups components by page, so the assets panel shows the nine groups. Controls, Control scrubber, and Select menu form their own Controls group; the site still lists them under Showing values. Dashboard cards keeps one page with a section per card group (Entity cards, Controls, Information, Grouping and layout, Media and pictures), each with its own guideline card and Examples. |
| Component section layout | Top to bottom: Guidelines card, 120px, Examples frame, 80px, a Components frame when the section has one, then the component sets 40px apart. Canvas #7D7D7D, component sets #8E8E8E, Examples frames #A4A4A4. No rounded corners on sections. Examples frames do not clip, so shadows show. |
| Guidelines card | 800px wide, no background, white text: 32px title (the component name), 18px body of at most two sentences, 18px links labeled `Contributor documentation › <Page>` in the dark-mode blue. No Source link in the card; the source link stays in the component description. |
| Cover | An instance of the roadmap cover template from the OHF Templates library with "DESIGN KIT" and the version (`Kit 1 · October 2026`), nothing else. The thumbnail is set by hand (Set as thumbnail); the Plugin API cannot. |
| License page | Links to the frontend license, the Material Design Icons license, the Roboto license, and the Home Assistant logo library. Nothing is restated or invented. The logo is referenced from the published logo library, not copied. |
| Changelog | The layout of Apple's design resources: one row per kit version, newest first. |
| Kit version | `git describe` on `dev` (`20260930.0-621-g316043960c / kit 1`), because the release tags live on release branches. A kit built from a release tag uses the tag. |
| Code Connect | Deferred. The Professional plan includes Code Connect for one library and one framework, and the kit is enabled in the team settings (Library: Home Assistant Design Kit; Framework: Web Components). The Figma MCP write tools stay refused on this plan, so the mappings are parserless template files (`*.figma.ts`, one per component set and component, 49 in total) in `design-kit/code-connect` in this repo, ready to publish with the Code Connect CLI and a personal access token (scopes Code Connect: Write, File content: Read): see the README in that folder. Publishing is skipped for kit 1: Dev Mode snippets only help OHF developers on the team file, Community duplicates never carry them, and every component description keeps its Source link. |
| Library publishing | The kit is published as a team library in the Open Home Foundation Figma team, which Code Connect needs, and as a free file on Figma Community. |
| Variables | 549 variables in 8 collections. Button size is a collection with modes xs, s, m, and l, so size is a mode, not a variant axis. Line-height variables are reference only, because a bound number applies as pixels. The frontend derives the `--rgb-*` triplets at runtime, so the dark values of the six `rgba()` users are set from #e1e1e1. |
| Tints and shadows | Tints that the code draws with `rgba()` or opacity are overlay rectangles with layer opacity, because the renderer ignores paint opacity on variable-bound fills. Shadows are plain effects; the kit has no effect styles. |
| Components | Every control on the Controls page is built, including the circular slider. Selector covers 9 of the 60+ selector types. The "Replaced device" state of the Device picker is skipped on purpose. |
| Dashboard cards | One page, Dashboard cards, with the 14 cards of the plan as component sets built from the kit's components (tile, entity, button, entities with entity rows, glance, heading, area, gauge, weather forecast, thermostat, light, media control, Markdown, picture entity). Reference section 412px: 12 columns of 27px with 8px gaps, rows of 56px with 8px gaps, so 6 columns are 202px and 2 rows 120px. Sizes come from each card's getGridOptions and styles; the reference renders are the live demos on the contributor card pages, captured in light and dark mode. The four weather state SVGs of the frontend are icon components under Icons / weather. |
| Examples | The page of screens is named Examples, not Templates, and sits after Getting started. One Figma section per window size class, named Wide (1440 x 900, sidebar expanded, three 352px columns), Docked (1024 x 768, sidebar collapsed, two 436px columns) and Narrow (390 x 844, no sidebar, one 374px column); each holds the demo dashboard and the Settings overview side by side under a guideline card. The Welcome section of the demo is left out. Screens are built from Tile, Heading, Entity, Badge and Icon button instances with overrides and from the App shell components (Sidebar, Top bar, Navigation row). The Settings screens carry the updates card of ha-config-dashboard with the brand icons as entity pictures. Every screen has its view or settings grid style and every section frame the section grid style. |
| Kit leads, site follows | The rule that the contributor site must document a component before the kit builds it is dropped. Elements that exist in the frontend but not on the site (the app shell: sidebar, top bar, navigation row, user badge, and later the more-info dialog, data table, and others) are built in the kit from their source files, with the description written from the code and the Docs line marked as not on the site yet. The site gets its page later, drafted from the kit text. Components that the site does document keep the site text as their source. |
| State file | `design-kit/state.json` in this repo holds the node ID of every page, section, component set, variable, style and icon, plus the frontend issues found. Update it after every change, so the next run does not have to search the file. |
| Location | The team library is the file "Home Assistant Design Kit" in the Open Home Foundation Figma team, Design System project. Its link is not published; ask a team admin. The MCP cannot move files between projects. |
| App shell | A ninth component group page, App shell, after Controls: User badge, Sidebar item, Sidebar (Expanded, Collapsed), Top bar (see Top bar variants) and Navigation row (with or without description). Built from ha-sidebar, the hui-root and hass-subpage toolbars, ha-navigation-list and ha-user-badge; the contributor site has no page for them, so the descriptions say the kit leads. The Examples screens use these instances. |
| Layout | A Layout page in Foundations after Spacing and radius. Four window size classes name the frontend breakpoints: Narrow 0 to 599px (sidebar drawer, narrow top bar, edge-to-edge settings cards), Compact 600 to 869px (still a drawer, two dashboard columns from 672px), Docked 870 to 1039px (sidebar docked) and Wide 1040px and up (isWide config layout). The page shows the sections view rules (columns of 320 to 500px, 32px gap, 8px below 600px, 24px row gap) and the section grid (12 columns, 8px gutter, 56px rows, 8px gap) with 1/4-scale schematics, and lists seven grid styles: Section / 12 columns + 56px rows, Dashboard view / Wide 1440, Docked 1024, Narrow 390, and Settings / Wide 1440, Docked 1024, Narrow 390. The size tokens stay on Spacing and radius. |
| Entity pictures | Brand icons (brands.home-assistant.io PNGs) are uploaded with the Figma upload_assets tool as the image fill of the 40px "entity picture" layer of Navigation row Leading=Picture, and of the "brand icon" layer of Data table row. Used for the updates card on the Settings screens and the Devices tables. |
| Top bar variants | Type=Panel (title first, or the menu button on narrow screens), Type=Subpage (back arrow first) and Type=Tabs (back arrow, Tab bar centered, hass-tabs-subpage on wide screens), each with Narrow=No\|Yes except Tabs. The icon buttons at the end are the booleans Action 1 to Action 3 on a fixed 144px right-aligned group of exposed Icon buttons, so one instance shows none to three and the icons are swapped per instance; a dashboard is a Panel with add, search and edit. The former Type=Dashboard is gone. Title offsets follow the source: 36px on wide screens (12px padding plus a 24px margin), 84px behind the back arrow, 60px on narrow screens. |
| Second batch of components | Built on 2026-10-28, all without a contributor page, so the kit leads. App shell: Tab (State, Label, Icon with Icon swap), Tab bar (four exposed tabs on a 2px divider track), Sidebar Layout=Drawer (the expanded sidebar with the drawer shadow, paired with a 32% black scrim). Layout and content: Data table header and Data table row (the Devices table columns: icon, Device, Area, Integration, Manufacturer, Model, Battery; Select mode adds the checkbox, Sorted the arrow, Battery icon the battery), Card header (linked title with chevron), Divider (Horizontal, Vertical). Feedback and status: Toast (Action=No\|Yes, Message); the Dialog section shows the climate more-info dialog as a composed example (see Dialog header and composed dialogs). Dashboard cards: Tile card Badge boolean (orange exclamation badge at the icon corner), Entity row Type=Divider and Type=Section. Navigation row Leading=Icon\|Picture and User badge Avatar=Initials\|Picture. Not built: the mobile tab bar, which the frontend does not have. |
| Examples, second batch | Wide: a Devices screen (Top bar Type=Tabs with icon tabs, the full-width search toolbar with Filters, selection mode, search, Group by, Sort by and the columns button, the full-width Data table, the Add device button (Button, size l, in the fab slot; not a separate component), a badge of 3 on the Settings sidebar item) and the dashboard with the climate more-info dialog open over a scrim. Narrow: the dashboard with the drawer open over a scrim, and a Toast at the bottom of the Settings screen. Data in the tables and dialogs is invented, not copied from a real instance. |
| Dialog header and composed dialogs | ha-dialog-header is its own component, Dialog header, in Feedback and status: a navigation icon button, the title, Breadcrumb (a small line above the title, as the more-info dialog shows the area), Subtitle (below), and Action 1 to Action 3 as exposed icon buttons. A composed dialog example (the climate more-info) is a frame styled like the Dialog with a Dialog header instance, a body of kit instances (Control circular slider recolored to the heat color, Select menu for the mode) and nothing detached. The Dialog set keeps its own header frame for now; nesting the Dialog header in it would move Title and Subtitle to the nested instance, which is a separate decision. Icons of a nested Icon button are set through its Icon swap property, not by swapping the inner instance. |
| Data table borders | The header row draws no border; every row draws a 1px top border, so the header and the first row share one line, as in the frontend where only a row after another row has a top border. Config tables run full width without the outer border (hass-tabs-subpage-data-table sets the border width to 0); a standalone table keeps it. |
| Examples per size, second batch | Each size section holds the Devices screen and the more-info dialog. Wide shows every column; Docked hides the Model column; Narrow uses the 72px Data table row Layout=Narrow (name with one truncated description line, battery at the end), puts the search field in the top bar and the filter chips in a row below it, and has no header row. The more-info dialog is 580px wide over a scrim on Wide and Docked and fills the screen without corners on Narrow. |

## Sources of truth

Every value in the kit traces to one file in the frontend repo or one page on the contributor site. The reconciliation run reads these and nothing else, so the list below is also the list of what triggers an update.

| What | Where in `home-assistant/frontend` (branch `dev`) | Goes into |
| --- | --- | --- |
| Core color palettes (primary, neutral, orange, red, green, 11 steps each, plus black and white) | [src/resources/theme/color/core.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/core.globals.ts) | Collection `Core color`, one mode, hidden scopes |
| Semantic colors (text, border, fill, on, surface, form) with light and dark values | [src/resources/theme/color/semantic.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/semantic.globals.ts) | Collection `Semantic color`, modes Light and Dark, aliased to Core |
| Legacy theme variables (`--primary-text-color`, `--card-background-color`, state colors and so on) | [src/resources/theme/color/color.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/color.globals.ts) | Collection `Legacy color`, modes Light and Dark; still used by most cards |
| Web Awesome mapping (`--wa-color-*` to `--ha-color-*`) | [src/resources/theme/color/wa.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/wa.globals.ts) | Not separate variables; used as the component-to-token lookup when building Web Awesome based components |
| Spacing (`--ha-space-1` to `-20`, 4px steps), border radius (`sm` 4px to `6xl` 36px, pill, circle), border width, animation durations | [src/resources/theme/core.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/core.globals.ts) | Collections `Spacing` and `Radius`; durations go on the Foundations page as text |
| Typography: Roboto, 14px base, sizes xs 10px to 5xl 40px, weights 300/400/500/700, line heights 1.2/1.6/2 | [src/resources/theme/typography.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/typography.globals.ts) | Collection `Typography` plus text styles |
| Header height 56px, opacities for text on light and dark | [src/resources/theme/main.globals.ts](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/main.globals.ts) | Collection `Layout` |
| Component inventory, specs and usage text | [contributors.home-assistant.io/design/components](https://contributors.home-assistant.io/design/components/) | Component descriptions and the guideline notes next to each component |
| Component source | [src/components](https://github.com/home-assistant/frontend/tree/dev/src/components) | Code Connect targets and the "source" link in each component description |
| Dashboard layout: 12-column sections 320 to 500px wide, 56px rows, 8px row gap, tile card is half a section by one row | [contributors.home-assistant.io/design/dashboards](https://contributors.home-assistant.io/design/dashboards/) | The Layout page and the grid styles of the Examples screens |
| Reference screens | [demo.home-assistant.io](https://demo.home-assistant.io/#/lovelace/home) | Examples screens, visually checked, not scraped |
| Release tags, for example 20260930.5 published 23 Oct 2026 | [Releases](https://github.com/home-assistant/frontend/releases) | The kit's version label |

Known frontend issues, reported and not invented: the dark semantic styles reference `--ha-color-neutral-00` and `--ha-color-90`, which do not exist in core.globals.ts, and `--ha-color-border-normal` in dark mode has no light counterpart. Every run reports these, and new ones, in `frontendIssues` in state.json.

## File structure

One library file, `Home Assistant Design Kit`, in the Open Home Foundation team, published to Figma Community as a duplicate. Pages mirror the contributor site so a reader can go from a Figma page to its documentation page with one link.

| Page | Contents |
| --- | --- |
| Cover | Instance of the OHF roadmap cover template with the kit name and version (`Kit 1 · October 2026`), nothing else. License and links live on their own pages. |
| Getting started | How to use the kit: enable the library, switch Light and Dark mode, swap icons, where guidelines live, how to check for a newer version |
| Changelog | One row per kit version: date, frontend release, what changed, who published |
| Color | Core and semantic swatches generated from variables, with the CSS variable name on each |
| Typography | Text styles table, font size scale, weights |
| Spacing and radius | Spacing scale, radius scale, border widths |
| Icons | All Material Design Icons of the `@mdi/svg` version in `package.json` and the Home Assistant custom icons as components, plus the `ha-icon` placeholder with INSTANCE_SWAP |
| Components: nine group pages (Actions, Input, Pickers, Forms, Feedback and status, Showing values, Layout and content, Controls, App shell), one Figma section per component | Group guideline card with links to the sections; each section: component guideline, Examples frame with Light and Dark panels, component sets; descriptions, links, and Dev Mode annotations on each set |
| Layout | Window size classes, the dashboard grids, and the grid styles |
| Dashboard cards | The 14 card types, built from the components at a 412px reference section, one section per card group with Guidelines and Examples; the weather state icons under Icons / weather |
| Examples | One section per window size class (Wide, Docked, Narrow) with the demo dashboard, the Settings overview, the Devices table and the climate more-info dialog; Narrow adds the drawer and a toast. Frames, not components |
| License | Links to the frontend license, the Material Design Icons license, the Roboto license, and the logo library; nothing restated |

Variables follow the frontend names so code syntax is a lookup, not a translation. Each variable gets WEB code syntax `var(--ha-color-text-primary)` and the scopes the figma-generate-library skill prescribes.

| Collection | Modes | Source | Count (approx.) |
| --- | --- | --- | --- |
| Core color | Value | core.globals.ts | 57 |
| Semantic color | Light, Dark | semantic.globals.ts | 103 |
| Legacy color | Light, Dark | color.globals.ts | 305 |
| Spacing | Value | core.globals.ts | 20 |
| Radius | Value | core.globals.ts | 12 plus 3 border widths |
| Typography | Value | typography.globals.ts | 9 sizes, 4 weights, 3 line heights, 3 families |
| Layout | Value | main.globals.ts, dashboards page | header 56, row 56, row gap 8, section min 320, section max 500 |

The component inventory of kit 1 started from the contributor component list, grouped the way the site groups it. The App shell group and the components the site does not document yet (data table, card header, divider, toast, dialog header) were added later; see the decisions above.

| Group | Components |
| --- | --- |
| Actions | Button, Progress button, Dropdown |
| Input | Text input, Textarea, Switch, Slider, Select box, Color picker |
| Pickers | Entity picker, Device picker, Area picker |
| Forms | Form, Selector |
| Feedback and status | Alert, Dialog, Adaptive dialog, Badge, Label badge, Spinner, Tooltip, Tip, State icon |
| Showing values | Bar, Gauge, Controls, Control scrubber, Select menu |
| Layout and content | List, Expansion panel, Marquee text, Faded |
| Dashboard cards | Tile, Entity, Button, Entities, Glance, Heading, Area, Gauge, Weather forecast, Thermostat, Light, Media control, Markdown, Picture entity |

Components are built in dependency order: State icon and Badge before Tile card, Button before Dialog, List before Entity picker. Variant matrices stay under 30 combinations; Button is split into `Button` (appearance x size x state) and `Icon button`.

## Guidelines inside Figma

Guidelines live where a designer meets the component, in three places Figma already has, and all three are generated from the contributor site so they never go stale by hand.

| Mechanism | What goes in it | Generated from |
| --- | --- | --- |
| Component description (shows in the assets panel and the properties panel on hover) | First paragraph of the contributor page: what it is, when to use it, when not to. Plus two links: documentation page and source file on GitHub. | `design/components/<name>` page, `src/components/ha-<name>.ts` |
| Annotations (Dev Mode, on the main component) | Spec values that are not visible from the layers: minimum touch target, keyboard behavior, what the frontend does on narrow screens | Specs section of the contributor page |
| Guideline frame next to the component set (a plain frame named `Guidelines`, with a note-styled text block and link text) | Two sentences of usage rules and one link per documentation page, labeled `Contributor documentation › <Page>`. Do and don't examples are not built yet. | Same page, Patterns pages |
| Code Connect | Maps each Figma component to its `src/components` file so Dev Mode shows the real element name and props | Code Connect CLI with one template file per component (label Web Components), after the library is published and enabled for Code Connect in the team settings. The Figma MCP cannot write Code Connect on the Professional plan. |
| Variable code syntax | The CSS variable name on every variable, so inspect shows `var(--ha-space-4)` not `16` | Variable names |

Figma's native notes (the sticky note tool) are a FigJam feature; in Design files the equivalent is a text block styled as a note inside the Guidelines frame, plus Dev Mode annotations. Links in text are clickable in Figma, so the guideline card links to the documentation page, and the component description ends with `Docs` and `Source` links.

On the Community duplicate, descriptions, annotations and guideline frames all survive. Code Connect mappings belong to the team file and do not travel with the duplicate; that is acceptable because community members do not have Dev Mode on the OHF codebase.

## Versioning and sync

The kit version is the frontend release tag it was reconciled against, plus a kit increment: `20260930.5 / kit 1`. A second kit publish against the same frontend release is `kit 2`. Anyone looking at a Community duplicate can tell at once which frontend it matches.

A frontend release triggers one Claude Code run; the run never publishes, a person does.

What the run does, in order:

1. Reads the theme files listed in Sources of truth from the release tag, and the component pages from the contributor site.
2. Reads the kit: all variables with their code syntax, all component descriptions, the changelog page.
3. Produces a diff: new, changed and removed variables; changed description text; components on the site that have no Figma component; Figma components whose source file moved.
4. Creates a Figma branch named after the release tag and applies the diff there through the Figma MCP. Variable values change in place so bindings survive. Removed variables are renamed with a `deprecated/` prefix, never deleted, so Community duplicates do not break.
5. Writes the changelog row and the new version on the cover, on the branch.
6. Posts the diff summary and the branch link in the design channel.

What is automatic and what is not:

| Automatic (the run) | Manual (a designer) |
| --- | --- |
| Variable values, names, modes, code syntax | Visual check of the Examples frames in Light and Dark |
| Component descriptions, links, annotations text | Building a new component when the site adds one (the run only creates a placeholder with the description) |
| Changelog row, cover version | Merging the branch, publishing the library, publishing to Community |
| Diff report and frontend issues found (missing tokens, dangling references) | Deciding whether a frontend issue should be filed |

Trigger: a scheduled check once a week on the releases list is enough; frontend releases ship roughly monthly with patch releases in between, and only tag-level changes to the theme files matter. The check compares the latest tag with the version on the cover and starts a run when they differ. A colleague can also start a run by hand with the prompt in the manual.

## Maintenance manual

This is the part colleagues follow. It assumes a Full seat on the Open Home Foundation Figma team, Claude Code with the Figma MCP connected, a local clone of `home-assistant/frontend`, and a local clone of this repo. A copy of this section goes on the kit's Getting started page as a link.

**Setup, once per person**

1. Clone `home-assistant/frontend` and check out the `dev` branch.
2. In Claude Code, connect the Figma MCP and sign in with your OHF Figma account.
3. Clone `OpenHomeFoundation/ux-design`. The `ha-figma-kit` skill is in `.claude/skills/ha-figma-kit` and loads when you start Claude Code in that clone, so everyone runs the same instructions.
4. Get the link of the team library file from a team admin. Keep it out of this repo; the skill asks for it.

**Run a reconciliation**

1. In the frontend clone: `git fetch --tags && git checkout <release tag>`.
2. Start Claude Code in the ux-design clone and run: `Reconcile the Home Assistant Design Kit with the frontend release <tag> in <path to the frontend clone>. Use the ha-figma-kit skill. Work on a new Figma branch named after the tag. Do not publish.`
3. Wait for the diff summary. It lists variables added, changed, removed, descriptions changed, components missing, and frontend issues found.
4. Open the branch link. Check the Foundations pages and the Examples frame of every changed component in Light and Dark mode.
5. Anything wrong: comment on the branch and tell Claude Code what to fix; it edits the branch. Never fix by hand on `main`.
6. Merge the branch in Figma (Branch menu, Review and merge).

**Publish**

1. Ask Claude Code to run the pre-publish check of the skill. It finds component properties that no layer uses and property names that clash with a variant axis; Figma refuses to publish either.
2. Assets panel, Library, Publish. Write the release note as the changelog row text.
3. Share, Publish to Community, Publish update. Keep the listing text; update the thumbnail only if the cover changed.
4. Post the changelog row in the design channel and in the UX Design discussions "Design system" category.

**Add a new component**

1. Check whether the contributor site documents it. If it does, the description comes from that page. If it does not, the kit leads: build it from the source file, write the description from the code and the element's doc comment, and mark the Docs line as not on the site yet. The site page follows later, with the kit text as its draft.
2. Run Claude Code in the ux-design clone with: `Add the <name> component to the Home Assistant Design Kit from src/components/ha-<name>.ts and its contributor page, on a branch.` The run creates variables it is missing, the component set, the Examples frame, the description, links and a Code Connect template.
3. Review, merge, publish as above.

**Rules that keep maintenance low**

- Variables are only ever edited by the run. A value typed by hand is overwritten at the next run.
- Never delete a variable or component; rename with `deprecated/`. Community duplicates rely on stable names.
- One branch per run, named after the frontend tag. Branches older than two releases are deleted.
- There is no working page. The run removes its helper frames before handing over.
- `design-kit/state.json`, `design-kit/CHANGELOG.md` and this manual are committed to `ux-design` after each run, so a run interrupted halfway can resume and the next person starts from the same state.

**If the run cannot reach Figma**: the Figma MCP needs the desktop app open or a signed-in account with a Full seat. Rate limits on the Professional plan can pause a long run; the skill tells Claude Code to continue from the state ledger.

## Publishing to Figma Community

Publish from the Open Home Foundation team's Community profile, not a personal one, so any team admin can push updates and the listing survives staff changes. Figma states that when a file is published to a team profile only that team's admin can publish updates, and that the Professional plan can publish free files ([Publish files to the Figma Community](https://help.figma.com/hc/en-us/articles/360040035974)).

| Listing field | Value |
| --- | --- |
| Name | Home Assistant Design Kit |
| Description | What it is, which frontend release it matches, link to the contributor site, link to the ux-design discussions for feedback, credit to the frontend contributors |
| Category and tags | UI kits; tags `home assistant`, `smart home`, `open source`, `dashboard`, `design system` |
| Thumbnail | The 1920 x 1080 cover (roadmap cover template with the kit version), set by hand with Set as thumbnail after each cover change |
| Support contact | The ux-design discussions URL |
| Comments | On, so community feedback lands on the listing |
| License | CC BY 4.0, which Figma applies to every free file ([Community copyright and licensing](https://help.figma.com/hc/en-us/articles/360042296374-Figma-Community-copyright-and-licensing)) |

What a Community duplicate is and is not: it is a snapshot of the file at publish time, with no version history and no link to the library. People get updates by duplicating again. That is why the cover shows the version and the Getting started page tells them how to check for a newer one. Likes and duplicate counts carry across updates, so publishing often costs nothing.

The listing belongs to the team Community profile with the OHF name and logo. Its text and avatar are public OHF branding, so the marketing team owns them.
