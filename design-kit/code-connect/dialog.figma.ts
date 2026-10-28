// url=FIGMA_KIT_URL?node-id=98-168
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dialog.ts
// component=ha-dialog
import figma from 'figma'
const instance = figma.selectedInstance
const title = instance.getString('Title')
const subtitle = instance.getBoolean('Subtitle') ? instance.getString('Subtitle text') : ''
const body = instance.getString('Body')
const headerAction = instance.getBoolean('Header action')
const type = instance.getEnum('Type', { Standard: 'standard', Alert: 'alert' })
const width = instance.getEnum('Width', { Small: 'small', Medium: 'medium', Large: 'large', 'Full screen': 'full' })

export default {
  example: figma.html`<ha-dialog open type="${type}" width="${width}" header-title="${title}"${subtitle ? figma.html` header-subtitle="${subtitle}"` : ''} @closed=${'${this._closed}'}>
  ${headerAction ? figma.html`<ha-icon-button slot="headerActionItems" label="Help" .path=${'${mdiHelpCircle}'}></ha-icon-button>
  ` : ''}<p>${body}</p>
  <ha-button slot="footer" appearance="plain" @click=${'${this._cancel}'}>Cancel</ha-button>
  <ha-button slot="footer" @click=${'${this._save}'}>Save</ha-button>
</ha-dialog>`,
  id: 'ha-dialog',
  metadata: { nestable: true },
}
