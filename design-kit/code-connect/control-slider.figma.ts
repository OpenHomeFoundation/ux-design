// url=FIGMA_KIT_URL?node-id=86-111
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-slider.ts
// component=ha-control-slider
import figma from 'figma'
const instance = figma.selectedInstance
const mode = instance.getEnum('Mode', { Start: 'start', End: 'end', Cursor: 'cursor' })
const stateAttr = instance.getEnum('State', {"Default": "", "Dragging": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-slider label="Brightness" mode="${mode}" min="0" max="100" step="1" value="60" unit="%"${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-control-slider>`,
  id: 'ha-control-slider',
  metadata: { nestable: true },
}
