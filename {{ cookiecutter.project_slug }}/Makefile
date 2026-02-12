{%- from '.cookiecutter_includes/registry/_config.j2' import ns with context -%}
{% import '.cookiecutter_includes/makefile/__init__.j2' as makefile_macros with context %}

{# TODO: Vars can be set like this and used in the macro #}
{%- set sphinx = cookiecutter.add_sphinx_docs -%}
{%- set github = cookiecutter.add_github_docs -%}

{{- makefile_macros.makefile.create(ns) -}}
