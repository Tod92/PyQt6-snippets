"""
https://www.pythontutorial.net/pyqt/pyqt-qhboxlayout/
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # add a spacer
        # layout.addStretch()

        # create buttons and add them to the layout
        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # add a spacer
        layout.setSpacing(5)
        # setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None
        layout.setContentsMargins(50, 50, 50, 50)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())