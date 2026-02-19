# core/metadata.py for cookiecutter-cookiecutter
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

from deprecated import deprecated


@deprecated("Use nutrimatic.models.Metadata from_package instead")
def init_metadata() -> None:
    """
    Populate module-level metadata such as ``__version__``, ``__author__``,
    and ``__license__`` based on the installed package metadata.

    This function attempts to read metadata from the installed distribution
    using :func:`importlib.metadata.metadata`. If the package is not installed
    (e.g., during development or when running from source), it falls back to
    reasonable defaults defined inside the function.

    The values are written into this module's global namespace so they may be
    imported from ``nutri-matic`` directly::

        >>> from nutrimatic import __version__, __author__
        >>> print(__version__)
        0.3.1

    This keeps the module metadata centralized and consistent with the
    package information defined in ``pyproject.toml``.
    """
    try:
        pkg_meta = metadata("nutri-matic")
        pkg_meta_dict = cast(Mapping[str, str], pkg_meta)

        version = pkg_meta_dict.get("Version", "0.1.0")
        author = pkg_meta_dict.get("Author", "Unknown")
        _license = pkg_meta_dict.get("License", "Unknown")

    except PackageNotFoundError:
        version = "0.1.0"
        author = "Jared Cook"
        _license = "MIT"

    _copyright = "2025 Jared Cook"

    # Write values back into module-level variables
    globals()["__version__"] = version
    globals()["__author__"] = author
    globals()["__license__"] = _license
    globals()["__copyright__"] = _copyright
