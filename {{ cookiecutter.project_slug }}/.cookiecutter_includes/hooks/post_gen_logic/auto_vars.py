# post_gen_logic/auto_vars.py for cookiecutter-cookiecutter
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

import os
from pathlib import Path
from typing import Any

from core.config import ensure_config
from core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def replace_placeholders_in_file(
    filepath: Path,
    replacements: dict[str, Any],
) -> None:
    """Reads a file, replaces the placeholder, and writes it back."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.debug(f"Skipping binary file: {filepath}")
        return
    except Exception as e:
        logger.info(f"An error occurred processing file {filepath}: {e}")
        return

    changed = False

    for placeholder, value in replacements.items():
        if placeholder in text:
            text = text.replace(placeholder, str(value))
            changed = True

    if changed:
        filepath.write_text(text, encoding="utf-8")
        logger.debug(f"Updated: {filepath}")


def replace_placeholders_in_dir(
    replacements: dict[str, Any],
    path: Path = Path.cwd(),
) -> None:
    """
    Walk through every file in the newly generated project directory
    and replace placeholders in all files.
    """
    for root, _dirs, files in os.walk(path):
        for file in files:
            # Exclude this hook script itself from the replacement
            if file == "post_gen_project.py":
                continue

            file_path: Path = Path(root) / file
            replace_placeholders_in_file(file_path, replacements)

    logger.debug("Timestamp injection complete.")
