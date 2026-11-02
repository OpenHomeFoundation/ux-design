# Changelog

One entry per kit version, newest first. The Changelog page in the Figma file has the same text.

## Kit 2, November 2026

Built from the frontend at `dev` 316043960c (`20260930.0-621-g316043960c`), the same as kit 1.

### Input

- Select, time input, duration input, date input with its date picker, button toggle group, labeled slider (plain and color temperature track), color input, code editor (YAML and template, with the codemirror syntax colors), and file upload.

### Pickers

- Picker: the generic picker field, with an icon or a color swatch.
- Icon picker, chip (input and assist), target picker with target rows, and multi-picker list.

### Forms

- The selector set grows from 9 to 24 variants, one per kind of control.
- A table maps all 61 selector types of the frontend to their kit component.

### App shell

- Notification badge: the count on sidebar entries. It is not the same as Badge.
- Sidebar item shows its count with a nested Notification badge. Set the count on that instance; the Badge count property is gone.

### Annotations

- Dev Mode annotations for every new component, and for the tab, tab bar, data table header and row, card header, divider, toast and dialog header.

## Kit 1, October 2026

Built from the frontend at `dev` 316043960c (`20260930.0-621-g316043960c`).

### Foundations

- Variables for color (core, semantic, legacy), spacing, radius, typography and layout, with the CSS custom property as code syntax.
- 108 Roboto text styles.
- Color, Typography, Spacing and radius, Layout, and Icons pages.
- Seven grid styles for sections, dashboard views and settings screens.

### Components

- Eight group pages (Actions, Input, Pickers, Forms, Feedback and status, Showing values, Layout and content, Controls) with a section per component. 32 documented components; Button is split into Button and Icon button.
- App shell page: sidebar (with drawer), sidebar item, top bar, tab bar, navigation row, user badge.
- Components the contributor site does not document yet: data table, card header, divider, toast, dialog header.
- Variants for the documented states, variable bindings, descriptions with Docs and Source links, guidelines, and Examples in Light and Dark.

### Icons

- All 7447 Material Design Icons of version 7.4.47, plus the Home Assistant custom icons, as components.

### Dashboard cards

- 14 cards built from the components: tile (with badge), entity, button, entities with entity rows (with divider and section rows), glance, heading, area, gauge, weather forecast, thermostat, light, media control, Markdown, and picture entity.
- Weather state icons from the frontend under Icons / weather.

### Examples

- Screens built from the components, one section per window size class (Wide, Docked, Narrow): the demo dashboard, the Settings overview with the updates card, the Devices table and the climate more-info dialog. Narrow adds the drawer and a toast.

### Not included

- Code Connect: templates are ready in `code-connect/` but not published.
- The "Replaced device" state of the device picker.
- A mobile tab bar: the frontend does not have one.
