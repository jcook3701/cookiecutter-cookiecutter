# core/logger.py for cookiecutter-cookiecutter
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

import logging
import sys
from functools import cache
from pathlib import Path
from typing import TextIO

import typer

from models import CLIConfig


@cache
class TyperHandler(logging.Handler):
    """Custom handler that routes log messages to typer.echo()."""

    def __init__(self, stream: TextIO | None = None) -> None:
        super().__init__()
        self.stream = stream or sys.stdout

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            try:
                # Try to use typer.echo() if running under a Typer context
                typer.echo(msg, file=self.stream)
            except Exception:
                # Fallback to normal write
                self.stream.write(msg + "\n")
                self.stream.flush()
        except Exception:
            self.handleError(record)


def _log_formatter(verbose: bool = False) -> logging.Formatter:
    """Return a logging formatter depending on verbosity."""
    fmt = "%(asctime)s | %(levelname)s | %(message)s" if verbose else "%(message)s"
    datefmt = "%H:%M:%S"
    return logging.Formatter(fmt, datefmt)


def _console_handler(cfg: CLIConfig, verbose: bool = False) -> logging.Handler:
    """Return a console handler — uses TyperHandler for CLI-aware output."""
    console_handler: logging.StreamHandler[TextIO] = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(_log_formatter(verbose))
    return console_handler


def _file_handler(cfg: CLIConfig) -> logging.FileHandler:
    """Return a FileHandler writing logs to"""
    log_dir: Path = cfg.log_dir
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = cfg.log_file

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
    )
    return file_handler


def setup_logging(cfg: CLIConfig, log_to_file: bool = True) -> logging.Logger:
    """
    Configure and return the main nutri-matic logger.

    Can be called at CLI startup, or once globally from config.
    """
    logger = logging.getLogger("nutri-matic")  # create a module-wide logger
    logger.setLevel(logging.DEBUG if cfg.verbose else logging.INFO)
    logger.handlers.clear()  # avoid duplicate logs in repeated runs

    logger.addHandler(_console_handler(cfg, cfg.verbose))
    if log_to_file:
        logger.addHandler(_file_handler(cfg))

    return logger
