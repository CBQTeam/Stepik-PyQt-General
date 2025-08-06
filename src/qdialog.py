import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание основного окна приложения
    widget = QWidget()
    widget.setWindowTitle("Главное окно")
    widget.setFixedSize(300, 300)
    openDialog = QPushButton("Открыть диалог", widget)

    # Разметка окна приложения
    widgetLayout = QVBoxLayout(widget)
    widgetLayout.addWidget(openDialog)

    # Создание диалогового окна и текстовой метки
    dialog = QDialog(widget)
    dialog.setWindowTitle("Диалоговое окно")
    dialog.setFixedSize(150, 150)
    helloLabel = QLabel("Привет мир", dialog)

    # Разметка виджетов на диалоговом окне
    dialogLayout = QVBoxLayout(widget)
    dialogLayout.addWidget(helloLabel)
    dialog.setLayout(dialogLayout)

    # Связывание нажатия кнопки и открытия диалогово окна
    openDialog.clicked.connect(lambda: dialog.exec())

    widget.setLayout(widgetLayout)
    widget.show()

    app.exec()
