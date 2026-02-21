# models/config.py for cookiecutter-cookiecutter
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

from pathlib import Path

from pydantic import BaseModel

from .accounts import Accounts
from .github import GitHubAccount, GitHubAuth


class CLIConfig(BaseModel):
    """
    Represents user CLI configuration nutri-matic.

    Attributes:
         github: (GitHubAccount) GitHub users/org personal info.
         ga_tracking: (str) Google Analytics Tracking number.
         accounts: (Accounts) User accounts.
         default_template_branch: (str)
         cache_dir: (Path) Path to cache directory.
         log_file: (Path) Path to log file.
         verbose: (bool) Enable/Disable verbose mode.
    """

    github: GitHubAccount | None = None
    ga_tracking: str | None = None
    accounts: Accounts | None = None

    default_template_branch: str = "main"

    cache_dir: Path = Path.home() / ".cache" / "nutri-matic"
    log_file: Path = Path.home() / ".nutri-matic" / "nutri-matic.log"

    verbose: bool = False

    @property
    def log_dir(self) -> Path:
        return self.log_file.parent


DEFAULT_CONFIG = CLIConfig(
    github=GitHubAccount(user="", namespace="", email="", auth=GitHubAuth()),
    ga_tracking="",
    accounts=Accounts(),
)
