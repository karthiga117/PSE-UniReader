"""PSE Universal Reader - application entry point."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow

from services.document_service import DocumentService
from services.reader_factory import ReaderFactory
from ui.reader_widget import ReaderWidget
from utils.logger import get_logger


class MainWindow(QMainWindow):
    """Main application window for opening and viewing documents."""

    def __init__(self) -> None:
        super().__init__()
        self.logger = get_logger()
        self.document_service = DocumentService(ReaderFactory())
        self.setWindowTitle("PSE Universal Reader")
        self.resize(1000, 700)

        self.reader_widget = ReaderWidget()
        self.setCentralWidget(self.reader_widget)

        self._build_menu()
        self.logger.info("Application startup complete.")

    def _build_menu(self) -> None:
        """Create the main file menu."""
        self.menuBar().setNativeMenuBar(False)
        file_menu = self.menuBar().addMenu("File")
        open_action = file_menu.addAction("Open File")
        open_action.triggered.connect(self.open_file)

    def open_file(self) -> None:
        """Open a supported document and display it in the UI."""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Document",
            "",
            "PDF (*.pdf);;Word (*.docx);;Excel (*.xlsx);;Text (*.txt);;All Supported Files (*.pdf *.docx *.xlsx *.txt)",
        )

        if not file_name:
            return

        try:
            self.logger.info("Document opening started: %s", file_name)
            document = self.document_service.open(file_name)
            self.logger.info("Document extracted successfully: %s", document.title)
            self.reader_widget.show_document(document)
        except Exception as exc:  # pragma: no cover - UI-level fallback
            self.logger.exception("Failed to open document: %s", file_name)
            self._show_error(exc)

    def _show_error(self, exc: Exception) -> None:
        """Present a friendly, non-technical error message to the user."""
        message = str(exc)
        if "Unsupported file format" in message:
            text = "Unsupported file format.\n\nPSE Universal Reader currently supports: PDF, Word, Excel and Text."
        else:
            text = "Unable to read this document.\n\nPlease verify that the file is valid and try again."

        QMessageBox.critical(self, "Reader Error", text)


def main() -> None:
    """Start the application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
