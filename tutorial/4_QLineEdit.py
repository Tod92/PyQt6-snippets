"""
https://www.pythontutorial.net/pyqt/pyqt-qlineedit/
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QCompleter
)

SIMPSONS= [
    'bart',
    'lisa',
    'omer',
    'marge',
    'marcel'
]

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        search_box = QLineEdit(
            self,
            placeholderText='Enter a keyword to search...',
            clearButtonEnabled=True
        )

        password = QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)
        simpson = QLineEdit(self)
        simpson.setCompleter(QCompleter(SIMPSONS))

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(search_box)
        layout.addWidget(password)
        layout.addWidget(simpson)
        
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())