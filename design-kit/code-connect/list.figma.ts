// url=FIGMA_KIT_URL?node-id=90-144
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-list.ts
// component=ha-list
import figma from 'figma'
const instance = figma.selectedInstance

export default {
  example: figma.html`<ha-list>
  <ha-list-item>Network</ha-list-item>
  <ha-list-item>Storage</ha-list-item>
</ha-list>`,
  id: 'ha-list',
  metadata: { nestable: true },
}
