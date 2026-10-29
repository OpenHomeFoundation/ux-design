// url=FIGMA_KIT_URL?node-id=91-186
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-expansion-panel.ts
// component=ha-expansion-panel
import figma from 'figma'
const instance = figma.selectedInstance
const header = instance.getString('Title')
const secondary = instance.getBoolean('Show secondary') ? instance.getString('Secondary') : ''
const leadingIcon = instance.getBoolean('Leading icon')
const outlined = instance.getEnum('Outlined', { No: '', Yes: ' outlined' })
const chevron = instance.getEnum('Chevron', { End: '', Start: ' left-chevron' })
const open = instance.getEnum('Open', { Closed: '', Open: ' expanded' })

export default {
  example: figma.html`<ha-expansion-panel header="${header}"${secondary ? figma.html` secondary="${secondary}"` : ''}${outlined}${chevron}${open}>${leadingIcon ? figma.html`<ha-svg-icon slot="leading-icon" .path=${'${mdiCog}'}></ha-svg-icon>` : ''}
  <div class="content">…</div>
</ha-expansion-panel>`,
  id: 'ha-expansion-panel',
  metadata: { nestable: true },
}
