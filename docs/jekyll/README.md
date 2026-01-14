# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview

{{ site.description }}  

 [Github docs](https://github.com/jcook3701/github-docs-cookiecutter) template generation + [Sphinx docs](https://github.com/jcook3701/sphinx-cookiecutter) template generation.  

<!--
This project is used to maintain the build and ci/cd structure for the following projects:  
[github-docs-cookiecutter](https://github.com/jcook3701/github-docs-cookiecutter)  
[sphinx-cookiecutter](https://github.com/jcook3701/sphinx-cookiecutter)  
[ansible-galaxy-cookiecutter](https://github.com/jcook3701/ansible-galaxy-cookiecutter)  
[python-cookiecutter]()  
-->

![dependency-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
![format-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/format-check.yml/badge.svg)
![lint-check](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
![security-audit](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
![spellcheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
![tests](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

## Usage Examples:

__Example:__ Pull from main branch.  
__Note:__ [Nutri-Matic](https://github.com/jcook3701/nutri-matic) is needed in active python environment.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

__Example:__ Pull from develop branch.  

```shell
$ cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git \
    --checkout develop \
     --no-input \
    project_name="test-project" \
    description="Cookiecutter test project."
```

__Note:__ replace ```test-project``` or any of the other variables with real context configuration variables.  

***

## Development Strategy:

__Note:__ All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.  
### 🐍️ Build environment (.venv)

``` shell
$ make install
```

### 🧬 Dependency Management (deptry)

```shell
$ make dependency-check
```

### 🛡️ Security Audit (pip-audit)

```shell
$ make security
```

### 🎨 Formatting (black)

```shell
$ make format-check
```

```shell
$ make format-fix
```

### 🔍 Linting (jinja2-cli, ruff, tomllint, & yaml-lint)

``` shell
$ make lint-check
```

``` shell
$ make lint-fix
```

### 🎓 Spellchecking (codespell)

```shell
$ make spellcheck
```

### 🧠 Typechecking (mypy)

``` shell
$ make typecheck
```

### 🧪 Testing (pytest)

``` shell
$ make test
```

### 🚀 Release (git tag)

```shell
$ make release
```

### ❓ Build Help

``` shell
$ make help
```

## Commit Help:

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

## Requirements:

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

### Authors Notes:
1. This code currently works with cookiecutter 1.7 from Ubuntu's apt repositories.

### TODO's
1. Update pyproject.toml to use latest version of cookiecutter to get latest features.
2. Update cookiecutter.json with:
	```"license": ["GPL-3.0", "Apache-2.0", "BSD-3-Clause", "MIT"],```

<!--
### Helpful Emojis:

📡🐋🛢️🚢 🦊💼 👨🏼‍💻🚧 📌 🌱🌳 ⏳🔑 🔫⌚ 🧼🧽 🔌💉

### Authors Hidden TODO's

For Sphinx-cookiecutter -> Need to move from cookiecutter.project_name to cookiecutter.project_slug
1.

# Maybe upgrade to python 3.12 in future: "pyproject>=1!0.1.2",

# TODO: Might add this to cookiecutter.json
  "_settings": {
    "changelog": {
      "ansible": false,
      "git_cliff": true
    },
    "extra": {
      "cookiecutter_project_upgrader": true,
      "deptry": true,
      "pip-audit": true,
      "pre-commit": true
    },
    "format": {
      "black": true,
      "ruff": false,
      "prettier": false
    },
    "lint": {
      "ansible": false,
      "jinja2": true,
      "ruff": true,
      "toml": true,
      "yaml": true
    },
    "spelling": {
      "codespell": true,
      "cspell": true
    },
    "typecheck": {
      "mypy": true
    },
    "test": {
      "pytest": true
    }
  },
--->
