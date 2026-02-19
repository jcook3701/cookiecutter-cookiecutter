{%- from '.cookiecutter_includes/registry/_config.j2' import ns with context -%}
{% import '.cookiecutter_includes/hooks/__init__.j2' as hooks_macros with context %}

{{- hooks_macros.post_gen_project.create(ns) -}}
