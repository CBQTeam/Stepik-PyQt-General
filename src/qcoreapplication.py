import sys
import time

from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal


class Task(QObject):
    # Создаём сигнал
    signal_finished = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    def run(self):

        # Выводим сообщения на экран, имитируя работу
        print("Do something")
        time.sleep(5)
        print("Finished")

        # Испускаем сигнал об окончании работы
        self.signal_finished.emit()


if __name__ == "__main__":
    # Создаём экземпляр неграфического приложения
    app = QCoreApplication(sys.argv)

    # Создаём задачу
    task = Task()

    # Связываем со слотом quit(), чтобы приложение завершилось
    task.signal_finished.connect(app.quit)

    # Запускаем задачу
    task.run()
