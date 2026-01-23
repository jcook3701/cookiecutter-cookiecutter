{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{{- license_macros.license_header.create(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='pre_gen_project.py',
	comment_style='hash') }}

import json
import os


def main() -> None:
    """Cookiecutter Pre Generation Scripts"""
    # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return
    {%- raw %}
    context = json.loads("""{{ cookiecutter | jsonify }}""")
    {% endraw %}
    print(f"Context: {context}")


if __name__ == "__main__":
    main()
