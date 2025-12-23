# --------------------------------------------------
# Changelog:
# --------------------------------------------------

## [unreleased]

### ⚙️  Miscellaneous

- *(init)* Project init.
- Feat 001 (#1)

* fix(dependency): Fixed dependency check.

* fix(template): made it so the cookiecutter.json could be modified.

* fix(hooks): removed changelogs out of hooks for the moment.  Causing more problems than it will solve and not needed in the same way as it was for ansible-galaxy project.  First commit should be fine for updating changelog.

* fix(cookiecutter): Fixed project naming to fit with what I am already using for my cookiecutter projects.

* fix(build): found out about Makefile default ; fixes problems when file is called by hooks. Makefile paths are all relative to the Makefile, which is necessary for build to succeed.

* fix(build): found out about Makefile default ; fixes problems when file is called by hooks. Makefile paths are all relative to the Makefile, which is necessary for build to succeed.

* feat(hooks): updated hooks to use cookiecutter.json file vars and now don't have to do a ton a templating to make sure the hook make commands work correctly depending on the template being generated.

* fix(ci/cd): Fixes so that ci/cd runs on feature branches.

* fix(test): Fixed test_bake_with_custom_name.
- Merge pull request #2 from jcook3701/develop

Feat 001 (#1)

### 🐛 Fixed

- *(template)* Testing for project update.
- *(template)* Removed items in the sub-template besides cookiecutter_input.json used by cookiecutter project upgrader.  Using exclude with the project upgrader command fixes everything.
- *(template)* Updates to template before pushing changes out to existing repos.

### 🚀 Added

- *(build)* Build appears to be working now.
- *(template)* Added sub template files to try and help ensure main cookiecutter directory is not set for deletion.
