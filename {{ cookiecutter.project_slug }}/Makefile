{% import '.cookiecutter_includes/license/__init__.j2' as license_macros with context %}
{% import '.cookiecutter_includes/make/__init__.j2' as make_macros with context %}

{{- license_macros.license_header.create(
	cookiecutter.license,
	cookiecutter.author,
	cookiecutter.project_slug,
	file_name='Makefile',
	comment_style='hash') -}}

{%- set sphinx = cookiecutter.add_sphinx_docs -%}
{%- set github = cookiecutter.add_github_docs -%}

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c
# If V is set to '1' or 'y' on the command line,
# AT will be empty (verbose).  Otherwise, AT will
# contain '@' (quiet by default).  The '?' is a
# conditional assignment operator: it only sets V
# if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif
# Detect if we are running inside GitHub Actions CI.
# GitHub sets the environment variable GITHUB_ACTIONS=true in workflows.
# We set CI=1 if running in GitHub Actions, otherwise CI=0 for local runs.
ifeq ($(GITHUB_ACTIONS),true)
CI := 1
else
CI := 0
endif
# Detect if we are running inside Cookiecutter (pre/post) hooks.
# Cookiecutter hooks are used to set the environment variable COOKIECUTTER_HOOKS=true.
# We set CC=1 if running in Cookiecutter hooks, otherwise CC=0 for standard runs.
COOKIECUTTER_RENDER_DIR := /tmp/rendered
ifeq ($(COOKIECUTTER_HOOKS),true)
CC := 1
else
CC := 0
endif
# --------------------------------------------------
# 🏗️ CI/CD Functions
# --------------------------------------------------
# Returns true when CI is off and gracefully moves through failed checks.
define run_ci_safe =
( $1 || \
	if [ "$(CI)" != "1" ]; then \
		echo "❌ process finished with error; continuing..."; \
		true; \
	else \
		echo "❌ process finished with error"; \
		exit 1; \
	fi \
)
endef
# cc_or_std:
#   Selects between Cookiecutter hook context and standard execution context.
#
#   If COOKIECUTTER_HOOKS=true, expands to the first argument (Cookiecutter render).
#   Otherwise, expands to the second argument (normal project execution).
#
#   Usage:
#     PROJECT_ROOT := $(call cc_or_std,$(COOKIECUTTER_RENDER_DIR),$(PWD))
cc_or_std = $(if $(filter true,$(COOKIECUTTER_HOOKS)),$(1),$(2))
{# Settings Section #}
{{ make_macros.settings.settings(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
# --------------------------------------------------
# 🐍 Python / Virtual Environment
# --------------------------------------------------
PYTHON_CMD := python3.11
VENV_DIR := $(PROJECT_ROOT)/.venv
# --------------------------------------------------
# 🐍 Python Dependencies
# --------------------------------------------------
DEPS := .
DEV_DEPS := .[dev]
DEV_DOCS := .[docs]
# --------------------------------------------------
# 🐍 Python Commands
# --------------------------------------------------
CREATE_VENV := $(PYTHON_CMD) -m venv $(VENV_DIR)
ACTIVATE := source $(VENV_DIR)/bin/activate
PYTHON := $(ACTIVATE) && $(PYTHON_CMD)
PIP := $(PYTHON) -m pip
# --------------------------------------------------
# 🍪 Render template (cookiecutter, cookiecutter_project_upgrader)
# --------------------------------------------------
COOKIECUTTER := $(ACTIVATE) && cookiecutter
PROJECT_UPGRADE := $(ACTIVATE) && cookiecutter_project_upgrader
# --------------------------------------------------
# 🧬 Dependency Management (deptry)
# --------------------------------------------------
DEPTRY := $(ACTIVATE) && deptry
# --------------------------------------------------
# 🛡️ Security Audit (pip-audit)
# --------------------------------------------------
PIPAUDIT := $(ACTIVATE) && pip-audit
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
BLACK := $(PYTHON) -m black
# --------------------------------------------------
# 🔍 Linting (ruff, yaml, jinja2)
# --------------------------------------------------
RUFF := $(PYTHON) -m ruff
TOMLLINT := tomllint
YAMLLINT := $(PYTHON) -m yamllint
JINJA := $(ACTIVATE) && jinja2 --strict \
	--extension=cookiecutter.extensions.JsonifyExtension \
	--extension=cookiecutter.extensions.RandomStringExtension \
	--extension=cookiecutter.extensions.SlugifyExtension \
	--extension=cookiecutter.extensions.TimeExtension \
	--extension=cookiecutter.extensions.UUIDExtension
# --------------------------------------------------
# 🎓 Spellchecker (codespell)
# --------------------------------------------------
CODESPELL := $(ACTIVATE) && codespell
# --------------------------------------------------
# 🧠 Typing (mypy)
# --------------------------------------------------
MYPY := $(PYTHON) -m mypy
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
PYTEST := $(PYTHON) -m pytest
{# Documentation Command Settings #}
{{ make_macros.docs.doc_commands_section(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
BUMPVERSION := $(ACTIVATE) && bump-my-version bump --verbose
# Patch types:
MAJOR := major
MINOR := minor
PATCH := patch
# --------------------------------------------------
# 📜 Changelog generation (git-clif)
# --------------------------------------------------
GITCLIFF := git cliff
GITCLIFF_CHANGELOG := $(GITCLIFF) --output $(CHANGELOG_FILE)
GITCLIFF_CHANGELOG_RELEASE := $(GITCLIFF) --unreleased --tag $(RELEASE) --output $(CHANGELOG_RELEASE_FILE)
# --------------------------------------------------
# 🐙 Github Tools (git)
# --------------------------------------------------
GIT := git
GITHUB := gh
# Commands:
GIT_INIT_STATUS := git rev-parse --is-inside-work-tree > /dev/null 2>&1
# --------------------------------------------------
# 🚨 Pre-Commit (pre-commit)
# --------------------------------------------------
PRECOMMIT := $(ACTIVATE) && pre-commit
# --------------------------------------------------
# 🏃‍♂️ Nutri-Matic command
# --------------------------------------------------
NUTRIMATIC := $(PYTHON) -m nutrimatic
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
# --------------------------------------------------
# Dependency Checks
# --------------------------------------------------
git-dependency-check:
	$(AT)which $(GIT) >/dev/null || \
		{ echo "Git is required: sudo apt install git"; exit 1; }

gh-dependency-check:
	$(AT)which $(GITHUB) >/dev/null || \
		{ echo "GitHub is required: sudo apt install gh"; exit 1; }
# --------------------------------------------------
# 🐍 Virtual Environment Setup
# --------------------------------------------------
venv:
	$(AT)echo "🐍 Creating virtual environment..."
	$(AT)$(CREATE_VENV)
	$(AT)echo "✅ Virtual environment created."

install: venv
	$(AT)echo "📦 Installing project dependencies..."
	$(AT)$(PIP) install --upgrade pip setuptools wheel
	# $(AT)$(PIP) install -e $(DEPS)
	$(AT)$(PIP) install -e $(DEV_DEPS)
	$(AT)$(PIP) install -e $(DEV_DOCS)
	$(AT)echo "✅ Dependencies installed."
# --------------------------------------------------
# 🚨 Pre-Commit (pre-commit)
# --------------------------------------------------
# Note: Run as part of project initialization.  No manual run needed.
pre-commit-init:
	$(AT)echo "📦 Installing pre-commit hooks and hook-types..."
	$(AT)which $(GIT) >/dev/null || { echo "Git is required"; exit 1; }
	$(AT)$(PRECOMMIT) install --install-hooks
	$(AT)$(PRECOMMIT) install --hook-type pre-commit --hook-type commit-msg
	$(AT)echo "✅ pre-commit dependencies installed!"
# --------------------------------------------------
# 🍪 Project Updater (cookiecutter_project_upgrader)
# --------------------------------------------------
project-upgrade:
	$(AT)echo "🍪 Upgrading project from initial cookiecutter template..."
	$(AT)$(PROJECT_UPGRADE) --context-file ./docs/cookiecutter_input.json \
		--upgrade-branch main \
		-e "cookiecutter.json" \
		-e "$(COOKIE_DIR)"
	$(AT)echo "✅ Finished project upgrade!"
# --------------------------------------------------
# 🛡️ Security (pip-audit)
# --------------------------------------------------
security:
	$(AT)echo "🛡️ Running security audit..."
	$(AT)$(call run_ci_safe, $(PIPAUDIT))
	$(AT)echo "✅ Finished security audit!"
# --------------------------------------------------
# 🧬 Dependency Management (deptry)
# --------------------------------------------------
dependency-check:
	$(AT)echo "🧬 Checking dependency issues..."
	$(AT)$(DEPTRY) --pep621-dev-dependency-groups dev,docs \
		 $(SRC_DIR)
	$(AT)echo "✅ Finished checking for dependency issues!"
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
black-formatter-check:
	$(AT)echo "🔍 Running black formatter style check..."
	$(AT)$(call run_ci_safe, $(BLACK) --check $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Finished formatting check of Python code with Black!"

black-formatter-fix:
	$(AT)echo "🎨 Running black formatter fixes..."
	$(AT)$(BLACK) $(SRC_DIR) $(TESTS_DIR)
	$(AT)echo "✅ Finished formatting Python code with Black!"

format-check: black-formatter-check
format-fix: black-formatter-fix
# --------------------------------------------------
# 🔍 Linting (jinja2, ruff, toml, & yaml)
# --------------------------------------------------
render-cookiecutter:
	$(AT)rm -rf $(RENDERED_COOKIE_DIR)
	$(AT)$(COOKIECUTTER) . --no-input \
		--output-dir $(RENDERED_COOKIE_DIR) \
		--overwrite-if-exists

jinja2-lint-check:
	$(AT)echo "🔍 jinja2 lint..."
	$(AT)jq '{cookiecutter: .}' cookiecutter.json > /tmp/_cc_wrapped.json
	$(AT)$(JINJA_FILE_LIST) | tr '\0' '\n'
	$(AT)$(ACTIVATE) && $(JINJA_FILE_LIST) | \
		while IFS= read -r -d '' f; do \
			if file "$$f" | grep -q text; then \
				echo "Checking $$f"; \
				$(JINJA) "$$f" /tmp/_cc_wrapped.json || exit 1; \
			fi; \
		done
	$(AT)echo "✅ Finished linting check of jinja2 macro files with jinja2!"

ruff-lint-check:
	$(AT)echo "🔍 Running ruff linting..."
	$(AT)$(MAKE) list-folders
	$(AT)$(RUFF) check --config pyproject.toml $(SRC_DIR) $(TESTS_DIR) \
		--force-exclude '$(COOKIE_DIR)/pyproject.toml'
	$(AT)echo "✅ Finished linting check of Python code with Ruff!"

ruff-lint-fix:
	$(AT)echo "🎨 Running ruff lint fixes..."
	$(AT)$(RUFF) check --config pyproject.toml --show-files $(SRC_DIR) $(TESTS_DIR)
	$(AT)$(RUFF) check --config pyproject.toml --fix $(SRC_DIR) $(TESTS_DIR) \
		--force-exclude '$(COOKIE_DIR)/pyproject.toml'
	$(AT)echo "✅ Finished linting Python code with Ruff!"

toml-lint-check:
	$(AT)echo "🔍 Running Tomllint..."
	$(AT)$(TOML_FILE_LIST) | tr '\0' '\n'
	$(AT)$(ACTIVATE) && \
		$(TOML_FILE_LIST) \
		| xargs -0 -n 1 $(TOMLLINT)
	$(AT)echo "✅ Finished linting check of toml files with Tomllint!"

yaml-lint-check:
	$(AT)echo "🔍 Running yamllint..."
	$(AT)$(YAMLLINT) $(PROJECT_ROOT)
	$(AT)$(YAMLLINT) $(RENDERED_COOKIE_DIR)
	$(AT)echo "✅ Finished linting check of yaml files with yamllint!"

lint-check: render-cookiecutter ruff-lint-check toml-lint-check yaml-lint-check
lint-fix: ruff-lint-fix
# --------------------------------------------------
# 🎓 Spellchecker (codespell)
# --------------------------------------------------
spellcheck:
	$(AT)echo "🎓 Checking Spelling (codespell)..."
	$(AT)$(call run_ci_safe, $(CODESPELL))
	$(AT)echo "✅ Finished spellcheck!"
# --------------------------------------------------
# 🧠 Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	$(AT)echo "🧠 Checking types (MyPy)..."
	$(AT)$(MAKE) list-folders
	$(AT)$(call run_ci_safe, $(MYPY) $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Python typecheck complete!"
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
test:
	$(AT)echo "🧪 Running tests with pytest..."
	$(AT)$(call run_ci_safe, $(PYTEST))
	$(AT)echo "✅ Python tests complete!"
{# Documentation Section #}
{{ make_macros.docs.doc_actions(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
# TODO: Also create a git tag of current version.
bump-version-patch:
	$(AT)echo "🔖 Updating $(PROJECT_NAME) version from $(VERSION)..."
	$(AT)$(BUMPVERSION) $(PATCH)
	$(AT)echo "✅ $(PROJECT_NAME) version update complete!"
# --------------------------------------------------
# 📜 Changelog generation (git-cliff)
# --------------------------------------------------
# Note: Run as part of pre-commit.  No manual run needed.
changelog:
	$(AT)echo "📜 $(PROJECT_NAME) Changelog Generation..."
	$(AT)$(GITCLIFF_CHANGELOG)
	$(AT)$(GITCLIFF_CHANGELOG_RELEASE)
	$(AT)$(GIT) add $(CHANGELOG_FILE)
	$(AT)$(GIT) add $(CHANGELOG_RELEASE_FILE)
	$(AT)echo "✅ Finished Changelog Update!"
# --------------------------------------------------
# 🐙 Github Commands (git)
# --------------------------------------------------
# Note: Run as part of project initialization.  No manual run needed.
git-init: git-dependency-check
	$(AT)if ! $(GIT_INIT_STATUS); then \
		echo "🌱 $(PROJECT_NAME) Git initialization! 🎉"; \
		$(GIT) init; \
		$(GIT) add --all; \
		$(GIT) commit -m "chore(init): Init commit. \
			Project $(PROJECT_NAME) template generation complete."; \
		echo "✅ Finished Git initialization!"; \
	else \
		echo "ℹ️ Git is already initialized for $(PROJECT_NAME)."; \
	fi

git-release:
	$(AT)if $(GIT_INIT_STATUS); then \
		echo "📦 $(PROJECT_NAME) Release Tag - $(RELEASE)! 🎉"; \
		$(GIT) tag -a $(RELEASE) -m "Release $(RELEASE)"; \
		$(GIT) push origin $(RELEASE); \
		$(GITHUB) release create $(RELEASE) --generate-notes; \
	echo "✅ Finished uploading Release - $(RELEASE)! 🎉"; \
	else \
		echo "❌ Git is not yet initialized.  Skipping version release." \
	fi
# --------------------------------------------------
# 📢 Release
# --------------------------------------------------
pre-commit: test security dependency-check format-fix lint-check spellcheck typecheck
pre-release: clean install pre-commit build-docs changelog build
release: git-release bump-version-patch
{# Clean Section #}
{{ make_macros.clean.clean(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
{# Version Section #}
{{ make_macros.version.version() }}
{# Help Section #}
{{ make_macros.help.help(
	jekyll_enabled=cookiecutter.add_github_docs,
	sphinx_enabled=cookiecutter.add_sphinx_docs) }}
