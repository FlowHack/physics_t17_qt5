from genericpath import isfile
from json import dump
from os import getcwd, listdir, mkdir
from os.path import join as path_join

from .variables import DEFAULT_SETTINGS

path = getcwd()
path_app_win = path_join(path, 'CoeffDynamicViscosity.exe')
path_to_settings_dir = path_join(path, 'settings')
path_to_settings = path_join(path_to_settings_dir, 'settings.json')
path_to_bin_dir = path_join(path, 'bin')
path_to_ui_dir = path_join(path_to_bin_dir, 'UI')
path_to_icos_dir = path_join(path_to_bin_dir, 'icos')
path_ui = {
    'MainWindow': path_join(path_to_ui_dir, 'MainWindow.ui'),
}
path_py = {
    'MainWindow': path_join(path_to_bin_dir, 'MainWindowUI.py'),
}
path_to_icos = {
    'preview': path_join(path_to_icos_dir, 'preview.png'),
    'app_ico': path_join(path_to_icos_dir, 'app_ico.png')
}
path_to_logs_dir = path_join(path_to_settings_dir, 'logs')

if 'logs' not in listdir(path_to_settings_dir):
    mkdir(path_to_logs_dir)
if not isfile(path_to_settings):
    with open(path_to_settings, 'w', encoding='utf-8') as file:
        dump(DEFAULT_SETTINGS, file)
