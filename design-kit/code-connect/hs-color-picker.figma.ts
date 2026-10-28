// url=FIGMA_KIT_URL?node-id=71-14
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-hs-color-picker.ts
// component=ha-hs-color-picker
import figma from 'figma'
const instance = figma.selectedInstance
const value = instance.getEnum('State', { 'With marker': true, 'No marker': false, Dragging: true, 'Half brightness': true })
const half = instance.getEnum('State', { 'With marker': false, 'No marker': false, Dragging: false, 'Half brightness': true })

export default {
  example: figma.html`<ha-hs-color-picker${value ? ' .value=${[200, 80]}' : ''}${half ? ' .colorBrightness=${128}' : ''} @value-changed=${'${this._hsColorChanged}'}></ha-hs-color-picker>`,
  id: 'ha-hs-color-picker',
  metadata: { nestable: true },
}
