
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from .version import __version__
from .updater import check_for_updates

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"ntt-demo {__version__}")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel(f"Current version: {__version__}")
        self.layout.addWidget(self.label)
        self.update_button = QPushButton("Check for Updates")
        self.update_button.clicked.connect(self.check_updates)
        self.layout.addWidget(self.update_button)

    def check_updates(self):
        check_for_updates(self)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
