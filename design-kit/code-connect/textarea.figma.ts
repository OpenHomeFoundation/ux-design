// url=FIGMA_KIT_URL?node-id=67-50
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-textarea.ts
// component=ha-textarea
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const text = instance.getString('Text')
const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''
const hasValue = instance.getEnum('State', { Empty: false, Hover: false, Focus: false, Filled: true, Invalid: true, Disabled: false })
const stateAttr = instance.getEnum('State', {"Empty": "", "Hover": "", "Focus": "", "Filled": "", "Invalid": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-textarea label="${label}"${hasValue ? figma.html` value="${text}"` : ''}${hint ? figma.html` hint="${hint}"` : ''}${stateAttr}></ha-textarea>`,
  id: 'ha-textarea',
  metadata: { nestable: true },
}
