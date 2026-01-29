---
layout: default
title: cookiecutter-cookiecutter
nav_order: 1
description: __cookiecutter-cookiecutter__ is the cookiecutter template project to rule them all. Generates cookiecutter template projects and is able to be queried by generated projects for updates.
---
{% include snippet_loader.html %}

{% if site.carousel_images %}
    {% include image-carousel.html %}
{% endif %}

{% include_relative README.md %}

## ☕ Support Me
If you enjoy this project, please consider buying me a coffee or making a code contribution.  

## Social Links

{% include social-bar.html %}
