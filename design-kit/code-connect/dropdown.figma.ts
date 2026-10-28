// url=FIGMA_KIT_URL?node-id=65-69
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dropdown.ts
// component=ha-dropdown
import figma from 'figma'
const instance = figma.selectedInstance

export default {
  example: figma.html`<ha-dropdown @wa-select=${'${this._handleSelect}'}>
  <ha-icon-button slot="trigger" label="More" .path=${'${mdiDotsVertical}'}></ha-icon-button>
  <ha-dropdown-item value="edit">Edit</ha-dropdown-item>
  <ha-dropdown-item value="delete" variant="danger">Delete</ha-dropdown-item>
</ha-dropdown>`,
  id: 'ha-dropdown',
  metadata: { nestable: true },
}
