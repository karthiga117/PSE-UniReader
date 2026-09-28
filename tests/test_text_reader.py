"""Tests for the text reader."""

from __future__ import annotations

from pathlib import Path

import pytest

from readers.text_reader import TextReader
from services.exceptions import DocumentReadError


def test_text_reader_valid_text(tmp_path: Path) -> None:
    file_path = tmp_path / "notes.txt"
    file_path.write_text("hello\nworld", encoding="utf-8")

    document = TextReader().read(str(file_path))

    assert document.title == "notes.txt"
    assert document.source == str(file_path)
    assert document.document_type == "text"
    assert document.content == "hello\nworld"
    assert document.metadata["format"] == "txt"


def test_text_reader_empty_text(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    document = TextReader().read(str(file_path))

    assert document.content == ""


def test_text_reader_unicode_text(tmp_path: Path) -> None:
    file_path = tmp_path / "unicode.txt"
    file_path.write_text("héllo — café\nمرحبا", encoding="utf-8")

    document = TextReader().read(str(file_path))

    assert document.content == "héllo — café\nمرحبا"


def test_text_reader_invalid_path() -> None:
    with pytest.raises(DocumentReadError):
        TextReader().read("missing.txt")
