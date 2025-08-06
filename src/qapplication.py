import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget()
    widget.show()

    print(f"Application PID: {app.applicationPid()}")
    print(f"Application dir path: {app.applicationDirPath()}")
    print(f"Application file path: {app.applicationFilePath()}")
    print(f"Application name: {app.applicationName()}")
    print(f"Application version: {app.applicationVersion()}")

    app.exec()
