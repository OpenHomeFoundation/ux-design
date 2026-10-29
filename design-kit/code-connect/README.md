# Code Connect templates

One parserless template (`*.figma.ts`) per component set or component in the kit, with the label "Web Components". Publishing is deferred: Dev Mode snippets only help people who work on the team library, and every component description already links to its source file.

The Figma MCP cannot write Code Connect on the Professional plan, so the templates are published with the Code Connect CLI.

## Publish

The templates use `FIGMA_KIT_URL` in place of the link of the team library file, so the link stays out of this repo.

1. Create a Figma personal access token with the scopes Code Connect: Write and File content: Read.
2. Put the file link in a local copy of the templates:

```sh
cp -r design-kit/code-connect /tmp/code-connect
cd /tmp/code-connect
sed -i 's#FIGMA_KIT_URL#<link of the team library file, without query string>#' *.figma.ts
```

3. Publish from that copy:

```sh
npx --package=@figma/code-connect@2.1.0 figma connect publish --token=<token>
```

`--dry-run` validates without publishing. `figma connect parse --dir .` prints the parsed templates.

## Update

`scripts/gen_code_connect.py` generates these files from the component properties in the kit and the public properties of each source file. When a component set gains or renames a property, update the generator, run it, and publish again. Remove a template whose node no longer exists with `figma connect unpublish --node=<url> --label="Web Components"`.
