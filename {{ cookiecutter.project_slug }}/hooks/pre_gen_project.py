{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{{- license_macros.license_header(
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
    # json_file = "cookiecutter.json"

    # json_path = Path(__file__).absolute() / "cookiecutter.json"
    # project_dir = Path.cwd()
    # print(f"FileName: {json_path}")
    # print(f"JSON File: {json_file}")
    # Init Auto Variables
    # release_date(json_path)


if __name__ == "__main__":
    main()
