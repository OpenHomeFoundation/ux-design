// url=FIGMA_KIT_URL?node-id=51-2
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-state-icon.ts
// component=ha-state-icon
import figma from 'figma'
const instance = figma.selectedInstance

export default {
  example: figma.html`<ha-state-icon .hass=${'${this.hass}'} .stateObj=${'${stateObj}'}></ha-state-icon>`,
  id: 'ha-state-icon',
  metadata: { nestable: true },
}
