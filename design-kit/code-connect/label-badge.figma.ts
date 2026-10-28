// url=FIGMA_KIT_URL?node-id=57-2
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-label-badge.ts
// component=ha-label-badge
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''
const description = instance.getBoolean('Show description') ? instance.getString('Description') : ''
const value = instance.getString('Value')

export default {
  example: figma.html`<ha-label-badge${label ? figma.html` label="${label}"` : ''}${description ? figma.html` description="${description}"` : ''}>${value}</ha-label-badge>`,
  id: 'ha-label-badge',
  metadata: { nestable: true },
}
