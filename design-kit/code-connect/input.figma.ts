// url=FIGMA_KIT_URL?node-id=66-166
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/input/ha-input.ts
// component=ha-input
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const value = instance.getString('Value')
const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''
const withClear = instance.getBoolean('Clear button')
const endText = instance.getBoolean('End text') ? instance.getString('End') : ''
const appearance = instance.getEnum('Appearance', { Material: 'material', Outlined: 'outlined', 'Outlined compact': 'outlined' })
const hasValue = instance.getEnum('State', { Empty: false, Hover: false, Focus: false, Filled: true, Invalid: true, Disabled: false })
const stateAttr = instance.getEnum('State', {"Empty": "", "Hover": "", "Focus": "", "Filled": "", "Invalid": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-input label="${label}"${hasValue ? figma.html` value="${value}"` : ''}${hint ? figma.html` hint="${hint}"` : ''} appearance="${appearance}"${withClear ? ' with-clear' : ''}${stateAttr}>${endText ? figma.html`<span slot="end">${endText}</span>` : ''}</ha-input>`,
  id: 'ha-input',
  metadata: { nestable: true },
}
