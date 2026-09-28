"""PySide6 widget for displaying a normalized document."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QTextBrowser, QVBoxLayout, QWidget

from models.document import Document


class ReaderWidget(QWidget):
    """Display document metadata and content in a read-only browser."""

    def __init__(self) -> None:
        super().__init__()
        self.title_label = QLabel("")
        self.type_label = QLabel("")
        self.content_browser = QTextBrowser()
        self.content_browser.setReadOnly(True)
        self.content_browser.setPlaceholderText("Open a document to view its content.")

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.type_label)
        layout.addWidget(self.content_browser)

    def show_document(self, document: Document) -> None:
        """Render a normalized document in the widget."""
        self.title_label.setText(f"Title: {document.title}")
        self.type_label.setText(f"Type: {document.document_type}")
        self.content_browser.setPlainText(document.content or "No content available.")
