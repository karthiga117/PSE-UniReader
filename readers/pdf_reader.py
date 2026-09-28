"""Reader for PDF documents."""

from __future__ import annotations

from pathlib import Path

import fitz

from models.document import Document
from readers.base_reader import BaseReader
from services.exceptions import DocumentReadError, InvalidDocumentError


class PdfReader(BaseReader):
    """Read PDF files into a common Document model."""

    def can_read(self, source: str) -> bool:
        return Path(source).suffix.lower() == ".pdf"

    def read(self, source: str) -> Document:
        path = Path(source)
        if not path.exists():
            raise InvalidDocumentError("Unable to read this document.\n\nPlease verify that the file is valid and try again.")

        try:
            document = fitz.open(path)
        except Exception as exc:
            raise InvalidDocumentError(
                "Unable to read this document.\n\nPlease verify that the file is valid and try again."
            ) from exc

        if document.is_encrypted:
            try:
                if not document.authenticate(""):
                    raise InvalidDocumentError(
                        "Unable to read this document.\n\nPlease verify that the file is valid and try again."
                    )
            except Exception as exc:
                raise InvalidDocumentError(
                    "Unable to read this document.\n\nPlease verify that the file is valid and try again."
                ) from exc

        page_count = document.page_count
        pages: list[str] = []
        try:
            for page_number in range(page_count):
                page = document[page_number]
                text = page.get_text("text")
                pages.append(f"--- Page {page_number + 1} ---\n\n{text.strip()}\n")
        except Exception as exc:
            raise DocumentReadError(
                "Unable to read this document.\n\nPlease verify that the file is valid and try again."
            ) from exc
        finally:
            document.close()

        content = "\n".join(pages).strip()
        return Document(
            title=path.name,
            source=str(path),
            document_type="pdf",
            content=content,
            metadata={"format": "pdf", "page_count": page_count},
        )
