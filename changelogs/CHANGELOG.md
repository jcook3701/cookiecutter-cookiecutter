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
- Feat 002 (#4)

* feat(template): added sub template files to try and help ensure main cookiecutter directory is not set for deletion.

* fix(template): testing for project update.

* fix(template): removed items in the sub-template besides cookiecutter_input.json used by cookiecutter project upgrader.  Using exclude with the project upgrader command fixes everything.

* fix(template): updates to template before pushing changes out to existing repos.

* fix(template): fixes for jinja2 templating.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup templates for gitignore. And prepared for makefile and pyproject files.

* feat(template): setup template fixes for pyproject.toml.

* feat(template): simplified templates and added functionality.

* fix(build): ci/cd - lint-check, jekyll pages.

* fix(template): turned of sphinx docs for cookiecutter template projects.  Not really needed.

* feat(template): updated template makefile to add or remove document gen commands depending on cookiecutter settings.

* feat(template): Docs are now removed/added from makefile depending on user selection.

* feat(build): Template updates for auto generating the project makefile.  Getting this setup to eventually be pulled into sub-projects to use in sub-templates that also use Makefile for project building.

* fix(template): fixed gitignore jinja template.

* feat(template): Updated all template files to include GPL-V3 header.  Also updates for template to auto generate pytest cookiecutter bake depending on needs.

* fix(template): forgot bracket in cookiecutter.json

* feat(ci/cd): ci/cd is no longer blocked by the cookiecutter copy without render.  All files should now have header dependent on selected license.  Also updated spellchecker configuration to add a bunch of dictionaries and words that are being used throughout the project.

* feat(template): cliff, yamllint, pre-commit, and gitignore updates to include template license header.  Also fixes to .gitignore jinja2 template.

* feat(template): Update makefile template phony and help jinja2 cookiecutter generation.

* fix(build): Fixed pytest within both main project and template.

* fix(jinja2): lint check had to ignore __init__.j2 files.  Need to find a better fix for the future.
- Merge pull request #5 from jcook3701/develop

Feat 002 (#4)
- Feat 003 (#6)

* feat(template): Added readme generation to jekyll component.

* fix(docs): Minor fix for format-check badge.
- Merge pull request #8 from jcook3701/develop

fix(build): Updates to template pre-commit to auto build docs on comm…
- Merge pull request #10 from jcook3701/develop

feat-005 (#8)
- Merge pull request #11 from jcook3701/feat-006

Feat-006
- Merge pull request #12 from jcook3701/develop

Develop
- Merge pull request #14 from jcook3701/develop

Feat 007 (#13)
- Merge pull request #15 from jcook3701/feat-008

Feat 008
- Feat 009 (#16)

* feat(build): updates to project-upgrade make command.

* fix(upgrade): Upgrade fix.
- Merge pull request #17 from jcook3701/develop

Feat 009 (#16)
- Feat 010 (#18)

* fix(template): fix for template post generation hooks.

* fix(template): fixes for template post generation project.

* fix(template): fixes for template post generation project.
- Merge pull request #19 from jcook3701/develop

Feat 010 (#18)
- Feat 011 (#20)

* fix(upgrade): Fix for upgrade variables.

* chore(readme): pushing readme changes.

* fix(docs): Fixed readme to remove duplicate description.
- Merge pull request #21 from jcook3701/develop

Feat 011 (#20)
- Merge pull request #30 from jcook3701/develop

Feat 012 issue templates
- Update template (#32)
- Merge pull request #33 from jcook3701/develop

Update template (#32)
- Feat 016 markdown lint

feat(lint): Added markdown lint file to both project and template.
- Merge pull request #35 from jcook3701/develop

Feat 016 markdown lint
- Merge pull request #36 from jcook3701/feat-017-issues-teplate-bug-fix

feat-017 issue template bug fix
- Merge pull request #37 from jcook3701/develop

Develop
- Feat 018 project upgrader cmd (#39)

* fix(update): I think this should fix the project upgrader and not break the rest of the use cases but a test is needed.

* chore(update) Update template
- Merge pull request #40 from jcook3701/develop

Feat 018 project upgrader cmd (#39)
- Feat 019 docs update (#42)

* feat(docs): Added security and contributing files to .github folder.

* chore(upgrade): Update template using cookiecutter_project_upgrader.

* feat(jekyll): Project has been upgraded to work with Jekyll 4.4 and builds with a manual command so we can use newer version of just the docs template.

* feat(ci/cd): Updates to spellcheck and markdown lint configuration file.

* fix(ci/cd): Jekyll ci/cd fixes.
- Merge pull request #43 from jcook3701/develop

Feat 019 docs update (#42)
- Feat 14 CLA (#29)

* feat(cla): prep for CLA.

* fix(cla): CI/CD fix for item cla causing unit tests to fail.

* fix(yaml): Yaml format fixes for cla ci/cd action.

* fix(spelling): Added yaml to list of real words.

* fix(contributing): Updates to the contributing file for use of CLA by default over DCO. Need to update template settings to swap between both.

* feat(template): Added Pull request templates and codeowners to project to speed up pull requests.

* fix(template): Minor fixes removed my actual github username and replaced with cookiecutter.github_username.

* feat(license): Major license change. Moved everything to .cookiecutter_includes and build license file and headers from there.  Also setup Djlint in the main project and should keep testing along with moving that to the template as well once done.

* fix(linting): Fixes moved off jinja2 linter and to djlint.

* fix(linting): Fixes moved off jinja2 linter and to djlint.

* fix(linting): All linting passes again.

* fix(djlint): Added djlint to template so doesn't get removed on next project upgrade.

* feat(license): License template clean up.  Still a little ways to go.

* fix(license): License header adjusted correctly to be REUSE Compliant.

* fix(license): Fix for linting and updates to license-header.j2 function comments.

* fix(license): License headers look correct without extra '#' at very end.

* feat(license): License headers and main LICENSE file generation working!

* fix(docs): Readme fixes.

* fix(license): License header fix to remove extra space after '#'.

* fix(license): License headers now show range from when project was started to current year.
- Merge pull request #46 from jcook3701/develop

Feat 14 CLA (#29)
- Feat 020 (#47)

* fix(jekyll): Jekyll ci/cd to include necessary environment variables.

* fix(docs): Minor updates for contributing and security documentation.

* fix(license): Moved license to markdown extension.
- Merge pull request #48 from jcook3701/develop

Feat 020 (#47)
- Feat 020 (#49)

* fix(jekyll): Jekyll ci/cd to include necessary environment variables.

* fix(docs): Minor updates for contributing and security documentation.

* fix(license): Moved license to markdown extension.

* fix(ci/cd): Fixes for Jekyll and CLA ci/cd.

* fix(lint): Linting fixes.
- Merge pull request #50 from jcook3701/develop

Feat 020 (#49)
- Feat 021 (#51)

* fix(ci/cd): Fixes ci/cd python install commands.

* fix(sub-template): Removed git-cliff from being added to sub-template hooks.
- Merge pull request #52 from jcook3701/develop

Feat 021 (#51)
- Feat 022 (#53)

* fix(ci/cd): Fixed jekyll and CLA.  Also fixes to actually get functionally out of the pull request templates that were setup.

* fix(cla): added default branch setting to project for CLA to ensure default branch is always correct regardless of how old the project is.
- Feat 022 (#53) (#54)

* fix(ci/cd): Fixed jekyll and CLA.  Also fixes to actually get functionally out of the pull request templates that were setup.

* fix(cla): added default branch setting to project for CLA to ensure default branch is always correct regardless of how old the project is.
- Feat 023 (#55)

* fix(cla): Fix for cla template trim_block.  Also added github_io to template settings.

* fix(jinja-runtime): Fix for jinja configuration file for vscode plugin.
- Merge pull request #56 from jcook3701/develop

Feat 023 (#55)
- Feat 024 (#57)

* fix(styling): Generally YAML fixes reducing warnings.  Also preparation for cookiecutter project upgrader.

* feat(upgrader): Project upgrader preparation.

* feat(docs): Added code of conduct to the template to fix documentation links.  I have a few changes I would like to make to it as well.

* fix(docs): Small customization to the code of conduct. Along with updates for Addressing and Repairing Harm.

* feat(docs): added new support file.  Along with updates to CLA ci/cd.  Along with general updates to other special configuration and community health files.

* feat(ci/cd): Updated cla to be swapped to dco.  Need to update github-docs next.

* feat(docs): Added updates to Community health files to handle cookiecutter.contribution_model variable.

* fix(cspell): Added jinja2 end functions to spellchecker to remove all the spelling warnings on code pages.

* feat(support): Added funding section to the support page.

* fix(cla): minor tab to spaces fix.
- Merge pull request #60 from jcook3701/develop

Feat 024 (#57)
- Feat 025 (#61)

* fix(security): Fix for security.md file markdown format.

* chore(upgrade): Update template from itself (cookiecutter-cookiecutter) using ```cookiecutter_project_upgrader```.
- Merge pull request #62 from jcook3701/develop

Feat 025 (#61)
- *(CLA)* Creating file for storing CLA Signatures.
- Feat 025 (#63)

* fix(security): Fix for security.md file markdown format.

* fix(license): license fixes for the .cookiecutter_includes directory.

* feat(template): Added 'documentation' to the template_type options.  This should fix the hooks issue.
- Merge pull request #64 from jcook3701/develop

Feat 025 (#63)
- Feat 026 (#65)

* fix(hooks): Fixed template hooks.

* fix(jinja2): configuration file update.

* fix(license): Forgot to fix one of the license headers and needed to remove file as well.

* chore(upgrade): Upgraded project using ```cookiecutter_project_upgrader```.
- Merge pull request #66 from jcook3701/develop

Feat 026 (#65)
- Feat 027 (#67)

* fix(template): Fixed missing commas that are causing gitignore error.

* chore(update) Update template using ```cookiecutter_project_upgrader```.
- Merge pull request #68 from jcook3701/develop

Feat 027 (#67)
- Feat 028 (#69)

* fix(python): Fixed python configuration file license name.

* feat(docs): readme updates that link to github_io documentation.

* fix(docs): Minor fix for license image shield.

* fix(docs): readme license fix.

* fix(changelogs): Added configuration item for changelog tool selection.  Also updated hooks.  This should finally fixes #41.
- Merge pull request #70 from jcook3701/develop

Feat 028 (#69)
- Feat 029 (#71)

* fix(template): Added none option to changelog selection to allow user to turn of this feature if needed.

* chore(update): Update template from ```cookiecutter-cookiecutter```.

* fix(upgrader): Added changelog setting to upgrader configuration files.

* fix(hooks): Fixed hook template for changelog configuration settings.
- Merge pull request #72 from jcook3701/develop

Feat 029 (#71)
- Feat 030 (#75)

* feat(template): Moved all community health files to the .cookiecutter_includes so they can be used on meta templates (secondary templates).

* fix(jinja2): Fixed linting issues.  Next to workflows.

* feat(ci/cd): added a few of the workflows files to the  template engine.

* feat(ci/cd): all ci/cd has been moved to jinja2 templating.
- Merge pull request #76 from jcook3701/develop

Feat 030 (#75)
- Feat 031 (#77)

* fix(cla): fixed cla ci/cd yaml errors.

* chore(update) Update template with cookiecutter_project_upgrader
- Merge pull request #78 from jcook3701/develop

Feat 031 (#77)
- Feat 032 (#81)

* fix(template): fixed default branch for project upgrader.

* fix(template): fixed default branch for project upgrader.

* feat(jinja): Creating gitignore and pyproject templates. Next to do is the Makefile and then templates should be done for a bit.

* fix(jinja): Fixed gitignore and pytest templates.

* fix(jinja): Fixed gitignore and pytest templates.

* feat(jinja2): un-finished templates updates for pyproject configuration file.

* feat(pyproject): Pyproject template is now working.  Needs some clean up. But MVP is good to go.

* feat(jinja2): Updates to python pyproject configuration files.

* feat(jinja2): Updates to pyproject template.

* Update template

* feat(jinja2): Fixed .gitignore template formatting.

* feat(jinja2): .gitignore template file clean up.

* feat(jinja2): Very minor fix for optional-deps pyproject template.
- Merge pull request #82 from jcook3701/develop

Feat 032 (#81)

### 🐛 Fixed

- *(build)* Updates to template pre-commit to auto build docs on commit and fix to project upgrader command. (#7)
- *(template)* Fixed git auto remove to ignore all readme files on merge.
- *(changelogs)* Removed changelogs make command from running during post hook generation scripts.
- *(issues)* Fixes and updates to issue templates.  Added developer only template to avoid having to fill out user forms for each project task.

### 🚀 Added

- *(build)* Build appears to be working now.
- *(git)* Added git attributes file to hopefully ignore updating specific files after they have been created. (#9)
- *(fix)* General fixes for template to ensure proper upgrade functionality. (#13)
- *(issues)* Setup issue templates. (#22)
