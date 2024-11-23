"""
https://www.pythontutorial.net/pyqt/pyqt-qvboxlayout/
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QVBoxLayout')

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create buttons
        label_1 = QLabel()
        label_1.setStyleSheet('QLabel{background-color:red}')
        label_2 = QLabel()
        label_2.setStyleSheet('QLabel{background-color:green}')
        label_3 = QLabel()
        label_3.setStyleSheet('QLabel{background-color:blue}')

        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)

        layout.setStretchFactor(label_1, 1)
        layout.setStretchFactor(label_2, 2)
        layout.setStretchFactor(label_3, 3)
        
        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())