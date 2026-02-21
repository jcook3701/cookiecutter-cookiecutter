# post_gen_logic/ansible.py for cookiecutter-cookiecutter
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

from core.config import ensure_config
from core.logger import setup_logging
from core.utils import make_dirs

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def generate_ansible_dirs() -> None:
    """Generate ansible project directories"""
    ansible_dirs = [
        "plugins",
        "plugins/action",
        "plugins/inventory",
        "plugins/lookup",
        "plugins/module_utils",
        "plugins/modules",
        "playbooks",
        "playbooks/files",
        "playbooks/tasks",
        "playbooks/templates",
        "playbooks/vars",
        "roles",
        "tests",
        "tests/units/",
        "tests/units/plugins",
        "tests/units/plugins/action",
        "tests/units/plugins/inventory",
        "tests/units/plugins/lookup",
        "tests/units/plugins/module_utils",
        "tests/units/plugins/modules",
        "tests/integration",
        "tests/integration/targets",
    ]
    make_dirs(ansible_dirs)
