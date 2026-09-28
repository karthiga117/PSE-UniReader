"""Factory for choosing the correct document reader."""

from __future__ import annotations

from pathlib import Path

from readers.base_reader import BaseReader
from readers.excel_reader import ExcelReader
from readers.pdf_reader import PdfReader
from readers.text_reader import TextReader
from readers.word_reader import WordReader
from services.exceptions import UnsupportedFormatError


class ReaderFactory:
    """Select a reader based on file extension."""

    def __init__(self, readers: list[BaseReader] | None = None) -> None:
        self.readers = readers or [
            TextReader(),
            PdfReader(),
            WordReader(),
            ExcelReader(),
        ]

    def get_reader(self, source: str) -> BaseReader:
        """Return a matching reader or raise a friendly error."""
        for reader in self.readers:
            if reader.can_read(source):
                return reader

        extension = Path(source).suffix.lower()
        if not extension:
            raise UnsupportedFormatError(
                "Unsupported file format.\n\nPSE Universal Reader currently supports: "
                "PDF, Word, Excel and Text."
            )

        raise UnsupportedFormatError(
            f"Unsupported file format: {extension}.\n\nPSE Universal Reader "
            "currently supports: PDF, Word, Excel and Text."
        )
