{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
	cookiecutter.license,
	cookiecutter.copyright,
	cookiecutter.project_slug,
	file_name='post_gen_project.py',
	comment_style='hash') }}
{%- set template_type = cookiecutter.template_type %}
{%- set doc_templates = ["sphinx-cookiecutter", "github-docs-cookiecutter"] %}

import json
import os

from nutrimatic.core import make
from nutrimatic.hooks.post_gen_logic import (
    {% if template_type ==  "ansible" %}
    generate_ansible_dirs,
    {% elif template_type != "documentation" %}
    generate_cliff_changelog_dirs,
    {% endif %}
    generate_docs_templates,
    get_make_cmds,
)


def main() -> None:
    """Cookiecutter Post Generation Scripts"""
    # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return
    {%- raw %}
    os.environ["COOKIECUTTER_HOOKS"] = "true"

    # Access cookiecutter context safely
    context = json.loads("""{{ cookiecutter | jsonify }}""")
    {% endraw %}
    generate_docs_templates(context)
    {% if template_type ==  "ansible" %}
    generate_ansible_dirs()
    {% elif sub_template == False  %}
    generate_cliff_changelog_dirs()
    {% endif %}

    # Run make commands to get project seeded
    make_cmds: list[str] = get_make_cmds(context)

    for cmd in make_cmds:
        make(cmd)


if __name__ == "__main__":
    main()
