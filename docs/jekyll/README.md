# {{ site.title }}

[![License](https://img.shields.io/github/license/jcook3701/cookiecutter-cookiecutter)](LICENSE.md)

**Author:** {{ site.author }}  
**Version:** {{ site.version }}  

## Overview

{{ site.description }}  

**Utilizes:**  
The **{{ site.title }}** depends on the following repositories for its documentation and sub-features.  
* [Github docs](https://github.com/jcook3701/github-docs-cookiecutter) cookiecutter template generation.
* [Nutri-Matic](https://github.com/jcook3701/nutri-matic) cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.
<!-- * [Sphinx docs](https://github.com/jcook3701/sphinx-cookiecutter) template generation. -->

**Maintains:**  
The **{{ site.title }}** is used to maintain the build and ci/cd structure for the following projects.  
* [github-docs-cookiecutter](https://github.com/jcook3701/github-docs-cookiecutter) Github docs cookiecutter template generation.  
* [sphinx-cookiecutter](https://github.com/jcook3701/sphinx-cookiecutter) sphinx cookiecutter template generation.  
* [ansible-galaxy-cookiecutter](https://github.com/jcook3701/ansible-galaxy-cookiecutter) Ansible Galaxy cookiecutter template + integration with Github docs cookiecutter template generation.  
* [python3-cookiecutter](https://github.com/jcook3701/python3-cookiecutter) Python3 cookiecutter template project + Github docs cookiecutter template generation + Sphinx docs cookiecutter template generation.  
<!-- * [typescript-cookiecutter](https://github.com/jcook3701/typescript-cookiecutter) Typescript cookiecutter template project + Github docs cookiecutter template generation.  -->

***

**CI/CD Check List:**

* ![dependency-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
* ![format-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/format-check.yml/badge.svg)
* ![lint-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
* ![security-audit](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
* ![spellcheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
* ![tests](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/tests.yml/badge.svg)
* ![typecheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

***

## Usage Examples

**Example 1:** Pull from main branch.  
**Note:** [Nutri-Matic](https://github.com/jcook3701/nutri-matic) is needed in active python environment.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

**Example 2:** Pull from develop branch.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --checkout develop \
     --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

**Note:** replace ```test-project``` or any of the other variables with real context configuration variables.  

***

## Getting Started

* [Requirements]({{ site.github_io_url }}/manual/setup-guide/requirements)
* [Installation guide]({{ site.github_io_url }}/manual/introduction/installation-guide)  

## Documentation

The {{ site.title }} documentation is available at [docs]({{ site.github_io_url }}).  

## Contributing

If you're interested in contributing to the {{ site.title }} project:  
* Start by reading the [contributing guide]({{ site.github_io_url }}/manual/developer-resources/contribute).  
* Learn how to setup your local environment, in our [developer guide]({{ site.github_io_url }}/manual/contribute/developer-guide).  
* Look through our [style guide]({{ site.github_io_url }}/manual/contribute/style-guides/index).  

***

## Authors Notes
1. This code is currently intended to work with cookiecutter (v2.6+) from PyPi repositories.

## License

{{ site.copyright }}  

This project is licensed under the **{{ site.license }} License**.  
See the [LICENSE]({{ site.repo_blob }}/LICENSE.md) file for the full license text.  

SPDX-License-Identifier: {{ site.license }}

<!--
### Helpful Emojis:

📡🐋🛢️🚢 🦊💼 👨🏼‍💻🚧 📌 🌱🌳 ⏳🔑 🔫⌚ 🧼🧽 🔌💉

--->
