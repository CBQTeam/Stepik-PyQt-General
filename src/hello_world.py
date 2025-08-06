import sys

# Импорт основных классов
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    # Создание основного приложения
    app = QApplication(sys.argv)

    # Создание основного окна
    widget = QWidget()
    widget.setWindowTitle("Привет мир!")
    widget.setFixedSize(300, 100)

    # Создание текстовой надписи
    label = QLabel("", widget)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Создание кнопки и связывание с текстовой надписью
    button = QPushButton("Нажми на меня", widget)
    button.clicked.connect(lambda: label.setText("Привет мир!"))

    # Настройка сетки
    layout = QVBoxLayout(widget)
    layout.addWidget(label)
    layout.addWidget(button)

    # Отображение основного окна
    widget.show()

    # Запуск событийного цикла
    app.exec()
