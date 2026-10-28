"""Write one parserless Code Connect template per kit component.

Usage: python3 gen_code_connect.py <output folder>
The templates use FIGMA_KIT_URL as a placeholder for the file link; see code-connect/README.md.
"""
import json, os, re, sys
OUT = sys.argv[1]
FILE = 'FIGMA_KIT_URL'
GH = 'https://github.com/home-assistant/frontend/blob/dev/'
ICON = "<ha-svg-icon slot=\"%s\" .path=${'${mdiIcon}'}></ha-svg-icon>"

def disabled_enum(prop, opts, extra=None):
    m = {o: '' for o in opts}
    m['Disabled'] = ' disabled'
    if extra: m.update(extra)
    return "const stateAttr = instance.getEnum('%s', %s)" % (prop, json.dumps(m))

T = []
def add(file, node, tag, src, body, example, id=None):
    T.append(dict(file=file, node=node, tag=tag, src=src, body=body, example=example, id=id or tag))

# Buttons
for name, node in [('Brand','61:163'),('Neutral','61:360'),('Success','61:517'),('Warning','61:674'),('Danger','61:831')]:
    add('button-%s' % name.lower(), node, 'ha-button', 'src/components/ha-button.ts', [
        "const label = instance.getString('Label')",
        "const appearance = instance.getEnum('Appearance', { Accent: 'accent', Filled: 'filled', Outlined: 'outlined', Plain: 'plain' })",
        disabled_enum('State', ['Default','Hover','Pressed','Focus','Disabled','Loading'], {'Loading': ' loading'}),
        "const startIcon = instance.getBoolean('Start icon')",
        "const endIcon = instance.getBoolean('End icon')",
    ], '<ha-button variant="%s" appearance="${appearance}"${stateAttr}>${startIcon ? figma.html`%s` : \'\'}${label}${endIcon ? figma.html`%s` : \'\'}</ha-button>' % (name.lower(), ICON % 'start', ICON % 'end'), 'ha-button-%s' % name.lower())

add('icon-button', '62:70', 'ha-icon-button', 'src/components/ha-icon-button.ts', [
    disabled_enum('State', ['Default','Hover','Selected','Focus','Disabled'], {'Selected': ' selected'}),
    "const size = instance.getEnum('Size', { '48': '48px', '36': '36px', '32': '32px', '24': '24px' })",
], '<ha-icon-button label="Menu" .path=${\'${mdiDotsVertical}\'}${stateAttr} style="--mdc-icon-button-size: ${size}"></ha-icon-button>')

add('progress-button', '64:55', 'ha-progress-button', 'src/components/buttons/ha-progress-button.ts', [
    disabled_enum('State', ['Resting','Progress','Success','Error','Disabled'], {'Progress': ' progress'}),
], '<ha-progress-button${stateAttr} @click=${\'${this._save}\'}>Save</ha-progress-button>')

add('dropdown-item', '65:68', 'ha-dropdown-item', 'src/components/ha-dropdown-item.ts', [
    "const label = instance.getString('Label')",
    "const showIcon = instance.getBoolean('Show icon')",
    "const typeAttr = instance.getEnum('Type', { Default: '', Danger: ' variant=\"danger\"', Selected: ' selected', Checkbox: ' type=\"checkbox\" checked', Submenu: '' })",
    "const submenu = instance.getEnum('Type', { Default: false, Danger: false, Selected: false, Checkbox: false, Submenu: true })",
    disabled_enum('State', ['Resting','Hover','Disabled']),
], '<ha-dropdown-item value="edit"${typeAttr}${stateAttr}>${showIcon ? figma.html`%s` : \'\'}${label}${submenu ? figma.html`<ha-dropdown slot="submenu">…</ha-dropdown>` : \'\'}</ha-dropdown-item>' % (ICON % 'icon'))

