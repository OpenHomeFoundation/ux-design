// url=FIGMA_KIT_URL?node-id=61-831
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-button.ts
// component=ha-button
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const appearance = instance.getEnum('Appearance', { Accent: 'accent', Filled: 'filled', Outlined: 'outlined', Plain: 'plain' })
const stateAttr = instance.getEnum('State', {"Default": "", "Hover": "", "Pressed": "", "Focus": "", "Disabled": " disabled", "Loading": " loading"})
const startIcon = instance.getBoolean('Start icon')
const endIcon = instance.getBoolean('End icon')

export default {
  example: figma.html`<ha-button variant="danger" appearance="${appearance}"${stateAttr}>${startIcon ? figma.html`<ha-svg-icon slot="start" .path=${'${mdiIcon}'}></ha-svg-icon>` : ''}${label}${endIcon ? figma.html`<ha-svg-icon slot="end" .path=${'${mdiIcon}'}></ha-svg-icon>` : ''}</ha-button>`,
  id: 'ha-button-danger',
  metadata: { nestable: true },
}
