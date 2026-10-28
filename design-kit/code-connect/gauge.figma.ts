// url=FIGMA_KIT_URL?node-id=83-30
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-gauge.ts
// component=ha-gauge
import figma from 'figma'
const instance = figma.selectedInstance
const valueText = instance.getString('Value text')
const mode = instance.getEnum('Mode', { Filled: 'filled', Success: 'success', Warning: 'warning', Error: 'error', Needle: 'needle' })

export default {
  example: figma.html`<ha-gauge min="0" max="100" value="62" .valueText=${'${'}${'"'}${valueText}${'"}'} .locale=${'${this.hass.locale}'}${mode === 'needle' ? ' needle .levels=${[{ level: 0, stroke: "var(--error-color)" }, { level: 40, stroke: "var(--warning-color)" }, { level: 70, stroke: "var(--success-color)" }]}' : ''}${mode === 'success' ? ' style="--gauge-color: var(--success-color)"' : mode === 'warning' ? ' style="--gauge-color: var(--warning-color)"' : mode === 'error' ? ' style="--gauge-color: var(--error-color)"' : ''}></ha-gauge>`,
  id: 'ha-gauge',
  metadata: { nestable: true },
}
