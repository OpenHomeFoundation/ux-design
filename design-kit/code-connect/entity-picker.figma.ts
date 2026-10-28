// url=FIGMA_KIT_URL?node-id=102-156
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/entity/ha-entity-picker.ts
// component=ha-entity-picker
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const value = instance.getString('Value')
const helper = instance.getBoolean('Helper') ? instance.getString('Helper text') : ''
const hasValue = instance.getEnum('State', {"Empty": false, "Hover": false, "Focus": false, "Filled": true, "Unknown": true, "Invalid": true, "Disabled": false, "Add button": false})
const stateAttr = instance.getEnum('State', {"Empty": "", "Hover": "", "Focus": "", "Filled": "", "Unknown": "", "Invalid": "", "Disabled": " disabled", "Add button": " add-button"})

export default {
  example: figma.html`<ha-entity-picker .hass=${'${this.hass}'} label="${label}"${hasValue ? figma.html` value="${value}"` : ''}${helper ? figma.html` helper="${helper}"` : ''}${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-entity-picker>`,
  id: 'ha-entity-picker',
  metadata: { nestable: true },
}
