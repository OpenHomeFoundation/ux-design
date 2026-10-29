// url=FIGMA_KIT_URL?node-id=86-18
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-button.ts
// component=ha-control-button
import figma from 'figma'
const instance = figma.selectedInstance
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-button label="Power"${stateAttr}><ha-svg-icon .path=${'${mdiPower}'}></ha-svg-icon></ha-control-button>`,
  id: 'ha-control-button',
  metadata: { nestable: true },
}
