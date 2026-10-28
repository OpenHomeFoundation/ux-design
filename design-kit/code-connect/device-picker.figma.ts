// url=FIGMA_KIT_URL?node-id=104-122
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/device/ha-device-picker.ts
// component=ha-device-picker
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const value = instance.getString('Value')
const helper = instance.getBoolean('Helper') ? instance.getString('Helper text') : ''
const hasValue = instance.getEnum('State', {"Empty": false, "Hover": false, "Focus": false, "Filled": true, "Unknown": true, "Invalid": true, "Disabled": false})
const stateAttr = instance.getEnum('State', {"Empty": "", "Hover": "", "Focus": "", "Filled": "", "Unknown": "", "Invalid": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-device-picker .hass=${'${this.hass}'} label="${label}"${hasValue ? figma.html` value="${value}"` : ''}${helper ? figma.html` helper="${helper}"` : ''}${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-device-picker>`,
  id: 'ha-device-picker',
  metadata: { nestable: true },
}
