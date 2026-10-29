// url=FIGMA_KIT_URL?node-id=89-62
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-select-menu.ts
// component=ha-control-select-menu
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const hideLabel = instance.getEnum('Layout', { 'Label and value': '', 'Tile feature': ' hide-label show-arrow' })
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Focus": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-select-menu label="${label}" .value=${'${this._value}'} .options=${'${options}'}${hideLabel}${stateAttr} @selected=${'${this._valueChanged}'}><ha-svg-icon slot="icon" .path=${'${mdiIcon}'}></ha-svg-icon></ha-control-select-menu>`,
  id: 'ha-control-select-menu',
  metadata: { nestable: true },
}
