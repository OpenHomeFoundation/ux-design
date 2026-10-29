# Kit conventions

Numbers and rules the kit uses on every page. Node IDs are in `design-kit/state.json`.

## Writing

- Follow the style guide on contributors.home-assistant.io: American English, sentence case, "Home Assistant" in full, "select" not "click", no Latin abbreviations, people-first wording.
- Guideline text: at most two sentences on what the component is for and what to use instead.
- Component description: what it is and when to use it, then two lines:
  - `Docs: <contributor page URL>`, or `Docs: not on the contributor site yet; the kit leads.`
  - `Source: https://github.com/home-assistant/frontend/blob/dev/<path>`
- Descriptions cannot hold hyperlinks, so they keep the raw URLs. Guideline cards use descriptive link labels instead: `Contributor documentation › <Page>` or `Frontend source › <file>.ts`.
- Example data is invented. Never copy names, areas or devices from a real home.

## Pages

- Order: Cover, Getting started, ---, Examples, ---, Color, Typography, Spacing and radius, Layout, Icons, ---, Actions, Input, Pickers, Forms, Feedback and status, Showing values, Layout and content, Controls, App shell, ---, Dashboard cards, ---, Changelog, License.
- Canvas color #7D7D7D. Square corners on sections and frames that are not part of a component.

## Group page

- A page header card at the top left: 1000px wide, title 48px Bold (120% line height), body 20px (150%), no links.
- One Figma section per component, 120px below the header, side by side 240px apart.

## Component section

Top to bottom, 40px inside the section:

1. **Guidelines card.** 800px wide, no background, Semantic color mode Dark so links show the dark-mode blue. Title 32px Bold (120%), body 18px Regular (150%), links 18px Medium.
2. **Examples frame**, 120px below. Fill #A4A4A4, padding 40, gap 40, horizontal auto layout, no clipping so shadows show. Two panels, `Examples / Light` and `Examples / Dark`: card background variable, radius 12, padding 24, gap 16, a 12px Medium label in the secondary text color. The Dark panel sets Semantic color to Dark and Legacy color to Dark.
3. **Component sets**, 80px below, 40px apart. Fill #8E8E8E, padding 40, gap 40 between variants, no corner radius. Single components that are not sets sit in a `Components` frame with the same fill.

The section is 40px larger than its content on the right and bottom.

## Components

- Variant axes: `State` for interaction states, `Layout` or `Type` for structure, `Size` only when a variable mode cannot do it. Button size is a variable mode (Button size collection), not an axis.
- Text and booleans are component properties. Icon slots are instance swap properties with the icon the source imports as default.
- Icon buttons nested in a component are exposed instances, so their icon is set per instance through the `Icon` swap property.
- Optional actions are booleans on a fixed group (for example Action 1 to Action 3), not separate variants.
- Tints and scrims are overlay rectangles with layer opacity.

## Examples page

- One section per window size class, stacked: Wide (1440 x 900, sidebar expanded), Docked (1024 x 768, sidebar collapsed), Narrow (390 x 844, no sidebar).
- Each section starts with a guideline card that states the grid numbers for that size.
- Screens are frames named `Examples / <Screen>`, built from instances, clipped at the frame edge.
- Screens carry the matching grid style (`Dashboard view / …` or `Settings / …`); every dashboard section frame carries `Section / 12 columns + 56px rows`.

## Layout numbers

| Rule | Value |
| --- | --- |
| Window size classes | Narrow 0 to 599px, Compact 600 to 869px, Docked 870 to 1039px, Wide 1040px and up |
| Sidebar | Expanded 256px, collapsed 56px, drawer below 870px |
| Top bar | 56px; title at 36px on wide screens, 84px behind the back arrow, 60px on narrow screens |
| Sections view | Columns 320 to 500px, gap 32px (8px below 600px), row gap 24px |
| Section grid | 12 columns, 8px gutter, rows 56px, gap 8px |
| Settings column | Centered, max 600px; edge to edge without radius below 600px |
| Data table | Header 56px, rows 52px (72px two-line on narrow screens), 1px divider above each row only |
| Fab slot | 16px from the bottom and end edges; the button is a Button, size l |
