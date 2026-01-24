# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  
__License:__ [![License](https://img.shields.io/github/license/jcook3701/cookiecutter-cookiecutter)](LICENSE)

## Overview

{{ site.description }}  

__Utilizes:__  
The __{{ site.title }}__ depends on the following repositories for its documentation and sub-features.  
* [Github docs](https://github.com/jcook3701/github-docs-cookiecutter) cookiecutter template generation.
* [Nutri-Matic](https://github.com/jcook3701/nutri-matic) cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.
<!-- * [Sphinx docs](https://github.com/jcook3701/sphinx-cookiecutter) template generation. -->

__Maintains:__  
The __{{ site.title }}__ is used to maintain the build and ci/cd structure for the following projects.  
* [github-docs-cookiecutter](https://github.com/jcook3701/github-docs-cookiecutter) Github docs cookiecutter template generation.  
* [sphinx-cookiecutter](https://github.com/jcook3701/sphinx-cookiecutter) sphinx cookiecutter template generation.  
* [ansible-galaxy-cookiecutter](https://github.com/jcook3701/ansible-galaxy-cookiecutter) Ansible Galaxy cookiecutter template + integration with Github docs cookiecutter template generation.  
* [python3-cookiecutter](https://github.com/jcook3701/python3-cookiecutter) Python3 cookiecutter template project + Github docs cookiecutter template generation + Sphinx docs cookiecutter template generation.  
<!-- * [typescript-cookiecutter](https://github.com/jcook3701/typescript-cookiecutter) Typescript cookiecutter template project + Github docs cookiecutter template generation.  -->

***

__CI/CD Check List:__  
* ![dependency-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
* ![format-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/format-check.yml/badge.svg)
* ![lint-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
* ![security-audit](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
* ![spellcheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
* ![tests](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/tests.yml/badge.svg)
* ![typecheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

***

## Usage Examples

__Example 1:__ Pull from main branch.  
__Note:__ [Nutri-Matic](https://github.com/jcook3701/nutri-matic) is needed in active python environment.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

__Example 2:__ Pull from develop branch.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --checkout develop \
     --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

__Note:__ replace ```test-project``` or any of the other variables with real context configuration variables.  

***

## Commit Help

__Note:__ Commits are required to be conventional git commit message.  This helps with the auto-generation of the changelog files and is enforced by pre-commit.  
__example:__  

```shell
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

* ```<type>```: A required noun that describes the nature of the change.  
* ```[optional scope]```: An optional phrase within parentheses that specifies the part of the codebase being affected (e.g., fix(parser):).  
* ```<description>```: A required short, imperative-mood summary of the changes.  
* ```[optional body]```: A longer description providing additional context and "what and why" details.  
* ```[optional footer(s)]```: Used for adding meta-information, such as issue references (Fixes #123) or indicating breaking changes.  

***

## Requirements

__Python 3.11__  

```shell
$ sudo apt install python3.11
```

__[Nutri-Matic](https://github.com/jcook3701/nutri-matic)__  
__Note:__ This is needed for the cookiecutter hooks to run correctly.  Without this package installed in active python environment cookiecutter pull will fail.  

```shell
$ pip install nutri-matic
```

__[rustup](https://rust-lang.org/tools/install/)__  
__Note:__ I found that it is easiest to use rustup to manage rustc and cargo but this is not required.  
__Example:__ Install rustup with the following:  

```shell
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

__[git-cliff](https://git-cliff.org/)__  
__Note:__ git-cliff can generate changelog files from the Git history by utilizing conventional commits as well as regex-powered custom parsers.  

```shell
$ cargo install git-cliff
```

***

### Authors Notes
1. This code is currently intended to work with cookiecutter (v2.1+).

<!--
### Helpful Emojis:

📡🐋🛢️🚢 🦊💼 👨🏼‍💻🚧 📌 🌱🌳 ⏳🔑 🔫⌚ 🧼🧽 🔌💉

--->
