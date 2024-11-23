"""
https://www.pythontutorial.net/pyqt/pyqt-qlabel/

"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QMovie


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)

        # create QLabel widgets
        label = QLabel('This is a QLabel widget')
        label_img = QLabel()
        pixmap = QPixmap('logo.png')
        label_img.setPixmap(pixmap)
        label_gif = QLabel()
        movie = QMovie('light.gif')
        label_gif.setMovie(movie)
        movie.start()
        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label_img)
        layout.addWidget(label_gif)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())