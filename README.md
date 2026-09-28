# PSE Universal Reader

A Windows desktop application built with Python and PySide6 that provides a single reading interface for multiple content types.

## Project Status

**Phase 1 — Foundation**

Initial project setup. The first goal is to create a clean architecture that can read:

- PDF
- Microsoft Word (`.docx`)
- Microsoft Excel (`.xlsx`)
- Web pages
- Plain text (`.txt`)
- Markdown (`.md`)

Future phases may add text-to-speech, OCR, AI document Q&A, RAG, and Windows accessibility integration.

## Technology

- Python 3.12+
- PySide6
- PyMuPDF
- python-docx
- openpyxl
- requests
- BeautifulSoup4
- pytest

## Initial Architecture

```text
pse-universal-reader/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── readers/
├── models/
├── services/
├── ui/
├── utils/
│
├── tests/
│
├── examples/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## First Milestone

The first milestone is intentionally small:

1. Create the Python application entry point.
2. Launch a PySide6 Windows window.
3. Display the application name.
4. Keep the structure ready for document readers.

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

Run:

```bash
python -m app.main
```

## Roadmap

### Phase 1
Multi-format local/web reading foundation.

### Phase 2
Search, bookmarks, reading history, themes, OCR and text-to-speech.

### Phase 3
AI summarization, explanation, translation and document Q&A.

### Phase 4
RAG and multi-document knowledge search.

### Phase 5
Windows accessibility/UI Automation and "read selected screen content".

## Design Principle

The UI should never contain document-format-specific parsing logic.

Each reader should convert its source into a common document representation so that future features such as search, AI and RAG can work independently of the original file type.
