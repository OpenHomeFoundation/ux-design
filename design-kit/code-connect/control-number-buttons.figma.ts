// url=FIGMA_KIT_URL?node-id=86-139
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-number-buttons.ts
// component=ha-control-number-buttons
import figma from 'figma'
const instance = figma.selectedInstance
const value = instance.getString('Value')
const stateAttr = instance.getEnum('State', {"Default": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-number-buttons label="Target temperature" value="21.5" step="0.5" min="7" max="35" unit="°C" .locale=${'${this.hass.locale}'}${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-control-number-buttons>`,
  id: 'ha-control-number-buttons',
  metadata: { nestable: true },
}
