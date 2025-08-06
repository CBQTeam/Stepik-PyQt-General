import sys

from PyQt5.QtGui import QGuiApplication, QWindow

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    window = QWindow()
    window.show()

    app.exec()
