# Makefile for cookiecutter_cookiecutter
#
# Copyright (c) 2025, Jared Cook
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <www.gnu.org>.
#
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
# --------------------------------------------------
# ⚙️ Build Settings
# --------------------------------------------------
PACKAGE_NAME := "cookiecutter-cookiecutter"
AUTHOR := "Jared Cook"
VERSION := 0.1.0
RELEASE := v$(VERSION)
# --------------------------------------------------
# 🐙 Github Build Settings
# --------------------------------------------------
GITHUB_USER := "jcook3701"
GITHUB_REPO := $(GITHUB_USER)/$(PACKAGE_NAME)
# --------------------------------------------------
# 📁 Build Directories
# --------------------------------------------------
PROJECT_ROOT := $(PWD)
HOOKS_DIR := $(PROJECT_ROOT)/hooks
SRC_DIR := $(HOOKS_DIR)
TEST_DIR := $(PROJECT_ROOT)/tests
TESTS_DIR := $(TEST_DIR)
DOCS_DIR := $(PROJECT_ROOT)/docs
SPHINX_DIR := $(DOCS_DIR)/sphinx
JEKYLL_DIR := $(DOCS_DIR)/jekyll
JEKYLL_SPHINX_DIR := $(JEKYLL_DIR)/sphinx
README_GEN_DIR := $(JEKYLL_DIR)/tmp_readme
CHANGELOG_DIR := $(PROJECT_ROOT)/changelogs
CHANGELOG_RELEASE_DIR := $(CHANGELOG_DIR)/releases
# --------------------------------------------------
# 📄 Build Files
# --------------------------------------------------
README_FILE := $(PROJECT_ROOT)/README.md
CHANGELOG_FILE := $(CHANGELOG_DIR)/CHANGELOG.md
CHANGELOG_RELEASE_FILE := $(CHANGELOG_RELEASE_DIR)/$(RELEASE).md
# --------------------------------------------------
# 🍪 Template Directories (cookiecutter)
# --------------------------------------------------
COOKIE_DIR := $(PROJECT_ROOT)/{{ cookiecutter.project_slug }}
COOKIE_MACRO_DIR := $(COOKIE_DIR)/.cookiecutter_includes
RENDERED_COOKIE_DIR := /tmp/rendered
RENDERED_VENV_DIR := $(RENDERED_COOKIE_DIR)/**/.venv
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
# 🍪 Render template (cookiecutter)
# --------------------------------------------------
COOKIECUTTER := $(ACTIVATE) && cookiecutter
# --------------------------------------------------
# 🧬 Dependency Management (deptry)
# --------------------------------------------------
DEPTRY := $(ACTIVATE) && deptry
# --------------------------------------------------
# 🛡️ Security Audit (pip-audit)
# --------------------------------------------------
PIPAUDIT :=	$(ACTIVATE) && pip-audit
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
# --------------------------------------------------
# 📚 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build --quiet
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
BUMPVERSION := $(ACTIVATE) && bump-my-version bump --verbose
# Patch types:
MAJOR := major
MINOR := minor
PATCH := patch
# --------------------------------------------------
# 📜 Changelog generation (git-cliff)
# --------------------------------------------------
GITCLIFF := git cliff
GITCLIFF_CHANGELOG := $(GITCLIFF) --output $(CHANGELOG_FILE)
GITCLIFF_CHANGELOG_RELEASE := $(GITCLIFF) --unreleased --tag $(RELEASE) --output $(CHANGELOG_RELEASE_FILE)
# --------------------------------------------------
# 🐙 Github Tools (git)
# --------------------------------------------------
GIT := git
GITHUB := gh
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
# Finds files of a given extension or "*" (all files) under a directory,
# skipping VENV_DIR and template markers like {{ }}.
define get_files_by_extension
	find $(1) -name "$(2)" \
		! -path "$(VENV_DIR)/*" \
		! -path "$(RENDERED_VENV_DIR)/*" \
		! -path "*{{*" \
		! -path "*}}*" \
		-print0
endef

JINJA_FILE_LIST := ( \
		$(call get_files_by_extension,$(PROJECT_ROOT),*.j2); \
		$(call get_files_by_extension,$(RENDERED_COOKIE_DIR),*.j2) \
	)
TOML_FILE_LIST := 	( \
		$(call get_files_by_extension,$(PROJECT_ROOT),*.toml); \
		$(call get_files_by_extension,$(RENDERED_COOKIE_DIR),*.toml) \
	)
# --------------------------------------------------
.PHONY: all list-folders venv install pre-commit-init security \
	dependency-check black-formatter-check black-formatter-fix \
	format-check format-fix ruff-lint-check ruff-lint-fix \
	toml-lint-check yaml-lint-check jinja2-lint-check \
	lint-check lint-fix spellcheck typecheck test sphinx \
	jekyll jekyll-serve build-docs run-docs bump-version-patch \
	changelog clean help
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
pre-commit-init:
	$(AT)echo "📦 Installing pre-commit hooks and hook-types..."
	$(AT)which $(GIT) >/dev/null || { echo "Git is required"; exit 1; }
	$(AT)$(PRECOMMIT) install --install-hooks
	$(AT)$(PRECOMMIT) install --hook-type pre-commit --hook-type commit-msg
	$(AT)echo "✅ pre-commit dependencies installed!"
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
# --------------------------------------------------
# 📚 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
sphinx:
	$(MAKE) -C $(SPHINX_DIR) all PUBLISHDIR=$(JEKYLL_SPHINX_DIR)

