// url=FIGMA_KIT_URL?node-id=68-34
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-switch.ts
// component=ha-switch
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''
const checked = instance.getEnum('Checked', { Off: '', On: ' checked' })
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-switch${checked}${stateAttr}>${label}</ha-switch>`,
  id: 'ha-switch',
  metadata: { nestable: true },
}
