#!/usr/bin/env python3
import yaml
from jinja2 import Template
from pathlib import Path

def render_conf(yaml_path, template_path, output_path, key):
    data = yaml.safe_load(Path(yaml_path).read_text())
    tpl = Template(Path(template_path).read_text())
    rendered = tpl.render(**data)
    Path(output_path).write_text(rendered)
    print(f"Generated {output_path}")

def main():
    Path("generated").mkdir(exist_ok=True)
    render_conf("src/indexes.yaml", "src/templates/indexes.j2", "generated/indexes.conf", "indexes")
    render_conf("src/inputs.yaml", "src/templates/inputs.j2", "generated/inputs.conf", "inputs")
    render_conf("src/authorize.yaml", "src/templates/authorize.j2", "generated/authorize.conf", "roles")
    render_conf("src/authentication.yaml", "src/templates/authentication.j2", "generated/authentication.conf", "authentication")

if __name__ == "__main__":
    main()
