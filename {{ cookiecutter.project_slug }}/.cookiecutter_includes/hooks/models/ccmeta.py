# models/ccmeta.py for cookiecutter-cookiecutter
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

from pydantic import BaseModel, Field

from .cctemplate import CCTemplate


class CCMeta(BaseModel):
    """
    Root model for teabag.toml.
    Adjust fields as needed to match your teabag.toml structure.
    """

    # If your file describes a single template:
    template: CCTemplate

    # Convenience / repo-level metadata
    tags: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)

    # Accept arbitrary extra keys (keeps backward compatibility)
    extra: dict[str, object] = Field(default_factory=dict)

    class Config:
        extra = "allow"
