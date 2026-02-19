# post_gen_logic/make.py for cookiecutter-cookiecutter
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

from typing import Any

from core.config import ensure_config
from core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def get_make_cmds(context: dict[str, Any]) -> list[str]:
    """Generate one or more documentation templates inside docs/"""

    make_cfg = context.get("_hooks", {}).get("post_gen_make_cmds", {})

    all_make_cmds = [
        "venv-create",
        "pip-install",
        "git-init",
        "pre-commit-init",
        "changelog",
        "build-docs",
    ]

    make_cmds = [cmd for cmd in all_make_cmds if make_cfg.get(cmd, False)]

    return make_cmds
