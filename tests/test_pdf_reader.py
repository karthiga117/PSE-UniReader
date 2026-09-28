"""Tests for the PDF reader."""

from __future__ import annotations

from pathlib import Path

import fitz
import pytest

from readers.pdf_reader import PdfReader
from services.exceptions import InvalidDocumentError


def test_pdf_reader_valid_pdf(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Hello PDF")
    document.save(file_path)
    document.close()

    result = PdfReader().read(str(file_path))

    assert result.title == "sample.pdf"
    assert result.document_type == "pdf"
    assert "Hello PDF" in result.content
    assert result.metadata["page_count"] == 1


def test_pdf_reader_multiple_pages(tmp_path: Path) -> None:
    file_path = tmp_path / "multi.pdf"
    pdf = fitz.open()
    for text in ["Page 1", "Page 2", "Page 3"]:
        page = pdf.new_page()
        page.insert_text((72, 72), text)
    pdf.save(file_path)
    pdf.close()

    result = PdfReader().read(str(file_path))

    assert "Page 1" in result.content
    assert "Page 2" in result.content
    assert "Page 3" in result.content
    assert result.metadata["page_count"] == 3


def test_pdf_reader_invalid_pdf(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.pdf"
    file_path.write_text("not a pdf")

    with pytest.raises(InvalidDocumentError):
        PdfReader().read(str(file_path))
