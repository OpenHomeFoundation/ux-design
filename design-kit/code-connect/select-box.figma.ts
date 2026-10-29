// url=FIGMA_KIT_URL?node-id=70-69
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-select-box.ts
// component=ha-select-box
import figma from 'figma'
const instance = figma.selectedInstance

export default {
  example: figma.html`<ha-select-box .options=${'${options}'} .value=${'${this._value}'} @value-changed=${'${this._valueChanged}'}></ha-select-box>`,
  id: 'ha-select-box',
  metadata: { nestable: true },
}
