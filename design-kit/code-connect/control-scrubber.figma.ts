// url=FIGMA_KIT_URL?node-id=87-29
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-scrubber.ts
// component=ha-control-scrubber
import figma from 'figma'
const instance = figma.selectedInstance
const stateAttr = instance.getEnum('State', {"Default": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-scrubber label="Position" min="0" max="100" step="1" value="40" unit="%"${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-control-scrubber>`,
  id: 'ha-control-scrubber',
  metadata: { nestable: true },
}
