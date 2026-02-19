# models/cctemplate.py for cookiecutter-cookiecutter
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

from pydantic import BaseModel, Field


class CCTemplateVariable(BaseModel):
    """Represents a single cookiecutter input variable."""

    name: str
    default: str | None = None
    description: str | None = None


class CCTemplate(BaseModel):
    """
    A single template defined in ccmeta.toml.
    """

    # --- universal / global template metadata ---
    name: str
    description: str | None = None
    path: Path = Field(..., description="Relative path to the template folder")

    # consistent across all project types:
    language: str | None = None  # e.g. "python", "node", "ansible"
    license: str | None = "MIT"  # default license
    version: str | None = "0.1.0"  # template versioning
    maintainer: str | None = None  # "Jared Cook", etc.
    project_type: str | None = None  # "library", "service", "cli"...

    # ─── cookiecutter input variables (template-specific) ───
    variables: list[CCTemplateVariable] = Field(
        default_factory=list, description="User input variables used by the template"
    )

    # ─── tags / feature flags ───
    tags: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)

    class Config:
        extra = "allow"
