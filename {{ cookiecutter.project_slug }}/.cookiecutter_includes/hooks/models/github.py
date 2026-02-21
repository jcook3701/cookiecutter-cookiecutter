# models/github.py for cookiecutter-cookiecutter
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
from typing import Literal

from pydantic import BaseModel


class GitHubAuth(BaseModel):
    """
    GitHub authentication types.

    Attributes:
         auth_type (Literal['token', 'ssh']): Type of authentication method.
         token (str | None): GitHub personal access token, if using token authentication.
         ssh_key_path (Path | None): Path to SSH private key, if using SSH authentication.
    """

    auth_type: Literal["token", "ssh"] = "ssh"
    token: str | None = None
    ssh_key_path: Path | None = Path("~/.ssh/id_rsa")


class GitHubAccount(BaseModel):
    """
    GitHub users/org personal info

    Attributes:
         user: (str) GitHub username.
         namespace: (str) GitHub organization or namespace; often same as user.
         email: (str) GitHub account email.
         auth: (GitHubAuth) Authentication configuration for GitHub access.
    """

    user: str = ""
    namespace: str = ""
    email: str = ""
    auth: GitHubAuth = GitHubAuth()


class GitHubRepo(BaseModel):
    """
    Represents a GitHub repository within a namespace.

    Attributes:
         owner: (str) GitHub repository owner.
         namespace: (str) GitHub organization or namespace; often same as user.
         name: (str) GitHub repository name.
         full_name: (str) GitHub owner fullname.
         description: GitHub repository description.
         url: (str) GitHub repository url.
         html_url: (str).
         ssh_url: (str).
         clone_url: (str).
         is_template: (bool).
    """

    owner: str = ""
    namespace: str = ""
    name: str = ""
    full_name: str = ""
    description: str = ""
    url: str = ""
    html_url: str = ""
    ssh_url: str = ""
    clone_url: str = ""
    is_template: bool = False
