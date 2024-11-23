"""
https://www.pythontutorial.net/pyqt/pyqt-signals-slots/

sender_object.signal_name.connect(receiver_object.slot_name)

"""
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('Qt Signals & Slots')

        # create a button widget and connect its clicked signal
        # to a method
        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)

        # create widgets
        label = QLabel()
        # using kwarg instead of line_edit.textChanged.connect(label.setText)
        line_edit = QLineEdit(textChanged=label.setText)

        # place the buton on window using a vertical box layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(line_edit)
        layout.addWidget(label)

        self.setLayout(layout)


        # show the window
        self.show()

    def button_clicked(self):
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())