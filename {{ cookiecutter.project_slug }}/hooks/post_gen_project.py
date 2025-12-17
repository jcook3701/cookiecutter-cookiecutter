{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{{- license_macros.license_header(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='post_gen_project.py',
	comment_style='hash') }}

import json
import os

from nutrimatic.core import make
from nutrimatic.hooks.post_gen_logic import (
    generate_docs_templates,
)


def main() -> None:
    """Cookiecutter Post Generation Scripts"""
    # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return

    # Access cookiecutter context safely
    context = json.loads("""{{ cookiecutter | jsonify }}""")

    generate_docs_templates(context)

    # Run make commands to get project seeded
    make_cmds = [
        "install",
        "git-init",
        "pre-commit-init",
        "changelog",
        # "build-docs",
    ]

    for cmd in make_cmds:
        make(cmd)


if __name__ == "__main__":
    main()
