"""Reader for plain text documents."""

from __future__ import annotations

from pathlib import Path

from models.document import Document
from readers.base_reader import BaseReader
from services.exceptions import DocumentReadError, InvalidDocumentError


class TextReader(BaseReader):
    """Read .txt files into a common Document model."""

    def can_read(self, source: str) -> bool:
        return Path(source).suffix.lower() == ".txt"

    def read(self, source: str) -> Document:
        path = Path(source)
        if not path.exists():
            raise DocumentReadError(
                "Unable to read this document.\n\nPlease verify that the file is valid and try again."
            )

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="utf-8-sig")
            except UnicodeDecodeError as decode_exc:
                raise DocumentReadError(
                    "Unable to read this document.\n\nPlease verify that the file is valid and try again."
                ) from decode_exc
        except OSError as exc:
            raise DocumentReadError(
                "Unable to read this document.\n\nPlease verify that the file is valid and try again."
            ) from exc

        if not text:
            content = ""
        else:
            content = text

        return Document(
            title=path.name,
            source=str(path),
            document_type="text",
            content=content,
            metadata={"format": "txt", "encoding": "utf-8"},
        )
