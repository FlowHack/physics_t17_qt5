from re import I
from PyQt5 import QtGui, QtWidgets
from bin.MainWindowUI import Ui_MainWindow
from settings import path_to_icos, LOGGER
from functions import (set_validator_double, all_edits, calculate_experiment,
                       calculate_phenomen, OpenGLDraw)
from time import sleep


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

        OpenGLDraw(self.ui.openGL_container)

        set_validator_double(list(self.edits.values()))
        self.ui.btn_simulation.clicked.connect(self.simulation)

    def simulation(self):
        rad_exp = self.ui.rad_simulation_exp.isChecked()

        if rad_exp:
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
                    self.edits['edit_abs_diameter'].text().replace(',', '.')
                ) / 10 / 100 / 2
            viscosity = float(
                self.edits['edit_abs_viscosity'].text().replace(',', '.')
            )

            res_experiment = calculate_experiment(
                p_ball=p_ball, p_water=p_water, radius=radius,
                height=height, abs_viscosity=viscosity
            )

            if res_experiment is None:
                return

            self.ui.openGL_container.clearMask()

            OpenGLDraw(
                widget=self.ui.openGL_container,
                height=55, need_ball=True
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
            p_ball =  \
                float(self.edits['edit_ball_density'].text().replace(',', '.'))
            p_water =  \
                float(
                    self.edits['edit_liquid_density'].text().replace(',', '.')
                )
            radius =  \
                float(
                    self.edits['edit_diameter_ball'].text().replace(',', '.')
                ) / 10 / 100 / 2
            viscosity =  \
                float(
                    self.edits[
                        'edit_dynamic_viscosity_coeff'
                    ].text().replace(',', '.')
                )

            res_phenomen = calculate_phenomen(
                radius=radius, p_ball=p_ball, p_water=p_water,
                viscosity=viscosity
            )

            if res_phenomen['time'] is None:
                return
