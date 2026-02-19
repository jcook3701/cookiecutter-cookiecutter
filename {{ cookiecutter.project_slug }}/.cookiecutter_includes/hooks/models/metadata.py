# models/metadata.py for cookiecutter-cookiecutter
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

from collections.abc import Mapping
from importlib.metadata import PackageNotFoundError, metadata
from typing import cast

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    metadata type.

    Attributes:
        version: (str).
        author: (str).
        license: (str).
        copyright: (str).
    """

    version: str = ""
    author: str = ""
    license: str = ""

    @property
    def copyright(self) -> str:
        return f"2025 {self.author}"

    @classmethod
    def from_package(cls, package_name: str = "nutri-matic") -> "Metadata":
        """
        Create Metadata from the installed package metadata.

        Falls back to defaults if the package is not found.
        """
        try:
            pkg_meta = metadata(package_name)
            pkg_meta_dict = cast(Mapping[str, str], pkg_meta)

            return cls(
                version=pkg_meta_dict.get("Version", "0.1.0"),
                author=pkg_meta_dict.get("Author", "Jared Cook"),
                license=pkg_meta_dict.get("License", "MIT"),
            )
        except PackageNotFoundError:
            return DEFAULT_METADATA


DEFAULT_METADATA = Metadata(version="0.1.0", author="Jared Cook", license="MIT")
