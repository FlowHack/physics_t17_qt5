#!/bin/bash

file="$PWD/venv"
path=$PWD
path_to_ico="$PWD/bin/icos/app_ico.ico"
open_file="$PWD/CoeffDynamicViscosity.sh"
open_application="$PWD/CoeffDynamicViscosity.py"

if [ -d $file ]; then
	$PWD/venv/bin/python3 CoeffDynamicViscosity.py
else
	echo "!!!!!Обновление python3 до актуальной версии!!!!!"
	sudo apt reinstall python3 -y

	echo "!!!!!Установка python3-venv!!!!!"
	sudo apt install python3-venv -y

	echo "!!!!!Установка python3-pip!!!!!"
	sudo apt install python3-pip -y
	
	echo "!!!!!Установка поддержки OpenGL!!!!!"
	sudo apt-get install freeglut3-dev

	echo "!!!!!Создание виртуального окружения!!!!!"
	python3 -m venv venv
	source "$PWD/venv/bin/activate"
	echo "!!!!!Установка зависимостей!!!!!"
	pip3 install wheel
	pip3 install -r requirements.txt

	echo "!!!!!Добавление программы в список программ !!!!!"
	cd /usr/share/applications/
	sudo touch CoeffDynamicViscosity.desktop  
	echo "[Desktop Entry]
Name=CoeffDynamicViscosity
Comment=Программа для определения коэффициента вязкости методом Стокса
Exec=sh $open_file
Terminal=false
Type=Application
Icon=$path_to_ico
Path=$path
Categories=System" | sudo tee CoeffDynamicViscosity.desktop

	echo "!!!!!Запуск программы!!!!!"
	cd $path
	python3 $open_application
fi