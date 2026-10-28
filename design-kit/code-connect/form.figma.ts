// url=FIGMA_KIT_URL?node-id=106-231
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/ha-form/ha-form.ts
// component=ha-form
import figma from 'figma'
const instance = figma.selectedInstance
const grid = instance.getBoolean('Grid')
const expandable = instance.getBoolean('Expandable section')
const errors = instance.getEnum('State', { Default: '', 'With errors': ' .error=${this._errors}', Disabled: '' })
const stateAttr = instance.getEnum('State', {"Default": "", "With errors": "", "Disabled": " disabled"})

export default {
  example: figma.html`<ha-form
  .hass=${'${this.hass}'}
  .data=${'${this._data}'}
  .schema=${'${['}${grid ? '{ type: "grid", schema: [...] }, ' : ''}${expandable ? '{ type: "expandable", title: "Advanced", schema: [...] }, ' : ''}${'...]}'}
  .computeLabel=${'${this._computeLabel}'}${errors}${stateAttr}
  @value-changed=${'${this._valueChanged}'}
></ha-form>`,
  id: 'ha-form',
  metadata: { nestable: true },
}
