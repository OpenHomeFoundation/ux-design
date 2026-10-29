// url=FIGMA_KIT_URL?node-id=86-172
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-select.ts
// component=ha-control-select
import figma from 'figma'
const instance = figma.selectedInstance
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-select label="Fan speed" .options=${'${options}'} .value=${'${this._value}'}${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-control-select>`,
  id: 'ha-control-select',
  metadata: { nestable: true },
}
