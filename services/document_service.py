"""Service layer that coordinates document opening."""

from __future__ import annotations

from services.exceptions import DocumentReadError, InvalidDocumentError
from services.reader_factory import ReaderFactory


class DocumentService:
    """Open documents using the registered factory."""

    def __init__(self, reader_factory: ReaderFactory) -> None:
        self.reader_factory = reader_factory

    def open(self, source: str):
        """Open a file and return a normalized Document."""
        reader = self.reader_factory.get_reader(source)
        try:
            return reader.read(source)
        except (InvalidDocumentError, DocumentReadError):
            raise
        except Exception as exc:  # pragma: no cover - defensive fallback
            raise DocumentReadError(
                "Unable to read this document.\n\nPlease verify that the file is valid and try again."
            ) from exc
