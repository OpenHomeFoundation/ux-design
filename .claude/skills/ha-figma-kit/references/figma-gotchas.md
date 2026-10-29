# Figma Plugin API gotchas

Lessons from building kit 1. Each one cost at least one failed or wrong run.

## Calls and pages

- `use_figma` rolls back every change of a call when the script throws. Fix the error and run the whole call again.
- Run one call at a time. Parallel calls on the same file interfere.
- `figma.currentPage = page` is not supported. Use `await figma.setCurrentPageAsync(page)`, once per call. To read another page in the same call, use `await page.loadAsync()`.
- Load every font before you change text, append text, or set text properties: `await figma.loadFontAsync(...)` for each segment of `getStyledTextSegments(['fontName'])`.

## Variables and paints

- `setBoundVariableForPaint` takes a variable object, not an ID string. Fetch it with `await figma.variables.getVariableByIdAsync(id)`.
- The renderer ignores paint opacity on a variable-bound fill. Draw tints and scrims as a separate rectangle with layer opacity.
- Spreading a bound paint drops its opacity. Set the fills first, then JSON-clone them and set the opacity.
- Bound line-height numbers apply as pixels. The line-height variables hold percentages for reference only.
- Variable keys in `state.json` use the collection names Core color, Semantic color and Legacy color.

## Components and properties

- Append a new variant to its component set before you set `componentPropertyReferences` to the set's properties. Otherwise the setter throws "Could not find a component property".
- Figma refuses to publish when a non-variant property has no layer that references it, or when a property name equals a variant axis name.
- Variants that reference one instance swap property share its default. When the icon must differ per variant (Alert), do not share the property.
- Set the icon of a nested, exposed Icon button through its `Icon` swap property with `setProperties`. `swapComponent` on the inner instance is reset by the property value.
- Changing a variant with `setProperties` can reset text overrides on the instance. Set the text properties again afterwards.
- Never read `componentPropertyDefinitions` on a variant. Read it on the set.
- New instances in a plain frame inherit the main component's constraints. Set `constraints = {horizontal: 'MIN', vertical: 'MIN'}` before you resize the parent.

## Layout and sizing

- `resize()` sets the sizing modes to fixed. Set `layoutSizingHorizontal` or `layoutSizingVertical` to `'HUG'` or `'FILL'` after the resize.
- `HUG` works only on an auto layout frame or a text child of one. `FILL` works only on a child of an auto layout frame. Append the node first.
- An auto layout frame can report a stale size. Set `layoutMode = 'NONE'`, then back to its direction, to force a new measurement.
- A detached copy is a frame, not a component. Compose examples from instances in a plain frame instead of detaching.

## Shapes and icons

- `vectorPaths` accept only the commands M, L, C, Q and Z. Draw arcs as cubic Béziers of at most 90° each, with k = 4/3 · tan(θ/4). Figma moves the node to the bounding box of the path.
- To recolor an MDI icon instance, set the fills of its `VECTOR` named `icon`. An Icon button also has a `FRAME` named `icon`; give that frame `fills = []`, or it shows as a black square.
- Frames that hold menus, dialogs or picker lists in Examples need `clipsContent = false`, or their shadows are cut off.

## Images

- `upload_assets` with `nodeIds` sets an image as the fill of an existing node, but refuses nested instance IDs (`I…;…`). Upload without a target, read the `imageHash` from the response, set the fill in `use_figma`, and remove the frames the upload placed.
- Brand icons come from `https://brands.home-assistant.io/<domain>/icon.png` (256px). Use `scaleMode: 'FIT'`.
