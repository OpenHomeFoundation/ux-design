// url=FIGMA_KIT_URL?node-id=105-140
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-area-picker.ts
// component=ha-area-picker
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const value = instance.getString('Value')
const helper = instance.getBoolean('Helper') ? instance.getString('Helper text') : ''
const hasValue = instance.getEnum('State', {"Empty": false, "Hover": false, "Focus": false, "Filled": true, "Unknown": true, "Invalid": true, "Disabled": false, "Add button": false})
const stateAttr = instance.getEnum('State', {"Empty": "", "Hover": "", "Focus": "", "Filled": "", "Unknown": "", "Invalid": "", "Disabled": " disabled", "Add button": ""})

export default {
  example: figma.html`<ha-area-picker .hass=${'${this.hass}'} label="${label}"${hasValue ? figma.html` value="${value}"` : ''}${helper ? figma.html` helper="${helper}"` : ''}${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-area-picker>`,
  id: 'ha-area-picker',
  metadata: { nestable: true },
}
