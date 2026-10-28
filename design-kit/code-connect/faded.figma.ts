// url=FIGMA_KIT_URL?node-id=97-12
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-faded.ts
// component=ha-faded
import figma from 'figma'
const instance = figma.selectedInstance
const text = instance.getString('Text')

export default {
  example: figma.html`<ha-faded faded-height="102">
  <p>${text}</p>
</ha-faded>`,
  id: 'ha-faded',
  metadata: { nestable: true },
}
