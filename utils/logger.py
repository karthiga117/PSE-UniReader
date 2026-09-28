"""Simple logger for reader and app lifecycle events."""

from __future__ import annotations

import logging


def get_logger() -> logging.Logger:
    """Return a configured logger without exposing document content."""
    logger = logging.getLogger("pse_universal_reader")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger
