// url=FIGMA_KIT_URL?node-id=82-10
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-bar.ts
// component=ha-bar
import figma from 'figma'
const instance = figma.selectedInstance
const color = instance.getEnum('Color', { Primary: '', Success: ' style="--ha-bar-primary-color: var(--success-color)"', Warning: ' style="--ha-bar-primary-color: var(--warning-color)"', Error: ' style="--ha-bar-primary-color: var(--error-color)"' })

export default {
  example: figma.html`<ha-bar min="0" max="100" value="62"${color}></ha-bar>`,
  id: 'ha-bar',
  metadata: { nestable: true },
}
