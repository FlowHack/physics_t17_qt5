from os.path import join as path_join
from os import listdir
from settings import path_app_win, path, LOGGER
from bin import MessageBox
from PyQt5.QtGui import QDoubleValidator


def create_shortcut_win(need=False):
    """Функция создания ярлыка для Windows

    Args:
        need (bool, optional): Переменная True, если запущена пользователем
            и False, если автоматически. Defaults to False.
    """

    import winshell
    from win32com.client import Dispatch

    logger = LOGGER('link_windows', 'main')
    logger.info(f'Функция создания ярлыка запущена с переменной {need=}')

    desktop = winshell.desktop()
    if 'CoeffDynamicViscosity.lnk' in listdir(desktop):
        logger.info('Ярлык уже имеется, завершаю.')
        MessageBox(
            'Ярлык уже создан', 'Ярлык уже есть',
            'Ярлык уже имеется на рабочем столе.'
        ).showinfo()
        return

    logger.info('Создаю переменные для ярлыка')
    path_desktop = path_join(desktop, 'CoeffDynamicViscosity.lnk')
    target = path_app_win
    wDir = path
    icon = path_app_win

    logger.warning('Получаю командную строку')
    shell = Dispatch('WScript.Shell')
    logger.warning('Создаю ярлык')
    shortcut = shell.CreateShortCut(path_desktop)

    logger.info('Заполняю ярлык данными')
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon

    logger.warning('Сохраняю ярлык')
    shortcut.save()

    logger.info('Ярлык удачно создан!')
    if need:
        MessageBox('Удачно', 'Удачно!', 'Ярлык удачно создан!').showinfo()


def set_validator_double(edits):
    for edit in edits:
        edit.setValidator(
            QDoubleValidator(-10000000000.00, 10000000000.00, 1000000)
        )