add('dropdown', '65:69', 'ha-dropdown', 'src/components/ha-dropdown.ts', [],
    '<ha-dropdown @wa-select=${\'${this._handleSelect}\'}>\n  <ha-icon-button slot="trigger" label="More" .path=${\'${mdiDotsVertical}\'}></ha-icon-button>\n  <ha-dropdown-item value="edit">Edit</ha-dropdown-item>\n  <ha-dropdown-item value="delete" variant="danger">Delete</ha-dropdown-item>\n</ha-dropdown>')

add('input', '66:166', 'ha-input', 'src/components/input/ha-input.ts', [
    "const label = instance.getString('Label')",
    "const value = instance.getString('Value')",
    "const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''",
    "const withClear = instance.getBoolean('Clear button')",
    "const endText = instance.getBoolean('End text') ? instance.getString('End') : ''",
    "const appearance = instance.getEnum('Appearance', { Material: 'material', Outlined: 'outlined', 'Outlined compact': 'outlined' })",
    "const hasValue = instance.getEnum('State', { Empty: false, Hover: false, Focus: false, Filled: true, Invalid: true, Disabled: false })",
    disabled_enum('State', ['Empty','Hover','Focus','Filled','Invalid','Disabled']),
], '<ha-input label="${label}"${hasValue ? figma.html` value="${value}"` : \'\'}${hint ? figma.html` hint="${hint}"` : \'\'} appearance="${appearance}"${withClear ? \' with-clear\' : \'\'}${stateAttr}>${endText ? figma.html`<span slot="end">${endText}</span>` : \'\'}</ha-input>')

add('textarea', '67:50', 'ha-textarea', 'src/components/ha-textarea.ts', [
    "const label = instance.getString('Label')",
    "const text = instance.getString('Text')",
    "const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''",
    "const hasValue = instance.getEnum('State', { Empty: false, Hover: false, Focus: false, Filled: true, Invalid: true, Disabled: false })",
    disabled_enum('State', ['Empty','Hover','Focus','Filled','Invalid','Disabled']),
], '<ha-textarea label="${label}"${hasValue ? figma.html` value="${text}"` : \'\'}${hint ? figma.html` hint="${hint}"` : \'\'}${stateAttr}></ha-textarea>')

add('switch', '68:34', 'ha-switch', 'src/components/ha-switch.ts', [
    "const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''",
    "const checked = instance.getEnum('Checked', { Off: '', On: ' checked' })",
    disabled_enum('State', ['Default','Hover','Focus','Disabled']),
], '<ha-switch${checked}${stateAttr}>${label}</ha-switch>')

add('slider', '69:98', 'ha-slider', 'src/components/ha-slider.ts', [
    "const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''",
    "const hint = instance.getBoolean('Show hint') ? instance.getString('Hint') : ''",
    "const markers = instance.getBoolean('Markers')",
    "const size = instance.getEnum('Size', { Small: 's', Medium: 'm' })",
    disabled_enum('State', ['Default','Focus','Dragging','Disabled']),
], '<ha-slider size="${size}"${label ? figma.html` label="${label}"` : \'\'}${hint ? figma.html` hint="${hint}"` : \'\'} min="0" max="100" step="1" value="50"${markers ? \' with-markers\' : \'\'}${stateAttr}></ha-slider>')

add('select-box-option', '70:68', 'ha-select-box', 'src/components/ha-select-box.ts', [
    "const label = instance.getString('Label')",
    "const description = instance.getBoolean('Show description') ? instance.getString('Description') : ''",
    "const image = instance.getBoolean('Show image')",
    disabled_enum('State', ['Resting','Hover','Selected','Disabled']),
], '<ha-select-box\n  .options=${\'${[{ value: "metric", label: "\'}${label}${\'"\'}${description ? figma.html`, description: "${description}"` : \'\'}${image ? \', image: "/static/images/metric.png"\' : \'\'}${\' }]}\'}\n  .value=${\'${this._value}\'}${stateAttr}\n></ha-select-box>', 'ha-select-box-option')

