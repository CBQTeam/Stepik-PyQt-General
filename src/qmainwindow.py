import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QAction,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание главного окна
    main = QMainWindow()
    main.setWindowTitle("Главное окно")
    main.setFixedSize(500, 500)

    # Создание меню
    menuBar = main.menuBar()
    mainMenu = menuBar.addMenu("Главная")

    # Создание действия для выхода
    acitonExit = QAction("Выход", main)
    acitonExit.triggered.connect(lambda: app.quit())
    mainMenu.addAction(acitonExit)

    # Создание меню "О программе"
    aboutMenu = menuBar.addMenu("О программе")
    aboutQtAction = QAction("О Qt", main)
    aboutQtAction.triggered.connect(lambda: app.aboutQt())
    aboutMenu.addAction(aboutQtAction)

    # Создание строки статуса
    status = main.statusBar()
    status.showMessage("Привет мир", 100000000)

    # Создание панели инструментов
    toolbar = main.addToolBar("Основная панель инструментов")
    toolbar.addAction(acitonExit)
    toolbar.addSeparator()
    toolbar.addAction(aboutQtAction)

    main.show()

    app.exec()
