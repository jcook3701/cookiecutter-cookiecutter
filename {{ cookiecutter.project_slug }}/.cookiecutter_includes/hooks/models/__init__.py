# models/__init__.py for cookiecutter-cookiecutter
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

from .accounts import Accounts
from .ccmeta import CCMeta
from .cctemplate import CCTemplate, CCTemplateVariable
from .config import DEFAULT_CONFIG, CLIConfig
from .github import GitHubAccount, GitHubAuth, GitHubRepo
from .metadata import DEFAULT_METADATA, Metadata
from .template import ConfigData, Namespace, TemplateRepo

__all__ = [
    "DEFAULT_CONFIG",
    "DEFAULT_METADATA",
    "Accounts",
    "CCMeta",
    "CCTemplate",
    "CCTemplateVariable",
    "CLIConfig",
    "ConfigData",
    "GitHubAccount",
    "GitHubAuth",
    "GitHubRepo",
    "Metadata",
    "Namespace",
    "TemplateRepo",
]
