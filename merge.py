import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BlocklyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blockly Integration with PyQt5")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_blockly_workspace()

    def load_blockly_workspace(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Blockly Workspace</title>
            <script src="https://unpkg.com/blockly/blockly.min.js"></script>
            <script src="https://unpkg.com/blockly/blocks_compressed.js"></script>
            <script src="https://unpkg.com/blockly/python_compressed.js"></script>
        </head>
        <body>
            <div id="blocklyDiv" style="height: 100%;"></div>
            <script>
                var workspace = Blockly.inject('blocklyDiv', {
                    toolbox: document.getElementById('toolbox'),
                });
            </script>
            <xml id="toolbox" style="display: none">
                <block type="controls_repeat_ext"></block>
                <block type="math_number"></block>
                <block type="text"></block>
            </xml>
        </body>
        </html>
        """
        self.web_view.setHtml(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlocklyWindow()
    window.show()
    sys.exit(app.exec_())