add('select-box', '70:69', 'ha-select-box', 'src/components/ha-select-box.ts', [],
    '<ha-select-box .options=${\'${options}\'} .value=${\'${this._value}\'} @value-changed=${\'${this._valueChanged}\'}></ha-select-box>')

add('hs-color-picker', '71:14', 'ha-hs-color-picker', 'src/components/ha-hs-color-picker.ts', [
    "const value = instance.getEnum('State', { 'With marker': true, 'No marker': false, Dragging: true, 'Half brightness': true })",
    "const half = instance.getEnum('State', { 'With marker': false, 'No marker': false, Dragging: false, 'Half brightness': true })",
], '<ha-hs-color-picker${value ? \' .value=${[200, 80]}\' : \'\'}${half ? \' .colorBrightness=${128}\' : \'\'} @value-changed=${\'${this._hsColorChanged}\'}></ha-hs-color-picker>')

def picker(file, node, tag, src, states, add_button):
    body = [
        "const label = instance.getString('Label')",
        "const value = instance.getString('Value')",
        "const helper = instance.getBoolean('Helper') ? instance.getString('Helper text') : ''",
        "const hasValue = instance.getEnum('State', %s)" % json.dumps({s: s in ('Filled','Unknown','Invalid') for s in states}),
        disabled_enum('State', states, {'Add button': ' add-button'} if add_button else None),
    ]
    add(file, node, tag, src, body, '<%s .hass=${\'${this.hass}\'} label="${label}"${hasValue ? figma.html` value="${value}"` : \'\'}${helper ? figma.html` helper="${helper}"` : \'\'}${stateAttr} @value-changed=${\'${this._valueChanged}\'}></%s>' % (tag, tag))
picker('entity-picker', '102:156', 'ha-entity-picker', 'src/components/entity/ha-entity-picker.ts', ['Empty','Hover','Focus','Filled','Unknown','Invalid','Disabled','Add button'], True)
picker('device-picker', '104:122', 'ha-device-picker', 'src/components/device/ha-device-picker.ts', ['Empty','Hover','Focus','Filled','Unknown','Invalid','Disabled'], False)
picker('area-picker', '105:140', 'ha-area-picker', 'src/components/ha-area-picker.ts', ['Empty','Hover','Focus','Filled','Unknown','Invalid','Disabled','Add button'], False)
for file, node in [('entity-picker-list','102:157'),('device-picker-list','104:123'),('area-picker-list','105:141')]:
    add(file, node, 'ha-generic-picker', 'src/components/ha-generic-picker.ts', [],
        '<ha-generic-picker .hass=${\'${this.hass}\'} .getItems=${\'${this._getItems}\'} .rowRenderer=${\'${this._rowRenderer}\'} search-label="Search" @value-changed=${\'${this._valueChanged}\'}></ha-generic-picker>', 'ha-generic-picker-' + file.split('-')[0])

add('form', '106:231', 'ha-form', 'src/components/ha-form/ha-form.ts', [
    "const grid = instance.getBoolean('Grid')",
    "const expandable = instance.getBoolean('Expandable section')",
    "const errors = instance.getEnum('State', { Default: '', 'With errors': ' .error=${this._errors}', Disabled: '' })",
    disabled_enum('State', ['Default','With errors','Disabled']),
], '<ha-form\n  .hass=${\'${this.hass}\'}\n  .data=${\'${this._data}\'}\n  .schema=${\'${[\'}${grid ? \'{ type: "grid", schema: [...] }, \' : \'\'}${expandable ? \'{ type: "expandable", title: "Advanced", schema: [...] }, \' : \'\'}${\'...]}\'}\n  .computeLabel=${\'${this._computeLabel}\'}${errors}${stateAttr}\n  @value-changed=${\'${this._valueChanged}\'}\n></ha-form>')

