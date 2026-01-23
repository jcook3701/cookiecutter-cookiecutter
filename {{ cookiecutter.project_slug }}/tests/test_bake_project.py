{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{% import '.cookiecutter_includes/tests/bake.j2' as tests_macros with context %}
{{- license_macros.license_header.create(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='test_bake_project.py',
	comment_style='hash') }}

from pytest_cookies.plugin import Cookies


{{ tests_macros.default_bake(
    cookiecutter.template_type) }}


{{ tests_macros.custom_bake(
    cookiecutter.template_type) }}
