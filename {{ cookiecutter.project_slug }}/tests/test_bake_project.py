{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{{- license_macros.license_header(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='test_bake_project.py',
	comment_style='hash') }}

from pytest_cookies.plugin import Cookies


def test_bake_with_defaults(cookies: Cookies) -> None:
    """Ensure the template bakes correctly with default context."""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()

    # Optional sanity checks
    project_name = result.project_path.name
    assert project_name  # non-empty
    readme_file = result.project_path / "LICENSE"
    assert readme_file.exists()


def test_bake_with_custom_name(cookies: Cookies) -> None:
    """Ensure custom project_name works."""
    result = cookies.bake(extra_context={"project_name": "test_project"})
    print(result)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == "test_project"
