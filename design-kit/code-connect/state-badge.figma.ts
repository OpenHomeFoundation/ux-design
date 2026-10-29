// url=FIGMA_KIT_URL?node-id=51-22
// source=https://github.com/home-assistant/frontend/blob/dev/src/components/entity/state-badge.ts
// component=state-badge
import figma from 'figma'
const instance = figma.selectedInstance
const color = instance.getEnum('Color', { Default: '', Active: ' stateColor', 'Light on': ' stateColor', Unavailable: '', Focus: '', Picture: '' })
const picture = instance.getEnum('Color', { Default: false, Active: false, 'Light on': false, Unavailable: false, Focus: false, Picture: true })

export default {
  example: figma.html`<state-badge .hass=${'${this.hass}'} .stateObj=${'${stateObj}'}${color}${picture ? ' .overrideImage=${entityPicture}' : ''}></state-badge>`,
  id: 'state-badge',
  metadata: { nestable: true },
}
