// url=FIGMA_KIT_URL?node-id=69-98
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-slider.ts
// component=ha-slider
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''
const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''
const markers = instance.getBoolean('Markers')
const size = instance.getEnum('Size', { Small: 's', Medium: 'm' })
const stateAttr = instance.getEnum('State', {"Default": "", "Focus": "", "Dragging": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-slider size="${size}"${label ? figma.html` label="${label}"` : ''}${hint ? figma.html` hint="${hint}"` : ''} min="0" max="100" step="1" value="50"${markers ? ' with-markers' : ''}${stateAttr}></ha-slider>`,
  id: 'ha-slider',
  metadata: { nestable: true },
}
