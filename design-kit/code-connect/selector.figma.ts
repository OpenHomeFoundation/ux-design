// url=FIGMA_KIT_URL?node-id=108-184
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-selector/ha-selector.ts
// component=ha-selector
import figma from 'figma'
const instance = figma.selectedInstance
const selector = instance.getEnum('Type', { Text: '{ text: {} }', Number: '{ number: { min: 0, max: 100 } }', Boolean: '{ boolean: {} }', 'Select (list)': '{ select: { mode: "list", options } }', 'Select (dropdown)': '{ select: { mode: "dropdown", options } }', 'Select (box)': '{ select: { mode: "box", options } }', Entity: '{ entity: {} }', Device: '{ device: {} }', Area: '{ area: {} }' })

export default {
  example: figma.html`<ha-selector .hass=${'${this.hass}'} .selector=${'${'}${selector}${'}'} label="Label" .value=${'${this._value}'} @value-changed=${'${this._valueChanged}'}></ha-selector>`,
  id: 'ha-selector',
  metadata: { nestable: true },
}
