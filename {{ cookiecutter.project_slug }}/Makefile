{% import '.cookiecutter_includes/license_header.j2' as license_macros with context %}
{% import '.cookiecutter_includes/make/__init__.j2' as make_macros with context %}

{{- license_macros.license_header(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='Makefile',
	comment_style='hash') -}}

{%- set sphinx = cookiecutter.add_sphinx_docs -%}
{%- set github = cookiecutter.add_github_docs -%}

{# Environment Settings Section #}
{{ make_macros.environment.settings()}}


{# Settings Section #}
{{ make_macros.settings.settings(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}

{# Python Command Settings #}
{{ make_macros.python.settings(

)}}

{# Documentation Command Settings #}
{{ make_macros.docs.doc_commands_section(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}

{# Changelog Settings #}
{{ make_macros.changelog.settings(

)}}

{# Git Settings #}
{{ make_macros.git.settings(

)}}
# --------------------------------------------------
# Functions
# --------------------------------------------------
{%- raw %}
# Finds files of a given extension or "*" (all files) under a directory,
# skipping VENV_DIR and template markers like {{ }}.
define get_files_by_extension
	find $(1) -name "$(2)" \
		! -path "$(VENV_DIR)/*" \
		! -path "$(RENDERED_VENV_DIR)/*" \
		! -path "*{{*" \
		! -path "*}}*" \
		! -name "__init__.j2" \
		-print0
endef
{% endraw %}

JINJA_FILE_LIST := ( \
		$(call get_files_by_extension,$(PROJECT_ROOT),*.j2); \
		$(call get_files_by_extension,$(RENDERED_COOKIE_DIR),*.j2) \
	)
TOML_FILE_LIST := 	( \
		$(call get_files_by_extension,$(PROJECT_ROOT),*.toml); \
		$(call get_files_by_extension,$(RENDERED_COOKIE_DIR),*.toml) \
	)
# --------------------------------------------------
{# .PHONY Section #}
{{ make_macros.phony.phony(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
# --------------------------------------------------
# Default: run lint, typecheck, spellcheck, tests, & docs
# --------------------------------------------------
all: install lint-check typecheck spellcheck test build-docs
# --------------------------------------------------
# Make Internal Utilities
# --------------------------------------------------
list-folders:
	$(AT)printf "\
	🐍 src: $(SRC_DIR)\n\
	🧪 Test: $(TESTS_DIR)\n"
{# Dependency Checks #}
# --------------------------------------------------
# Dependency Checks
# --------------------------------------------------
git-dependency-check:
	$(AT)which $(GIT) >/dev/null || \
		{ echo "Git is required: sudo apt install git"; exit 1; }

gh-dependency-check:
	$(AT)which $(GITHUB) >/dev/null || \
		{ echo "GitHub is required: sudo apt install gh"; exit 1; }

{# Python Action Section #}
{{ make_macros.python.python_actions(

)}}
{# Documentation Action Section #}
{{ make_macros.docs.doc_actions(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
{# Git Action Section #}
{{ make_macros.git.git_actions(

)}}
{# Release Action Section #}

{# Clean Action Section #}
{{ make_macros.clean.clean(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
{# Version Action Section #}
{{ make_macros.version.version() }}
{# Help Action Section #}
{{ make_macros.help.help(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
