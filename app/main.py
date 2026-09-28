"""PSE Universal Reader - application entry point."""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PSE Universal Reader")
        self.resize(1000, 700)

        label = QLabel("PSE Universal Reader\n\nPhase 1 - Foundation")
        label.setStyleSheet(
            "font-size: 24px; padding: 40px;"
        )
        self.setCentralWidget(label)


def main() -> None:
    """Start the application."""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
