// url=FIGMA_KIT_URL?node-id=99-112
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-adaptive-dialog.ts
// component=ha-adaptive-dialog
import figma from 'figma'
const instance = figma.selectedInstance
const title = instance.getString('Title')
const subtitle = instance.getBoolean('Subtitle') ? instance.getString('Subtitle text') : ''
const body = instance.getString('Body')
const headerAction = instance.getBoolean('Header action')
const mode = instance.getEnum('Mode', { Dialog: 'dialog', 'Bottom sheet': 'bottom-sheet' })
const guarded = instance.getEnum('Guarded', { No: '', Yes: ' prevent-scrim-close' })

export default {
  example: figma.html`<ha-adaptive-dialog open${guarded} header-title="${title}"${subtitle ? figma.html` header-subtitle="${subtitle}"` : ''} @closed=${'${this._closed}'}>
  ${headerAction ? figma.html`<ha-icon-button slot="headerActionItems" label="Help" .path=${'${mdiHelpCircle}'}></ha-icon-button>
  ` : ''}<p>${body}</p>
  <ha-button slot="footer" appearance="plain" @click=${'${this._cancel}'}>Cancel</ha-button>
  <ha-button slot="footer" @click=${'${this._save}'}>Save</ha-button>
</ha-adaptive-dialog>`,
  id: 'ha-adaptive-dialog',
  metadata: { nestable: true },
}
