"""
https://www.pythontutorial.net/pyqt/pyqt-qcheckbox/
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # create a checkbox
        self.checkbox = QCheckBox('I agree', self)

        check_button = QPushButton('Check', self)
        check_button.clicked.connect(self.check)

        uncheck_button = QPushButton('Uncheck', self)
        uncheck_button.clicked.connect(self.uncheck)
        
        # tristate checkbox
        self.tristate_checkbox = QCheckBox('TriState', self)
        self.tristate_checkbox.setTristate(True)
        self.tristate_checkbox.stateChanged.connect(self.showState)
        
        layout.addWidget(self.checkbox, 0, 0,
                         Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(check_button, 1, 0)
        layout.addWidget(uncheck_button, 1, 1)


        layout.addWidget(self.tristate_checkbox, 2, 0, Qt.AlignmentFlag.AlignCenter)

        # show the window
        self.show()

    def check(self):
        self.checkbox.setChecked(True)

    def uncheck(self):
        self.checkbox.setChecked(False)

    def showState(self, state):
        print(state)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())