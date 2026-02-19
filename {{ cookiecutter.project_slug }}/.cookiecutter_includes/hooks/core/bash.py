# core/bash.py for cookiecutter-cookiecutter
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
import shutil
import subprocess
import sys
from pathlib import Path

from core.config import ensure_config
from core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def clean() -> None:
    """Remove _shared_hooks directory."""
    _shared_hooks = Path.cwd() / "_shared_hooks"
    logger.info(f"hooks directory: {_shared_hooks}")
    if _shared_hooks.exists() and _shared_hooks.is_dir():
        shutil.rmtree(_shared_hooks)
        logger.info(f"Removed {_shared_hooks} directory.")
    else:
        logger.info("_shared_hooks directory does not exist, nothing to remove.")


def make(cmd: str, *, verbose: bool = False) -> None:
    """Run a make target inside post-gen, exiting on failure."""
    logger.info(f"▶ Running: make {cmd}")
    try:
        result = subprocess.run(
            ["make", cmd],
            check=True,
            capture_output=True,
            text=True,
        )
        if verbose and result.stdout:
            logger.info(result.stdout.rstrip())
        logger.info(f"✅ Command succeeded: make {cmd}")
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Command failed: make {cmd}")
        # Optionally log stdout/stderr captured from the failed command
        if e.stdout:
            logger.error(f"STDOUT: {e.stdout}")
        if e.stderr:
            logger.error(f"STDERR: {e.stderr}")
        sys.exit(e.returncode)


def tree() -> None:
    """Run tree cmd inside the post-gen."""
    logger.info(f"Current working directory: {os.getcwd()}")
    subprocess.run(["tree", "-a", "."], check=False)
