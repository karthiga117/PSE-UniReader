"""Abstract base class for all document readers."""

from __future__ import annotations

from abc import ABC, abstractmethod

from models.document import Document


class BaseReader(ABC):
    """Common interface for converting a source into a Document."""

    @abstractmethod
    def can_read(self, source: str) -> bool:
        """Return True if this reader supports the source."""

    @abstractmethod
    def read(self, source: str) -> Document:
        """Read the source and return a Document."""
