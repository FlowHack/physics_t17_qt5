from PyQt5 import QtGui, QtWidgets
from bin.MainWindowUI import Ui_MainWindow
from bin import MessageBox
from functions.calculations import splitting_number
from settings import path_to_icos, LOGGER
from functions import (set_validator_double, all_edits, calculate_experiment,
                       calculate_phenomen, OpenGlWindow)


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.logger = LOGGER('master', 'app')
        self.logger.info('Получаю UI главного окна')
        self.ui = Ui_MainWindow()
        self.logger.info('Загружаю UI главного окна')
        self.ui.setupUi(self)
        self.edits = all_edits(self.ui)
        self.logger.info('initialize_ui')
        self.initialize_ui()

    def initialize_ui(self):
        self.logger.info('Добавление иконки к приложению')
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(path_to_icos['app_ico']),
            QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.setWindowIcon(icon)
        self.ui.frame_1.setVisible(False)

        self.logger.info('Установка валидаторов')
        set_validator_double(list(self.edits.values()))
        self.logger.info('Подключение функций к кнопкам')
        self.ui.btn_simulation.clicked.connect(self.simulation)
        self.ui.btn_restart.clicked.connect(self.clear)

        self.logger.warning('Установка окна по центру')
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        qt_rectangle = self.frameGeometry()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def simulation(self):
        rad_exp = self.ui.rad_simulation_exp.isChecked()

        if rad_exp:
            try:
                p_ball =  \
                    float(
                        self.edits[
                            'edit_abs_ball_density'
                        ].text().replace(',', '.')
                    )
                p_water =  \
                    float(
                        self.edits[
                            'edit_abs_liquid_density'
                        ].text().replace(',', '.')
                    )
                height =  \
                    float(
                        self.edits['edit_abs_height'].text().replace(',', '.')
                    ) / 10 / 100
                radius =  \
                    float(
                        self.edits[
                            'edit_abs_diameter'
                        ].text().replace(',', '.')
                    ) / 10 / 100 / 2
                viscosity = float(
                    self.edits['edit_abs_viscosity'].text().replace(',', '.')
                )
            except ValueError:
                MessageBox(
                    title='Ошибка', text='Ошибка в значениях',
                    msg='Неверные значения для эксперимента'
                ).showerror()
                return

            res_experiment = calculate_experiment(
                p_ball=p_ball, p_water=p_water, radius=radius,
                height=height, abs_viscosity=viscosity
            )

            if res_experiment is None:
                return
            if height > 0.57:
                MessageBox(
                    title='Неверное значение',
                    text='НЕверное значение высоты',
                    msg='Максимальная высота пробирки, которую можно указать '
                        '550мм'
                ).showwarning()

            height_for_simulation = int(round(height * 100, 0))
            time_step = res_experiment['avg_time']

            if time_step < 12:
                steps = range(height_for_simulation + 1)[::-1]
                count_steps = len(steps)
            else:
                steps, count_steps = splitting_number(height_for_simulation)

            time_step = time_step / count_steps * 1000000000

            OpenGlWindow(
                numbers=steps, time=time_step, count_simulations=3
            )

            self.ui.edit_viscosity_1.setText(str(res_experiment['viscosity1']))
            self.ui.edit_viscosity_2.setText(str(res_experiment['viscosity2']))
            self.ui.edit_viscosity_3.setText(str(res_experiment['viscosity3']))
            self.ui.edit_viscosity_average.setText(
                str(res_experiment['viscosity'])
            )
            self.ui.edit_passed_height_1.setText(str(res_experiment['height']))
            self.ui.edit_passed_height_2.setText(str(res_experiment['height']))
            self.ui.edit_passed_height_3.setText(str(res_experiment['height']))
            self.ui.edit_passed_height_average.setText(
                str(res_experiment['height'])
            )
            self.ui.edit_passage_time_1.setText(str(res_experiment['time1']))
            self.ui.edit_passage_time_2.setText(str(res_experiment['time2']))
            self.ui.edit_passage_time_3.setText(str(res_experiment['time3']))
            self.ui.edit_passage_time_average.setText(
                str(res_experiment['avg_time'])
            )
            self.ui.edit_radius_of_the_ball_1.setText(
                str(res_experiment['radius'])
            )
            self.ui.edit_radius_of_the_ball_2.setText(
                str(res_experiment['radius'])
            )
            self.ui.edit_radius_of_the_ball_3.setText(
                str(res_experiment['radius'])
            )
            self.ui.edit_radius_of_the_ball_average.setText(
                str(res_experiment['radius'])
            )
        else:
            try:
                p_ball =  \
                    float(
                        self.edits[
                            'edit_ball_density'
                        ].text().replace(',', '.')
                    )
                p_water =  \
                    float(
                        self.edits[
                            'edit_liquid_density'
                        ].text().replace(',', '.')
                    )
                radius =  \
                    float(
                        self.edits[
                            'edit_diameter_ball'
                        ].text().replace(',', '.')
                    ) / 10 / 100 / 2
                viscosity =  \
                    float(
                        self.edits[
                            'edit_dynamic_viscosity_coeff'
                        ].text().replace(',', '.')
                    )
            except ValueError:
                MessageBox(
                    title='Ошибка', text='Ошибка в значениях',
                    msg='Неверные значения для симуляции'
                ).showerror()
                return

            res_phenomen = calculate_phenomen(
                radius=radius, p_ball=p_ball, p_water=p_water,
                viscosity=viscosity
            )
            if res_phenomen['time'] is None:
                return

            height_for_simulation = 55
            time_step = res_phenomen['time']

            if time_step < 12:
                steps = range(height_for_simulation + 1)[::-1]
                count_steps = len(steps)
            else:
                steps, count_steps = splitting_number(height_for_simulation)

            time_step = time_step / count_steps * 1000000000

            OpenGlWindow(numbers=steps, time=time_step)

    def clear(self):
        for edit in self.edits.values():
            edit.setText('')
