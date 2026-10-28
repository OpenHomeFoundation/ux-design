// url=FIGMA_KIT_URL?node-id=86-59
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-switch.ts
// component=ha-control-switch
import figma from 'figma'
const instance = figma.selectedInstance
const checked = instance.getEnum('Checked', { Off: '', On: ' checked' })
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-switch label="Power" .pathOn=${'${mdiPower}'} .pathOff=${'${mdiPowerOff}'}${checked}${stateAttr} @change=${'${this._valueChanged}'}></ha-control-switch>`,
  id: 'ha-control-switch',
  metadata: { nestable: true },
}
