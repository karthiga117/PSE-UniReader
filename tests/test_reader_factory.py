"""Tests for the reader factory."""

from __future__ import annotations

from readers.excel_reader import ExcelReader
from readers.pdf_reader import PdfReader
from readers.text_reader import TextReader
from readers.word_reader import WordReader
from services.exceptions import UnsupportedFormatError
from services.reader_factory import ReaderFactory


def test_reader_factory_selects_matching_reader() -> None:
    factory = ReaderFactory()

    assert isinstance(factory.get_reader("example.txt"), TextReader)
    assert isinstance(factory.get_reader("example.pdf"), PdfReader)
    assert isinstance(factory.get_reader("example.docx"), WordReader)
    assert isinstance(factory.get_reader("example.xlsx"), ExcelReader)


def test_reader_factory_raises_for_unsupported_file_type() -> None:
    try:
        ReaderFactory().get_reader("notes.csv")
        assert False, "Expected UnsupportedFormatError"
    except UnsupportedFormatError:
        pass
