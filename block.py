from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Import QUrl from QtCore module

import sys

class BlocklyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Blockly in PyQt")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.load_blockly()

    def load_blockly(self):
        # Load Blockly HTML in the web browser component
        self.browser.setUrl(QUrl("file:///C:/Users/iansa/Desktop/project-lexus/block.html"))  # Corrected QUrl usage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlocklyWindow()
    window.show()
    sys.exit(app.exec_())
