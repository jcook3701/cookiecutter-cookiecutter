# --------------------------------------------------
# Changelog:
# --------------------------------------------------

## [unreleased]

### ⚙️  Miscellaneous

- *(init)* Project init.

### 🐛 Fixed

- *(dependency)* Fixed dependency check.
- *(template)* Made it so the cookiecutter.json could be modified.
- *(hooks)* Removed changelogs out of hooks for the moment.  Causing more problems than it will solve and not needed in the same way as it was for ansible-galaxy project.  First commit should be fine for updating changelog.
- *(cookiecutter)* Fixed project naming to fit with what I am already using for my cookiecutter projects.
- *(build)* Found out about Makefile default ; fixes problems when file is called by hooks. Makefile paths are all relative to the Makefile, which is necessary for build to succeed.
- *(build)* Found out about Makefile default ; fixes problems when file is called by hooks. Makefile paths are all relative to the Makefile, which is necessary for build to succeed.
- *(ci/cd)* Fixes so that ci/cd runs on feature branches.

### 🚀 Added

- *(build)* Build appears to be working now.
- *(hooks)* Updated hooks to use cookiecutter.json file vars and now don't have to do a ton a templating to make sure the hook make commands work correctly depending on the template being generated.
