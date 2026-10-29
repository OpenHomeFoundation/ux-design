// url=FIGMA_KIT_URL?node-id=105-141
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-generic-picker.ts
// component=ha-generic-picker
import figma from 'figma'
const instance = figma.selectedInstance

export default {
  example: figma.html`<ha-generic-picker .hass=${'${this.hass}'} .getItems=${'${this._getItems}'} .rowRenderer=${'${this._rowRenderer}'} search-label="Search" @value-changed=${'${this._valueChanged}'}></ha-generic-picker>`,
  id: 'ha-generic-picker-area',
  metadata: { nestable: true },
}
