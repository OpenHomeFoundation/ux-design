// url=FIGMA_KIT_URL?node-id=59-2
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-tooltip.ts
// component=ha-tooltip
import figma from 'figma'
const instance = figma.selectedInstance
const text = instance.getString('Text')

export default {
  example: figma.html`<ha-tooltip for="sensor-value" placement="top">${text}</ha-tooltip>`,
  id: 'ha-tooltip',
  metadata: { nestable: true },
}