add('selector', '108:184', 'ha-selector', 'src/components/ha-selector/ha-selector.ts', [
    "const selector = instance.getEnum('Type', { Text: '{ text: {} }', Number: '{ number: { min: 0, max: 100 } }', Boolean: '{ boolean: {} }', 'Select (list)': '{ select: { mode: \"list\", options } }', 'Select (dropdown)': '{ select: { mode: \"dropdown\", options } }', 'Select (box)': '{ select: { mode: \"box\", options } }', Entity: '{ entity: {} }', Device: '{ device: {} }', Area: '{ area: {} }' })",
], '<ha-selector .hass=${\'${this.hass}\'} .selector=${\'${\'}${selector}${\'}\'} label="Label" .value=${\'${this._value}\'} @value-changed=${\'${this._valueChanged}\'}></ha-selector>')

add('alert', '75:197', 'ha-alert', 'src/components/ha-alert.ts', [
    "const title = instance.getString('Title')",
    "const message = instance.getString('Message')",
    "const type = instance.getEnum('Type', { Error: 'error', Warning: 'warning', Info: 'info', Success: 'success' })",
    "const layout = instance.getEnum('Layout', { Message: 'message', Title: 'title', Dismissable: 'dismissable', Action: 'action', Narrow: 'narrow' })",
], '<ha-alert alert-type="${type}"${layout === \'title\' ? figma.html` title="${title}"` : \'\'}${layout === \'dismissable\' ? \' dismissable\' : \'\'}${layout === \'narrow\' ? \' narrow\' : \'\'}>${message}${layout === \'action\' ? figma.html`<ha-button slot="action" appearance="plain">Retry</ha-button>` : \'\'}</ha-alert>')

for file, node, tag, src, extra_body, extra_attr in [
    ('dialog','98:168','ha-dialog','src/components/ha-dialog.ts',
     ["const type = instance.getEnum('Type', { Standard: 'standard', Alert: 'alert' })",
      "const width = instance.getEnum('Width', { Small: 'small', Medium: 'medium', Large: 'large', 'Full screen': 'full' })"],
     ' type="${type}" width="${width}"'),
    ('adaptive-dialog','99:112','ha-adaptive-dialog','src/components/ha-adaptive-dialog.ts',
     ["const mode = instance.getEnum('Mode', { Dialog: 'dialog', 'Bottom sheet': 'bottom-sheet' })",
      "const guarded = instance.getEnum('Guarded', { No: '', Yes: ' prevent-scrim-close' })"],
     '${guarded}'),
]:
    add(file, node, tag, src, [
        "const title = instance.getString('Title')",
        "const subtitle = instance.getBoolean('Subtitle') ? instance.getString('Subtitle text') : ''",
        "const body = instance.getString('Body')",
        "const headerAction = instance.getBoolean('Header action')",
    ] + extra_body, '<%s open%s header-title="${title}"${subtitle ? figma.html` header-subtitle="${subtitle}"` : \'\'} @closed=${\'${this._closed}\'}>\n  ${headerAction ? figma.html`<ha-icon-button slot="headerActionItems" label="Help" .path=${\'${mdiHelpCircle}\'}></ha-icon-button>\n  ` : \'\'}<p>${body}</p>\n  <ha-button slot="footer" appearance="plain" @click=${\'${this._cancel}\'}>Cancel</ha-button>\n  <ha-button slot="footer" @click=${\'${this._save}\'}>Save</ha-button>\n</%s>' % (tag, extra_attr, tag))

add('badge', '53:73', 'ha-badge', 'src/components/ha-badge.ts', [
    "const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''",
    "const content = instance.getString('Content')",
    "const type = instance.getEnum('Type', { Static: '', Button: ' type=\"button\"' })",
    "const layout = instance.getEnum('Layout', { 'Icon and text': 'both', 'Text only': 'text', 'Icon only': 'icon' })",
], '<ha-badge${type}${label ? figma.html` label="${label}"` : \'\'}${layout === \'icon\' ? \' icon-only\' : \'\'}>${layout !== \'text\' ? figma.html`%s` : \'\'}${layout !== \'icon\' ? content : \'\'}</ha-badge>' % (ICON % 'icon'))