jekyll:
	$(MAKE) -C $(JEKYLL_DIR) all;

jekyll-serve: docs
	$(MAKE) -C $(JEKYLL_DIR) run;

build-docs: sphinx jekyll
run-docs: jekyll-serve
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
# TODO: Also create a git tag of current version.
bump-version-patch:
	$(AT)echo "🔖 Updating $(PACKAGE_NAME) version from $(VERSION)..."
	$(AT)$(BUMPVERSION) $(PATCH)
	$(AT)echo "✅ $(PACKAGE_NAME) version update complete!"
# --------------------------------------------------
# 📜 Changelog generation (git-cliff)
# --------------------------------------------------
# Note: Run as part of pre-commit.  No manual run needed.
changelog:
	$(AT)echo "📜 $(PACKAGE_NAME) Changelog Generation..."
	$(AT)$(GITCLIFF_CHANGELOG)
	$(AT)$(GITCLIFF_CHANGELOG_RELEASE)
	$(AT)$(GIT) add $(CHANGELOG_FILE)
	$(AT)$(GIT) add $(CHANGELOG_RELEASE_FILE)
	$(AT)echo "✅ Finished Changelog Update!"
# --------------------------------------------------
# 🐙 Github Commands (git)
# --------------------------------------------------
git-release:
	$(AT)echo "📦 $(PACKAGE_NAME) Release Tag - $(RELEASE)! 🎉"
	$(AT)$(GIT) tag -a $(RELEASE) -m "Release $(RELEASE)"
	$(AT)$(GIT) push origin $(RELEASE)
	$(AT)$(GITHUB) release create $(RELEASE) --generate-notes
	$(AT)echo "✅ Finished uploading Release - $(RELEASE)! 🎉"
# --------------------------------------------------
# 📢 Release
# --------------------------------------------------
pre-commit: test security dependency-check format-fix lint-check spellcheck typecheck
pre-release: clean install pre-commit build-docs changelog build
release: git-release bump-version-patch
# --------------------------------------------------
# 🧹 Clean artifacts
# --------------------------------------------------
clean-docs:
	$(AT)echo "🧹 Cleaning documentation artifacts..."
	$(AT)rm -rf $(SPHINX_DIR)/_build $(JEKYLL_SPHINX_DIR)
	$(AT)$(call run_ci_safe, cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN))
	$(AT)echo "✅ Cleaned documentation artifacts..."

clean-build:
	$(AT)echo "🧹 Cleaning build artifacts..."
	$(AT)rm -rf build dist *.egg-info
	$(AT)find $(SRC_DIR) $(TESTS_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	$(AT)-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	$(AT)echo "🧹 Cleaned build artifacts."

clean: clean-docs clean-build
# --------------------------------------------------
# Version
# --------------------------------------------------
version:
	$(AT)echo "$(PACKAGE_NAME)"
	$(AT)echo "author: $(AUTHOR)"
	$(AT)echo "version: $(VERSION)"
# --------------------------------------------------
# ❓ Help
# --------------------------------------------------
help:
	$(AT)echo "📦 $(PACKAGE_NAME) Makefile"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make venv                   Create virtual environment"
	$(AT)echo "  make install                Install dependencies"
	$(AT)echo "  make black-formatter-check  Run Black formatter check"
	$(AT)echo "  make black-formatter-fix    Run Black formatter"
	$(AT)echo "  make format-check           Run all project formatter checks (black)"
	$(AT)echo "  make format-fix             Run all project formatter autofixes (black)"
	$(AT)echo "  make jinja2-lint-check      Run jinja-cmd linter"
	$(AT)echo "  make ruff-lint-check        Run Ruff linter"
	$(AT)echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff"
	$(AT)echo "  make yaml-lint-check        Run YAML linter"
	$(AT)echo "  make lint-check             Run all project linters (ruff, yaml, & jinja2)"
	$(AT)echo "  make lint-fix               Run all project linter autofixes (ruff)"
	$(AT)echo "  make typecheck              Run Mypy type checking"
	$(AT)echo "  make test                   Run Pytest suite"
	$(AT)echo "  make sphinx                 Generate Sphinx Documentation"
	$(AT)echo "  make jekyll                 Generate Jekyll Documentation"
	$(AT)echo "  make build-docs             Build Sphinx + Jekyll documentation"
	$(AT)echo "  make run-docs               Serve Jekyll site locally"
	$(AT)echo "  make clean                  Clean build artifacts"
	$(AT)echo "  make version                Displays project information."
	$(AT)echo "  make all                    Run lint, typecheck, test, and docs"
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
