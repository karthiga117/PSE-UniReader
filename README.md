# PSE Universal Reader

A Windows desktop application built with Python and PySide6 that provides a single reading interface for multiple content types.

## Supported Formats

- PDF       ✅
- Word      ✅
- Excel     ✅
- TXT       ✅
- Markdown  ⏳
- Web       ⏳

## Phase 2 Architecture

```text
                PySide6 UI
                     │
                     ▼
             DocumentService
                     │
                     ▼
               ReaderFactory
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     PDFReader   WordReader   ExcelReader
        │            │            │
        └────────────┼────────────┘
                     ▼
                 Document
                     │
                     ▼
               ReaderWidget
```

## Project Status

**Phase 2 — Core Document Reading Architecture**

The project now includes a format-independent document model, reader interface, concrete readers, service layer, and a basic PySide6 viewer.

## Technology

- Python 3.12+
- PySide6
- PyMuPDF
- python-docx
- openpyxl
- pytest

## Directory Structure

```text
pse-universal-reader/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── models/
│   ├── __init__.py
│   └── document.py
│
├── readers/
│   ├── __init__.py
│   ├── base_reader.py
│   ├── text_reader.py
│   ├── pdf_reader.py
│   ├── word_reader.py
│   └── excel_reader.py
│
├── services/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── reader_factory.py
│   └── document_service.py
│
├── ui/
│   ├── __init__.py
│   └── reader_widget.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_text_reader.py
│   ├── test_pdf_reader.py
│   ├── test_word_reader.py
│   ├── test_excel_reader.py
│   └── test_reader_factory.py
│
├── examples/
├── requirements.txt
├── README.md
└── .gitignore
```

## Run

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m app.main
```

Run the tests:

```bash
pytest
```

## Design Principle

The UI should never contain document-format-specific parsing logic.

Each reader converts its source into a common `Document` representation so future features such as search and AI can work independently of the original file type.

## Roadmap

### Phase 1
Foundational app shell.

### Phase 2
Document model, readers, service layer, and reader UI.

### Phase 3
Search, bookmarks, reading history, themes, OCR and text-to-speech.

### Phase 4
AI summarization, explanation, translation, and document Q&A.

### Phase 5
RAG and multi-document knowledge search.

### Phase 6
Windows accessibility/UI Automation and "read selected screen content".
