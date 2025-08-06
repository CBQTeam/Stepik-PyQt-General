import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


# Двигатель, который можно включить/выключить.
# В зависимости от этого испустит сигнал started или stopped
class Engine(QObject):
    started: pyqtSignal = pyqtSignal(bool)
    stopped: pyqtSignal = pyqtSignal(bool)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.state = False

    def setEngineControl(self, on: bool) -> None:
        if on:
            self.start()
        else:
            self.stop()

    def start(self):
        self.state = True
        self.started.emit(self.state)

    def stop(self):
        self.state = False
        self.stopped.emit(self.state)


# Машина, в которой имитируем работу ключа зажигания
class Car(QObject):
    ignition_key: pyqtSignal = pyqtSignal(bool)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self.on = False

    def setIgnitionKey(self, on: bool) -> None:
        self.on = on
        self.ignition_key.emit(self.on)


# Слот, который задаёт текст на надписи
def setStatus(status: bool):
    match status:
        case True:
            statusLbl.setText("Двигатель запущен")
        case False:
            statusLbl.setText("Двигатель заглушен")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаём главное окно
    widget = QWidget()
    widget.setWindowTitle("Машина")
    widget.setFixedSize(300, 100)
    widget.show()

    # Создаём интерфейс
    startBtn = QPushButton("Старт", widget)
    stopBtn = QPushButton("Стоп", widget)
    statusLbl = QLabel(widget)

    layout = QVBoxLayout(widget)
    layout.addWidget(statusLbl)
    layout.addWidget(startBtn)
    layout.addWidget(stopBtn)

    # Создаём собственные объекты
    car = Car()
    engine = Engine()

    # Связываем ключ зажигания с двигателем
    car.ignition_key.connect(engine.setEngineControl)

    # Связываем статус двигателя с текстовой меткой
    engine.started.connect(setStatus)
    engine.stopped.connect(setStatus)

    # Связываем действия включения/выключения двигателя через ключ зажигания
    startBtn.clicked.connect(lambda: car.setIgnitionKey(True))
    stopBtn.clicked.connect(lambda: car.setIgnitionKey(False))

    app.exec()
