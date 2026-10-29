// url=FIGMA_KIT_URL?node-id=183-371
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-control-circular-slider.ts
// component=ha-control-circular-slider
import figma from 'figma'
const instance = figma.selectedInstance
const mode = instance.getEnum('Mode', { Start: ' mode="start"', End: ' mode="end"', Full: ' mode="full"', Dual: ' dual' })
const values = instance.getEnum('Mode', { Start: ' value="21"', End: ' value="21"', Full: ' value="21"', Dual: ' low="19" high="24"' })
const stateAttr = instance.getEnum('State', {"Default": "", "Inactive": " inactive", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-control-circular-slider label="Target temperature"${mode}${values} current="20.5" min="7" max="35" step="0.5"${stateAttr} @value-changed=${'${this._valueChanged}'}></ha-control-circular-slider>`,
  id: 'ha-control-circular-slider',
  metadata: { nestable: true },
}