add('label-badge', '57:2', 'ha-label-badge', 'src/components/ha-label-badge.ts', [
    "const label = instance.getBoolean('Show label') ? instance.getString('Label') : ''",
    "const description = instance.getBoolean('Show description') ? instance.getString('Description') : ''",
    "const value = instance.getString('Value')",
], '<ha-label-badge${label ? figma.html` label="${label}"` : \'\'}${description ? figma.html` description="${description}"` : \'\'}>${value}</ha-label-badge>')

add('spinner', '58:18', 'ha-spinner', 'src/components/ha-spinner.ts', [
    "const size = instance.getEnum('Size', { Tiny: 'tiny', Small: 'small', Medium: 'medium', Large: 'large' })",
], '<ha-spinner size="${size}"></ha-spinner>')

add('tooltip', '59:2', 'ha-tooltip', 'src/components/ha-tooltip.ts', [
    "const text = instance.getString('Text')",
], '<ha-tooltip for="sensor-value" placement="top">${text}</ha-tooltip>')

add('tip', '78:2', 'ha-tip', 'src/components/ha-tip.ts', [
    "const text = instance.getString('Text')",
], '<ha-tip .hass=${\'${this.hass}\'}>${text}</ha-tip>')

add('state-icon', '51:2', 'ha-state-icon', 'src/components/ha-state-icon.ts', [],
    '<ha-state-icon .hass=${\'${this.hass}\'} .stateObj=${\'${stateObj}\'}></ha-state-icon>')

add('state-badge', '51:22', 'state-badge', 'src/components/entity/state-badge.ts', [
    "const color = instance.getEnum('Color', { Default: '', Active: ' stateColor', 'Light on': ' stateColor', Unavailable: '', Focus: '', Picture: '' })",
    "const picture = instance.getEnum('Color', { Default: false, Active: false, 'Light on': false, Unavailable: false, Focus: false, Picture: true })",
], '<state-badge .hass=${\'${this.hass}\'} .stateObj=${\'${stateObj}\'}${color}${picture ? \' .overrideImage=${entityPicture}\' : \'\'}></state-badge>')

add('gauge', '83:30', 'ha-gauge', 'src/components/ha-gauge.ts', [
    "const valueText = instance.getString('Value text')",
    "const mode = instance.getEnum('Mode', { Filled: 'filled', Success: 'success', Warning: 'warning', Error: 'error', Needle: 'needle' })",
], '<ha-gauge min="0" max="100" value="62" .valueText=${\'${\'}${\'"\'}${valueText}${\'"}\'} .locale=${\'${this.hass.locale}\'}${mode === \'needle\' ? \' needle .levels=${[{ level: 0, stroke: "var(--error-color)" }, { level: 40, stroke: "var(--warning-color)" }, { level: 70, stroke: "var(--success-color)" }]}\' : \'\'}${mode === \'success\' ? \' style="--gauge-color: var(--success-color)"\' : mode === \'warning\' ? \' style="--gauge-color: var(--warning-color)"\' : mode === \'error\' ? \' style="--gauge-color: var(--error-color)"\' : \'\'}></ha-gauge>')

add('bar', '82:10', 'ha-bar', 'src/components/ha-bar.ts', [
    "const color = instance.getEnum('Color', { Primary: '', Success: ' style=\"--ha-bar-primary-color: var(--success-color)\"', Warning: ' style=\"--ha-bar-primary-color: var(--warning-color)\"', Error: ' style=\"--ha-bar-primary-color: var(--error-color)\"' })",
], '<ha-bar min="0" max="100" value="62"${color}></ha-bar>')

add('control-button', '86:18', 'ha-control-button', 'src/components/ha-control-button.ts', [
    disabled_enum('State', ['Default','Hover','Focus','Disabled']),
], '<ha-control-button label="Power"${stateAttr}>%s</ha-control-button>' % "<ha-svg-icon .path=${'${mdiPower}'}></ha-svg-icon>")

