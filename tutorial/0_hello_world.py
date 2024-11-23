"""
https://www.pythontutorial.net/pyqt/pyqt-hello-world/
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget


# create the QApplication
app = QApplication(sys.argv)

# create the main window
window = QWidget(windowTitle='Hello World')
window.show()

# start the event loop
sys.exit(app.exec())