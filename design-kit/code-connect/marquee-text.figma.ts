// url=FIGMA_KIT_URL?node-id=96-8
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-marquee-text.ts
// component=ha-marquee-text
import figma from 'figma'
const instance = figma.selectedInstance
const text = instance.getString('Text')
const pause = instance.getEnum('State', { Fits: '', Scrolling: '', Paused: ' pause-on-hover' })

export default {
  example: figma.html`<ha-marquee-text speed="15" pause-duration="1000"${pause}>${text}</ha-marquee-text>`,
  id: 'ha-marquee-text',
  metadata: { nestable: true },
}