add('control-switch', '86:59', 'ha-control-switch', 'src/components/ha-control-switch.ts', [
    "const checked = instance.getEnum('Checked', { Off: '', On: ' checked' })",
    disabled_enum('State', ['Default','Hover','Focus','Disabled']),
], '<ha-control-switch label="Power" .pathOn=${\'${mdiPower}\'} .pathOff=${\'${mdiPowerOff}\'}${checked}${stateAttr} @change=${\'${this._valueChanged}\'}></ha-control-switch>')

add('control-slider', '86:111', 'ha-control-slider', 'src/components/ha-control-slider.ts', [
    "const mode = instance.getEnum('Mode', { Start: 'start', End: 'end', Cursor: 'cursor' })",
    disabled_enum('State', ['Default','Dragging','Disabled']),
], '<ha-control-slider label="Brightness" mode="${mode}" min="0" max="100" step="1" value="60" unit="%"${stateAttr} @value-changed=${\'${this._valueChanged}\'}></ha-control-slider>')

add('control-number-buttons', '86:139', 'ha-control-number-buttons', 'src/components/ha-control-number-buttons.ts', [
    "const value = instance.getString('Value')",
    disabled_enum('State', ['Default','Focus','Disabled']),
], '<ha-control-number-buttons label="Target temperature" value="21.5" step="0.5" min="7" max="35" unit="°C" .locale=${\'${this.hass.locale}\'}${stateAttr} @value-changed=${\'${this._valueChanged}\'}></ha-control-number-buttons>')

add('control-select', '86:172', 'ha-control-select', 'src/components/ha-control-select.ts', [
    disabled_enum('State', ['Default','Hover','Focus','Disabled']),
], '<ha-control-select label="Fan speed" .options=${\'${options}\'} .value=${\'${this._value}\'}${stateAttr} @value-changed=${\'${this._valueChanged}\'}></ha-control-select>')

add('control-circular-slider', '183:371', 'ha-control-circular-slider', 'src/components/ha-control-circular-slider.ts', [
    "const mode = instance.getEnum('Mode', { Start: ' mode=\"start\"', End: ' mode=\"end\"', Full: ' mode=\"full\"', Dual: ' dual' })",
    "const values = instance.getEnum('Mode', { Start: ' value=\"21\"', End: ' value=\"21\"', Full: ' value=\"21\"', Dual: ' low=\"19\" high=\"24\"' })",
    disabled_enum('State', ['Default','Inactive','Disabled'], {'Inactive': ' inactive'}),
], '<ha-control-circular-slider label="Target temperature"${mode}${values} current="20.5" min="7" max="35" step="0.5"${stateAttr} @value-changed=${\'${this._valueChanged}\'}></ha-control-circular-slider>')

add('control-scrubber', '87:29', 'ha-control-scrubber', 'src/components/ha-control-scrubber.ts', [
    disabled_enum('State', ['Default','Focus','Disabled']),
], '<ha-control-scrubber label="Position" min="0" max="100" step="1" value="40" unit="%"${stateAttr} @value-changed=${\'${this._valueChanged}\'}></ha-control-scrubber>')

add('control-select-menu', '89:62', 'ha-control-select-menu', 'src/components/ha-control-select-menu.ts', [
    "const label = instance.getString('Label')",
    "const hideLabel = instance.getEnum('Layout', { 'Label and value': '', 'Tile feature': ' hide-label show-arrow' })",
    disabled_enum('State', ['Default','Hover','Focus','Disabled']),
], '<ha-control-select-menu label="${label}" .value=${\'${this._value}\'} .options=${\'${options}\'}${hideLabel}${stateAttr} @selected=${\'${this._valueChanged}\'}>%s</ha-control-select-menu>' % (ICON % 'icon'))

