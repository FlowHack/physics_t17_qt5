from logging import INFO, Formatter, getLogger
from logging.handlers import RotatingFileHandler
from os.path import join as path_join
from json import dump, load

from .paths import path_to_logs_dir, path_to_settings


def __get_logger__(name: str, file: str) -> object:
    """Функция создания логгера

    Args:
        name (str): Имя записи
        file (str): Путь до файла

    Returns:
        object: Объект логгер
    """

    logger_format = ('[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s')
    formatter = Formatter(fmt=logger_format, datefmt='%Y-%m-%d %H:%M:%S')

    handler = RotatingFileHandler(
        path_join(path_to_logs_dir, f'{file}.log'),
        maxBytes=5252880,
        backupCount=5,
    )
    handler.setFormatter(formatter)

    file_logger = getLogger(name)
    file_logger.setLevel(INFO)
    file_logger.addHandler(handler)

    return file_logger


LOGGER = __get_logger__


def get_settings():
    with open(path_to_settings, 'r', encoding='utf-8') as file:
        settings_json = load(file)

    return settings_json


def write_settings(data):
    with open(path_to_settings, 'w', encoding='utf-8') as file:
        dump(data, file)
