// url=FIGMA_KIT_URL?node-id=64-55
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/buttons/ha-progress-button.ts
// component=ha-progress-button
import figma from 'figma'
const instance = figma.selectedInstance
const stateAttr = instance.getEnum('State', {"Resting": "", "Progress": " progress", "Success": "", "Error": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-progress-button${stateAttr} @click=${'${this._save}'}>Save</ha-progress-button>`,
  id: 'ha-progress-button',
  metadata: { nestable: true },
}
