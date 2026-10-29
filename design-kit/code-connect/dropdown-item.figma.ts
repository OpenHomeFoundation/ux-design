// url=FIGMA_KIT_URL?node-id=65-68
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dropdown-item.ts
// component=ha-dropdown-item
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const showIcon = instance.getBoolean('Show icon')
const typeAttr = instance.getEnum('Type', { Default: '', Danger: ' variant="danger"', Selected: ' selected', Checkbox: ' type="checkbox" checked', Submenu: '' })
const submenu = instance.getEnum('Type', { Default: false, Danger: false, Selected: false, Checkbox: false, Submenu: true })
const stateAttr = instance.getEnum('State', {"Resting": "", "Hover": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-dropdown-item value="edit"${typeAttr}${stateAttr}>${showIcon ? figma.html`<ha-svg-icon slot="icon" .path=${'${mdiIcon}'}></ha-svg-icon>` : ''}${label}${submenu ? figma.html`<ha-dropdown slot="submenu">…</ha-dropdown>` : ''}</ha-dropdown-item>`,
  id: 'ha-dropdown-item',
  metadata: { nestable: true },
}