add('list-item', '90:125', 'ha-list-item', 'src/components/ha-list-item.ts', [
    "const primary = instance.getString('Primary text')",
    "const secondary = instance.getEnum('Lines', { 'One line': '', 'Two lines': instance.getString('Secondary text') })",
    "const graphic = instance.getEnum('Graphic', { None: '', Icon: ' graphic=\"icon\"', Avatar: ' graphic=\"avatar\"' })",
    "const meta = instance.getBoolean('Meta')",
    disabled_enum('State', ['Default','Activated','Disabled'], {'Activated': ' activated'}),
], '<ha-list-item${secondary ? \' twoline\' : \'\'}${graphic}${meta ? \' hasMeta\' : \'\'}${stateAttr}>${graphic ? figma.html`<ha-svg-icon slot="graphic" .path=${\'${mdiWifi}\'}></ha-svg-icon>` : \'\'}${primary}${secondary ? figma.html`<span slot="secondary">${secondary}</span>` : \'\'}${meta ? figma.html`<ha-svg-icon slot="meta" .path=${\'${mdiChevronRight}\'}></ha-svg-icon>` : \'\'}</ha-list-item>')

add('list', '90:144', 'ha-list', 'src/components/ha-list.ts', [],
    '<ha-list>\n  <ha-list-item>Network</ha-list-item>\n  <ha-list-item>Storage</ha-list-item>\n</ha-list>')

add('expansion-panel', '91:186', 'ha-expansion-panel', 'src/components/ha-expansion-panel.ts', [
    "const header = instance.getString('Title')",
    "const secondary = instance.getBoolean('Show secondary') ? instance.getString('Secondary') : ''",
    "const leadingIcon = instance.getBoolean('Leading icon')",
    "const outlined = instance.getEnum('Outlined', { No: '', Yes: ' outlined' })",
    "const chevron = instance.getEnum('Chevron', { End: '', Start: ' left-chevron' })",
    "const open = instance.getEnum('Open', { Closed: '', Open: ' expanded' })",
], '<ha-expansion-panel header="${header}"${secondary ? figma.html` secondary="${secondary}"` : \'\'}${outlined}${chevron}${open}>${leadingIcon ? figma.html`<ha-svg-icon slot="leading-icon" .path=${\'${mdiCog}\'}></ha-svg-icon>` : \'\'}\n  <div class="content">…</div>\n</ha-expansion-panel>')

add('marquee-text', '96:8', 'ha-marquee-text', 'src/components/ha-marquee-text.ts', [
    "const text = instance.getString('Text')",
    "const pause = instance.getEnum('State', { Fits: '', Scrolling: '', Paused: ' pause-on-hover' })",
], '<ha-marquee-text speed="15" pause-duration="1000"${pause}>${text}</ha-marquee-text>')

add('faded', '97:12', 'ha-faded', 'src/components/ha-faded.ts', [
    "const text = instance.getString('Text')",
], '<ha-faded faded-height="102">\n  <p>${text}</p>\n</ha-faded>')

os.makedirs(OUT, exist_ok=True)
for old in os.listdir(OUT):
    if old.endswith('.figma.ts'): os.remove(os.path.join(OUT, old))
names = set()
for t in T:
    assert t['id'] not in names, t['id']; names.add(t['id'])
    lines = ['// url=%s?node-id=%s' % (FILE, t['node'].replace(':', '-')), '// source=%s%s' % (GH, t['src']), '// component=%s' % t['tag'], "import figma from 'figma'", 'const instance = figma.selectedInstance'] + t['body'] + ['', 'export default {', '  example: figma.html`%s`,' % t['example'], "  id: '%s'," % t['id'], '  metadata: { nestable: true },', '}', '']
    open(os.path.join(OUT, t['file'] + '.figma.ts'), 'w').write('\n'.join(lines))
json.dump({'codeConnect': {'include': ['*.figma.ts'], 'label': 'Web Components', 'language': 'html'}}, open(os.path.join(OUT, 'figma.config.json'), 'w'), indent=2)
print(len(T), 'templates')
