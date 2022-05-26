from os import listdir, system
from os.path import join as path_join

from .paths import path_to_bin_dir, path_to_ui_dir, path_py


def check_ui_in_py(LOGGER):
    logger = LOGGER('ui_in_py', 'main')
    logger.info('Начинаю проверку наличия py файлов')

    for item in list(path_py.keys()):
        name = item + 'UI.py'

        if name not in listdir(path_to_bin_dir):
            logger.warning('Файлы не найдены, запускаю конвертацию.')
            convert_ui_in_py(logger)
            break

    logger.info('Все файлы найдены!')


def convert_ui_in_py(logger):
    logger.info('Прохожусь по имеющимя файлам!')
    for item in listdir(path_to_ui_dir):
        name = item.split('.')[0] + 'UI.py'
        ui_path = path_join(path_to_ui_dir, item)
        py_path = path_join(path_to_bin_dir, name)

        logger.info(f'Начинаю конвертацию: {name=}; {ui_path=}; {py_path=}.')
        system(f'pyuic5 {ui_path} -o {py_path}')
