# core/config.py for cookiecutter-cookiecutter
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
from functools import cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from core.logger import setup_logging
from models import DEFAULT_CONFIG, CLIConfig

CONFIG_EXT = ".yml"
CONFIG_PATH = Path.home() / ".config" / "nutri-matic" / f"config{CONFIG_EXT}"

logger = setup_logging(DEFAULT_CONFIG)


def _read_config(path: Path) -> dict[str, Any]:
    """Read JSON or YAML config and return as a dict."""
    logger.debug(f"Attempting to read config from {path}")
    if not path.exists():
        logger.info(f"Config file {path} does not exist.")
        raise FileNotFoundError(path)

    try:
        if path.suffix in {".yml", ".yaml"}:
            with open(path, encoding="utf-8") as f:
                data: dict[str, Any] = yaml.safe_load(f)
        else:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        # Runtime type check
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}")
        logger.debug("Config read successfully")
        return data
    except Exception as e:
        logger.warning(f"Failed to read config: {e}")
        raise


def _write_config(path: Path, cfg: CLIConfig) -> None:
    """Write config to file, respecting JSON/YAML based on extension."""
    path.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"Writing default config to {path}")

    if path.suffix in {".yml", ".yaml"}:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                cfg.model_dump(mode="json", by_alias=True),
                f,
                sort_keys=False,
            )
    else:
        json_str = cfg.model_dump_json(
            indent=4, fallback=lambda x: str(x) if isinstance(x, Path) else x
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(json_str)

    logger.debug("Config written successfully")


def _load_or_create_config(path: Path) -> CLIConfig:
    """Try to load the config; if missing or invalid, write defaults."""
    try:
        data = _read_config(path)
        cfg = CLIConfig.model_validate(data)
        logger.info(f"Config loaded from {path}")
    except (
        FileNotFoundError,
        json.JSONDecodeError,
        yaml.YAMLError,
        ValidationError,
    ) as e:
        logger.warning(f"Config invalid or missing ({e}), creating default.")
        _write_config(path, DEFAULT_CONFIG)
        cfg = DEFAULT_CONFIG

    return cfg


@cache
def ensure_config() -> CLIConfig:
    """Ensure the config exists and return a validated singleton CLIConfig instance."""
    return _load_or_create_config(CONFIG_PATH)
