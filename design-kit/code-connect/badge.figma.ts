// url=FIGMA_KIT_URL?node-id=53-73
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-badge.ts
// component=ha-badge
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''
const content = instance.getString('Content')
const type = instance.getEnum('Type', { Static: '', Button: ' type="button"' })
const layout = instance.getEnum('Layout', { 'Icon and text': 'both', 'Text only': 'text', 'Icon only': 'icon' })

export default {
  example: figma.html`<ha-badge${type}${label ? figma.html` label="${label}"` : ''}${layout === 'icon' ? ' icon-only' : ''}>${layout !== 'text' ? figma.html`<ha-svg-icon slot="icon" .path=${'${mdiIcon}'}></ha-svg-icon>` : ''}${layout !== 'icon' ? content : ''}</ha-badge>`,
  id: 'ha-badge',
  metadata: { nestable: true },
}
