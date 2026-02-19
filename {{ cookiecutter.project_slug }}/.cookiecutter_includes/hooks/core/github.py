# core/github.py for cookiecutter-cookiecutter
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

import json

import requests

from models import ConfigData, GitHubRepo, Namespace, TemplateRepo


def fetch_config(repo_url: str) -> ConfigData | None:
    """
    Fetch cookiecutter.json from a GitHub repo,
    trying both main and master branches.
    """
    branches = ["main", "master"]

    for branch in branches:
        raw_url = f"{repo_url}/raw/{branch}/config.json"
        resp = requests.get(raw_url)

        if resp.status_code == 200:
            try:
                data = json.loads(resp.text)
                return ConfigData(
                    project_name=data.get("project_name", ""),
                    author=data.get("author", ""),
                    version=data.get("version", ""),
                    description=data.get("description", ""),
                    variables=data,
                )
            except json.JSONDecodeError:
                return None

    return None


def fetch_namespace(namespace: str) -> Namespace:
    """Fetch all repositories in a namespace and their configs."""
    url = f"https://api.github.com/users/{namespace}/repos"
    resp = requests.get(url)
    resp.raise_for_status()
    repos = resp.json()

    templates = []
    for repo in repos:
        repo_url = repo["html_url"]
        config = fetch_config(repo_url)
        owner = repo["owner"]["login"] if "owner" in repo else namespace

        if config:
            templates.append(
                TemplateRepo(
                    repo=GitHubRepo(
                        owner=owner,
                        namespace=owner,
                        name=repo.get("name", ""),
                        full_name=repo.get("full_name", ""),
                        description=repo.get("description", ""),
                        url=repo.get("url", ""),
                        html_url=repo_url,
                        ssh_url=repo.get("ssh_url", ""),
                        clone_url=repo.get("clone_url", ""),
                        is_template=repo.get("is_template", ""),
                    ),
                    config=config,
                )
            )

    return Namespace(templates=templates)
