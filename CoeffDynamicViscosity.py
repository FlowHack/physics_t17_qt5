from settings import (LOGGER, check_ui_in_py, path_to_icos, get_settings,
                      write_settings)
from tracemalloc import get_traced_memory
from tracemalloc import start as trace_start
from sys import platform as sys_platform
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import gc
from master_windows import App
from sys import exit as exit_ex


class StartApp:
    def __init__(self):
        self.logger = LOGGER('start_app', 'main')
        self.logger.info('Получаю настройки программы')
        self.settings = get_settings()

        self.logger.info('Запускаю превью')
        self.app = QtWidgets.QApplication([])
        self.logger.info('Создаю preview pixmap')
        self.pixmap = self.create_pixmap()
        self.logger.info('Создаю превью')
        self.create_splash()

        self.logger.info('Создаю задачу для sheduler')
        self.start_scheduler()
        self.splash_text_progress(20)
        sleep(0.5)

        if int(self.settings['first_start']) == 1:
            self.logger.info('Первый запуск программы, создаю ярлык!')

            if sys_platform == 'win32':
                self.logger.warning(
                    f'{sys_platform=}. Создаю ярлык для windows'
                )
                from functions import create_shortcut_win
                create_shortcut_win()

            self.logger.warning('Записываю в настройки first_start = 0')
            self.settings['first_start'] = 0
            write_settings(self.settings)
        self.splash_text_progress(50)
        sleep(0.5)

        self.logger.warning('Создаю окно')
        master = App()
        self.splash_text_progress(80)
        sleep(0.5)
        self.logger.warning('Показываю окно')
        master.show()
        sleep(0.5)
        self.splash_text_progress(100)
        self.splash.finish(master)

        exit_ex(self.app.exec())

    @staticmethod
    def sheduler() -> None:
        """Функция отвечает за сброс мусора
        """

        scheduler_logger = LOGGER('scheduler', 'sheduler')
        size_last, size_peak = get_traced_memory()
        size_last = size_last // 1024

        scheduler_logger.warning(f'Запускаю очситку мусора. {size_last=}')
        gc.collect()

        size_now, size_peak = get_traced_memory()
        size_now = size_now // 1024
        size_peak = size_peak // 1024
        scheduler_logger.warning(
            f'Использовалось: {size_last}Mib, Теперь: {size_now}Mib, '
            f'В пике: {size_peak}Mib'
        )

    def start_scheduler(self):
        """Функция запуска фонового процесса отслеживания заполненности памяти
        """

        trace_start()
        scheduler = QtCore.QTimer()
        scheduler.timeout.connect(self.sheduler)
        scheduler.start(3000)

    def create_pixmap(self):
        pixmap = QtGui.QPixmap(path_to_icos['preview'])
        pixmap.fill(QtCore.Qt.transparent)
        w = pixmap.size().width()
        h = pixmap.size().height()

        clipPath = QtGui.QPainterPath()
        clipPath.addRoundedRect(QtCore.QRectF(0, 0, w, h), w//6, h//6)

        qp = QtGui.QPainter(pixmap)
        qp.setClipPath(clipPath)
        qp.drawPixmap(0, 0, QtGui.QPixmap(path_to_icos['preview']))
        qp.end()

        return pixmap

    def splash_text_progress(self, progress):
        """Создание текста со статусом загрузки preview

        Args:
            progress (_type_): Прогресс от 0 до 100
        """

        self.splash.showMessage(
            f'Загрузка данных...{progress}%',
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black
        )

    def create_splash(self, progress=0):
        """Функция создания и обновления preview перед запуском программы

        Args:
            progress (int, optional): Прогресс от 0 до 100. Defaults to 0.
        """

        self.splash = QtWidgets.QSplashScreen(self.pixmap)
        self.splash.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.splash_text_progress(progress)
        self.splash.show()
        QtWidgets.qApp.processEvents()


if __name__ == '__main__':
    check_ui_in_py(LOGGER)

    LOGGER('platform', 'main').info(f'Запуск на платформе: {sys_platform}')
    StartApp()
