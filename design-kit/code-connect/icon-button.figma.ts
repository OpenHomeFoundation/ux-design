// url=FIGMA_KIT_URL?node-id=62-70
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-icon-button.ts
// component=ha-icon-button
import figma from 'figma'
const instance = figma.selectedInstance
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Selected": " selected", "Focus": "", "Disabled": " disabled"})
const size = instance.getEnum('Size', { '48': '48px', '36': '36px', '32': '32px', '24': '24px' })

export default {
  example: figma.html`<ha-icon-button label="Menu" .path=${'${mdiDotsVertical}'}${stateAttr} style="--mdc-icon-button-size: ${size}"></ha-icon-button>`,
  id: 'ha-icon-button',
  metadata: { nestable: true },
}
