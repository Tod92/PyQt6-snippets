"""
https://www.pythontutorial.net/pyqt/pyqt-qpushbutton/
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton('Click Me')
        button_delete = QPushButton('Delete')
        icon = QIcon('trash.png')
        button_delete.setIcon(icon)
        button_toggle = QPushButton('Toggle Me')
        button_toggle.setCheckable(True)
        button_toggle.clicked.connect(self.on_toggle)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button_delete)
        layout.addWidget(button_toggle)
        self.setLayout(layout)
        
        # show the window
        self.show()


    def on_toggle(self, checked):
        print(checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())