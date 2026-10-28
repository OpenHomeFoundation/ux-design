// url=FIGMA_KIT_URL?node-id=78-2
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-tip.ts
// component=ha-tip
import figma from 'figma'
const instance = figma.selectedInstance
const text = instance.getString('Text')

export default {
  example: figma.html`<ha-tip .hass=${'${this.hass}'}>${text}</ha-tip>`,
  id: 'ha-tip',
  metadata: { nestable: true },
}
