// url=FIGMA_KIT_URL?node-id=58-18
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-spinner.ts
// component=ha-spinner
import figma from 'figma'
const instance = figma.selectedInstance
const size = instance.getEnum('Size', { Tiny: 'tiny', Small: 'small', Medium: 'medium', Large: 'large' })

export default {
  example: figma.html`<ha-spinner size="${size}"></ha-spinner>`,
  id: 'ha-spinner',
  metadata: { nestable: true },
}
