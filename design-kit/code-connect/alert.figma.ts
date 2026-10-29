// url=FIGMA_KIT_URL?node-id=75-197
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-alert.ts
// component=ha-alert
import figma from 'figma'
const instance = figma.selectedInstance
const title = instance.getString('Title')
const message = instance.getString('Message')
const type = instance.getEnum('Type', { Error: 'error', Warning: 'warning', Info: 'info', Success: 'success' })
const layout = instance.getEnum('Layout', { Message: 'message', Title: 'title', Dismissable: 'dismissable', Action: 'action', Narrow: 'narrow' })

export default {
  example: figma.html`<ha-alert alert-type="${type}"${layout === 'title' ? figma.html` title="${title}"` : ''}${layout === 'dismissable' ? ' dismissable' : ''}${layout === 'narrow' ? ' narrow' : ''}>${message}${layout === 'action' ? figma.html`<ha-button slot="action" appearance="plain">Retry</ha-button>` : ''}</ha-alert>`,
  id: 'ha-alert',
  metadata: { nestable: true },
}
