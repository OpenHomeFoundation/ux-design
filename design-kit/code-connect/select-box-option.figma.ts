// url=FIGMA_KIT_URL?node-id=70-68
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-select-box.ts
// component=ha-select-box
import figma from 'figma'
const instance = figma.selectedInstance
const label = instance.getString('Label')
const description = instance.getBoolean('Show description') ? instance.getString('Description') : ''
const image = instance.getBoolean('Show image')
const stateAttr = instance.getEnum('State', {"Resting": "", "Hover": "", "Selected": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-select-box
  .options=${'${[{ value: "metric", label: "'}${label}${'"'}${description ? figma.html`, description: "${description}"` : ''}${image ? ', image: "/static/images/metric.png"' : ''}${' }]}'}
  .value=${'${this._value}'}${stateAttr}
></ha-select-box>`,
  id: 'ha-select-box-option',
  metadata: { nestable: true },
}
