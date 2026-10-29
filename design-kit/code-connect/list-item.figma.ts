// url=FIGMA_KIT_URL?node-id=90-125
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-list-item.ts
// component=ha-list-item
import figma from 'figma'
const instance = figma.selectedInstance
const primary = instance.getString('Primary text')
const secondary = instance.getEnum('Lines', { 'One line': '', 'Two lines': instance.getString('Secondary text') })
const graphic = instance.getEnum('Graphic', { None: '', Icon: ' graphic="icon"', Avatar: ' graphic="avatar"' })
const meta = instance.getBoolean('Meta')
const stateAttr = instance.getEnum('State', {"Default": "", "Activated": " activated", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-list-item${secondary ? ' twoline' : ''}${graphic}${meta ? ' hasMeta' : ''}${stateAttr}>${graphic ? figma.html`<ha-svg-icon slot="graphic" .path=${'${mdiWifi}'}></ha-svg-icon>` : ''}${primary}${secondary ? figma.html`<span slot="secondary">${secondary}</span>` : ''}${meta ? figma.html`<ha-svg-icon slot="meta" .path=${'${mdiChevronRight}'}></ha-svg-icon>` : ''}</ha-list-item>`,
  id: 'ha-list-item',
  metadata: { nestable: true },
}
