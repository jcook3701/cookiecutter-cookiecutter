# post_gen_logic/__init__.py for cookiecutter-cookiecutter
#
# SPDX-FileCopyrightText: Copyright (c) 2025-2026, Jared Cook
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .ansible import generate_ansible_dirs
from .auto_vars import replace_placeholders_in_dir
from .changelogs import generate_cliff_changelog_dirs
from .docs import generate_docs_templates
from .make import get_make_cmds

__all__ = [
    "generate_ansible_dirs",
    "generate_cliff_changelog_dirs",
    "generate_docs_templates",
    "get_make_cmds",
    "replace_placeholders_in_dir",
]
