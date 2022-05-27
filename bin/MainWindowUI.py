# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/flowhack/FlowHack_Linux/Yandex.Disk/proggramming/Python/Dev/physics_t17_qt5/bin/UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(947, 600))
        MainWindow.setMaximumSize(QtCore.QSize(947, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("font: 75 italic 12pt \"Times New Roman\";\n"
"background-color: rgb(230, 230, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(20, 230, 911, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("")
        self.frame_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.edit_passed_height_3 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passed_height_3.setGeometry(QtCore.QRect(540, 120, 171, 31))
        self.edit_passed_height_3.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passed_height_3.setReadOnly(True)
        self.edit_passed_height_3.setObjectName("edit_passed_height_3")
        self.lab_experiment_1 = QtWidgets.QLabel(self.frame_2)
        self.lab_experiment_1.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.lab_experiment_1.setObjectName("lab_experiment_1")
        self.edit_radius_of_the_ball_1 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_radius_of_the_ball_1.setGeometry(QtCore.QRect(730, 40, 171, 31))
        self.edit_radius_of_the_ball_1.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_radius_of_the_ball_1.setMaxLength(32768)
        self.edit_radius_of_the_ball_1.setCursorPosition(0)
        self.edit_radius_of_the_ball_1.setReadOnly(True)
        self.edit_radius_of_the_ball_1.setObjectName("edit_radius_of_the_ball_1")
        self.lab_viscosity = QtWidgets.QLabel(self.frame_2)
        self.lab_viscosity.setGeometry(QtCore.QRect(340, 10, 191, 16))
        self.lab_viscosity.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_viscosity.setObjectName("lab_viscosity")
        self.edit_radius_of_the_ball_2 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_radius_of_the_ball_2.setGeometry(QtCore.QRect(730, 80, 171, 31))
        self.edit_radius_of_the_ball_2.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_radius_of_the_ball_2.setReadOnly(True)
        self.edit_radius_of_the_ball_2.setObjectName("edit_radius_of_the_ball_2")
        self.edit_viscosity_2 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_viscosity_2.setGeometry(QtCore.QRect(350, 80, 171, 31))
        self.edit_viscosity_2.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_viscosity_2.setReadOnly(True)
        self.edit_viscosity_2.setObjectName("edit_viscosity_2")
        self.edit_passed_height_1 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passed_height_1.setGeometry(QtCore.QRect(540, 40, 171, 31))
        self.edit_passed_height_1.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passed_height_1.setReadOnly(True)
        self.edit_passed_height_1.setObjectName("edit_passed_height_1")
        self.edit_passage_time_3 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passage_time_3.setGeometry(QtCore.QRect(160, 120, 171, 31))
        self.edit_passage_time_3.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passage_time_3.setReadOnly(True)
        self.edit_passage_time_3.setObjectName("edit_passage_time_3")
        self.lab_radius_of_the_ball = QtWidgets.QLabel(self.frame_2)
        self.lab_radius_of_the_ball.setGeometry(QtCore.QRect(730, 10, 171, 16))
        self.lab_radius_of_the_ball.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_radius_of_the_ball.setObjectName("lab_radius_of_the_ball")
        self.edit_viscosity_1 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_viscosity_1.setGeometry(QtCore.QRect(350, 40, 171, 31))
        self.edit_viscosity_1.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_viscosity_1.setReadOnly(True)
        self.edit_viscosity_1.setObjectName("edit_viscosity_1")
        self.edit_viscosity_3 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_viscosity_3.setGeometry(QtCore.QRect(350, 120, 171, 31))
        self.edit_viscosity_3.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_viscosity_3.setReadOnly(True)
        self.edit_viscosity_3.setObjectName("edit_viscosity_3")
        self.edit_passage_time_2 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passage_time_2.setGeometry(QtCore.QRect(160, 80, 171, 31))
        self.edit_passage_time_2.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passage_time_2.setReadOnly(True)
        self.edit_passage_time_2.setObjectName("edit_passage_time_2")
        self.lab_experiment_3 = QtWidgets.QLabel(self.frame_2)
        self.lab_experiment_3.setGeometry(QtCore.QRect(20, 130, 121, 16))
        self.lab_experiment_3.setObjectName("lab_experiment_3")
        self.edit_passed_height_2 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passed_height_2.setGeometry(QtCore.QRect(540, 80, 171, 31))
        self.edit_passed_height_2.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passed_height_2.setReadOnly(True)
        self.edit_passed_height_2.setObjectName("edit_passed_height_2")
        self.lab_passed_height = QtWidgets.QLabel(self.frame_2)
        self.lab_passed_height.setGeometry(QtCore.QRect(540, 10, 171, 16))
        self.lab_passed_height.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_passed_height.setObjectName("lab_passed_height")
        self.lab_experiment_2 = QtWidgets.QLabel(self.frame_2)
        self.lab_experiment_2.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.lab_experiment_2.setObjectName("lab_experiment_2")
        self.edit_passage_time_1 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passage_time_1.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.edit_passage_time_1.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passage_time_1.setInputMask("")
        self.edit_passage_time_1.setReadOnly(True)
        self.edit_passage_time_1.setObjectName("edit_passage_time_1")
        self.lab_passage_time = QtWidgets.QLabel(self.frame_2)
        self.lab_passage_time.setGeometry(QtCore.QRect(160, 10, 171, 16))
        self.lab_passage_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_passage_time.setObjectName("lab_passage_time")
        self.edit_radius_of_the_ball_3 = QtWidgets.QLineEdit(self.frame_2)
        self.edit_radius_of_the_ball_3.setGeometry(QtCore.QRect(730, 120, 171, 31))
        self.edit_radius_of_the_ball_3.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_radius_of_the_ball_3.setReadOnly(True)
        self.edit_radius_of_the_ball_3.setObjectName("edit_radius_of_the_ball_3")
        self.lab_experiment_average = QtWidgets.QLabel(self.frame_2)
        self.lab_experiment_average.setGeometry(QtCore.QRect(20, 170, 121, 16))
        self.lab_experiment_average.setObjectName("lab_experiment_average")
        self.edit_passage_time_average = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passage_time_average.setGeometry(QtCore.QRect(160, 160, 171, 31))
        self.edit_passage_time_average.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passage_time_average.setReadOnly(True)
        self.edit_passage_time_average.setObjectName("edit_passage_time_average")
        self.edit_viscosity_average = QtWidgets.QLineEdit(self.frame_2)
        self.edit_viscosity_average.setGeometry(QtCore.QRect(350, 160, 171, 31))
        self.edit_viscosity_average.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_viscosity_average.setReadOnly(True)
        self.edit_viscosity_average.setObjectName("edit_viscosity_average")
        self.edit_passed_height_average = QtWidgets.QLineEdit(self.frame_2)
        self.edit_passed_height_average.setGeometry(QtCore.QRect(540, 160, 171, 31))
        self.edit_passed_height_average.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_passed_height_average.setReadOnly(True)
        self.edit_passed_height_average.setObjectName("edit_passed_height_average")
        self.edit_radius_of_the_ball_average = QtWidgets.QLineEdit(self.frame_2)
        self.edit_radius_of_the_ball_average.setGeometry(QtCore.QRect(730, 160, 171, 31))
        self.edit_radius_of_the_ball_average.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_radius_of_the_ball_average.setReadOnly(True)
        self.edit_radius_of_the_ball_average.setObjectName("edit_radius_of_the_ball_average")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(180, 50, 611, 171))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_1.setObjectName("frame_1")
        self.edit_liquid_density = QtWidgets.QLineEdit(self.frame_1)
        self.edit_liquid_density.setGeometry(QtCore.QRect(360, 90, 241, 31))
        self.edit_liquid_density.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_liquid_density.setCursorPosition(0)
        self.edit_liquid_density.setObjectName("edit_liquid_density")
        self.lab_dynamic_viscosity_coeff = QtWidgets.QLabel(self.frame_1)
        self.lab_dynamic_viscosity_coeff.setGeometry(QtCore.QRect(10, 140, 341, 16))
        self.lab_dynamic_viscosity_coeff.setObjectName("lab_dynamic_viscosity_coeff")
        self.lab_liquid_density = QtWidgets.QLabel(self.frame_1)
        self.lab_liquid_density.setGeometry(QtCore.QRect(120, 100, 221, 16))
        self.lab_liquid_density.setStyleSheet("font: 75 italic 12pt \"Times New Roman\";")
        self.lab_liquid_density.setObjectName("lab_liquid_density")
        self.edit_dynamic_viscosity_coeff = QtWidgets.QLineEdit(self.frame_1)
        self.edit_dynamic_viscosity_coeff.setGeometry(QtCore.QRect(360, 130, 241, 31))
        self.edit_dynamic_viscosity_coeff.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_dynamic_viscosity_coeff.setCursorPosition(0)
        self.edit_dynamic_viscosity_coeff.setObjectName("edit_dynamic_viscosity_coeff")
        self.edit_diameter_ball = QtWidgets.QLineEdit(self.frame_1)
        self.edit_diameter_ball.setGeometry(QtCore.QRect(360, 10, 241, 31))
        self.edit_diameter_ball.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_diameter_ball.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.edit_diameter_ball.setCursorPosition(0)
        self.edit_diameter_ball.setObjectName("edit_diameter_ball")
        self.lab_ball_diameter = QtWidgets.QLabel(self.frame_1)
        self.lab_ball_diameter.setGeometry(QtCore.QRect(130, 20, 211, 16))
        self.lab_ball_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ball_diameter.setObjectName("lab_ball_diameter")
        self.edit_ball_density = QtWidgets.QLineEdit(self.frame_1)
        self.edit_ball_density.setGeometry(QtCore.QRect(360, 50, 241, 31))
        self.edit_ball_density.setTabletTracking(False)
        self.edit_ball_density.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.edit_ball_density.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_ball_density.setObjectName("edit_ball_density")
        self.lab_ball_density = QtWidgets.QLabel(self.frame_1)
        self.lab_ball_density.setGeometry(QtCore.QRect(130, 60, 211, 16))
        self.lab_ball_density.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ball_density.setObjectName("lab_ball_density")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 440, 911, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.lab_abs_viscosity = QtWidgets.QLabel(self.frame_3)
        self.lab_abs_viscosity.setGeometry(QtCore.QRect(250, 130, 151, 20))
        self.lab_abs_viscosity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_abs_viscosity.setObjectName("lab_abs_viscosity")
        self.lab_abs_liquid_density = QtWidgets.QLabel(self.frame_3)
        self.lab_abs_liquid_density.setGeometry(QtCore.QRect(10, 90, 231, 20))
        self.lab_abs_liquid_density.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_abs_liquid_density.setObjectName("lab_abs_liquid_density")
        self.lab_abs_radius = QtWidgets.QLabel(self.frame_3)
        self.lab_abs_radius.setGeometry(QtCore.QRect(530, 90, 61, 20))
        self.lab_abs_radius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_abs_radius.setObjectName("lab_abs_radius")
        self.lab_abs_ball_density = QtWidgets.QLabel(self.frame_3)
        self.lab_abs_ball_density.setGeometry(QtCore.QRect(40, 50, 201, 20))
        self.lab_abs_ball_density.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_abs_ball_density.setObjectName("lab_abs_ball_density")
        self.edit_abs_height = QtWidgets.QLineEdit(self.frame_3)
        self.edit_abs_height.setGeometry(QtCore.QRect(600, 40, 241, 31))
        self.edit_abs_height.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_abs_height.setObjectName("edit_abs_height")
        self.edit_abs_ball_density = QtWidgets.QLineEdit(self.frame_3)
        self.edit_abs_ball_density.setGeometry(QtCore.QRect(250, 40, 241, 31))
        self.edit_abs_ball_density.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_abs_ball_density.setObjectName("edit_abs_ball_density")
        self.lab_abs_height = QtWidgets.QLabel(self.frame_3)
        self.lab_abs_height.setGeometry(QtCore.QRect(530, 50, 61, 20))
        self.lab_abs_height.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_abs_height.setObjectName("lab_abs_height")
        self.edit_abs_viscosity = QtWidgets.QLineEdit(self.frame_3)
        self.edit_abs_viscosity.setGeometry(QtCore.QRect(410, 120, 241, 31))
        self.edit_abs_viscosity.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_abs_viscosity.setText("")
        self.edit_abs_viscosity.setObjectName("edit_abs_viscosity")
        self.edit_abs_liquid_density = QtWidgets.QLineEdit(self.frame_3)
        self.edit_abs_liquid_density.setGeometry(QtCore.QRect(250, 80, 241, 31))
        self.edit_abs_liquid_density.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_abs_liquid_density.setObjectName("edit_abs_liquid_density")
        self.edit_abs_diameter = QtWidgets.QLineEdit(self.frame_3)
        self.edit_abs_diameter.setGeometry(QtCore.QRect(600, 80, 241, 31))
        self.edit_abs_diameter.setStyleSheet("border-radius: 14px;\n"
"background-color: rgb(150, 150, 150);\n"
"color: rgb(240, 240, 240);\n"
"padding: 7px;")
        self.edit_abs_diameter.setText("")
        self.edit_abs_diameter.setObjectName("edit_abs_diameter")
        self.lab_absolute_values = QtWidgets.QLabel(self.frame_3)
        self.lab_absolute_values.setGeometry(QtCore.QRect(10, 10, 891, 20))
        self.lab_absolute_values.setStyleSheet("font: 14pt;")
        self.lab_absolute_values.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_absolute_values.setWordWrap(False)
        self.lab_absolute_values.setObjectName("lab_absolute_values")
        self.btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_restart.setGeometry(QtCore.QRect(700, 10, 111, 31))
        self.btn_restart.setStyleSheet("QPushButton {\n"
"    background-color: rgb(195, 195, 195);\n"
"    font: 13pt \"Times New Roman\";\n"
"    border-radius: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(140, 140, 140);\n"
"    transition: 0.6s;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40,40);\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(110, 156, 255);\n"
"}")
        self.btn_restart.setObjectName("btn_restart")
        self.rad_simulation_exp = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_simulation_exp.setEnabled(True)
        self.rad_simulation_exp.setGeometry(QtCore.QRect(170, 10, 203, 25))
        self.rad_simulation_exp.setCheckable(True)
        self.rad_simulation_exp.setChecked(True)
        self.rad_simulation_exp.setObjectName("rad_simulation_exp")
        self.rad_simulation_phenomen = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_simulation_phenomen.setEnabled(True)
        self.rad_simulation_phenomen.setGeometry(QtCore.QRect(390, 10, 158, 25))
        self.rad_simulation_phenomen.setObjectName("rad_simulation_phenomen")
        self.btn_simulation = QtWidgets.QPushButton(self.centralwidget)
        self.btn_simulation.setGeometry(QtCore.QRect(570, 10, 111, 31))
        self.btn_simulation.setStyleSheet("QPushButton {\n"
"    background-color: rgb(195, 195, 195);\n"
"    font: 13pt \"Times New Roman\";\n"
"    border-radius: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(140, 140, 140);\n"
"    transition: 0.6s;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 40,40);\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(110, 156, 255);\n"
"}")
        self.btn_simulation.setObjectName("btn_simulation")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rad_simulation_exp.clicked.connect(self.frame_2.show)
        self.rad_simulation_exp.clicked.connect(self.frame_3.show)
        self.rad_simulation_exp.clicked.connect(self.frame_1.hide)
        self.rad_simulation_phenomen.clicked.connect(self.frame_1.show)
        self.rad_simulation_phenomen.clicked.connect(self.frame_2.hide)
        self.rad_simulation_phenomen.clicked.connect(self.frame_3.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CoeffDynamicViscosity"))
        self.lab_experiment_1.setText(_translate("MainWindow", "Эксперемент №1"))
        self.lab_viscosity.setText(_translate("MainWindow", "Вязкость (Па)"))
        self.lab_radius_of_the_ball.setText(_translate("MainWindow", "Радиус шара (м)"))
        self.lab_experiment_3.setText(_translate("MainWindow", "Эксперемент №3"))
        self.lab_passed_height.setText(_translate("MainWindow", "Пройденная высота (м)"))
        self.lab_experiment_2.setText(_translate("MainWindow", "Эксперемент №2"))
        self.lab_passage_time.setText(_translate("MainWindow", "Время прохождения (с)"))
        self.lab_experiment_average.setText(_translate("MainWindow", "Средние значения"))
        self.lab_dynamic_viscosity_coeff.setText(_translate("MainWindow", "Коэффициент динамической вязкости (Н*с/м^3)"))
        self.lab_liquid_density.setText(_translate("MainWindow", "Плотность жидкости (кг.м^3)"))
        self.lab_ball_diameter.setText(_translate("MainWindow", "Диаметр шара (мм)"))
        self.lab_ball_density.setText(_translate("MainWindow", "Плотность шара (кг/м^3)"))
        self.lab_abs_viscosity.setText(_translate("MainWindow", "Вязкость (Н*с/м^3) ="))
        self.lab_abs_liquid_density.setText(_translate("MainWindow", "Плотность жидкости (кг/м^3) ="))
        self.lab_abs_radius.setText(_translate("MainWindow", "D (мм) ="))
        self.lab_abs_ball_density.setText(_translate("MainWindow", "Плотность шара (кг/м^3) ="))
        self.lab_abs_height.setText(_translate("MainWindow", "h (мм) ="))
        self.lab_absolute_values.setText(_translate("MainWindow", "Абсолютные значения"))
        self.btn_restart.setText(_translate("MainWindow", "Сбросить"))
        self.rad_simulation_exp.setText(_translate("MainWindow", "Симуляция эксперимента"))
        self.rad_simulation_phenomen.setText(_translate("MainWindow", "Симуляция явления"))
        self.btn_simulation.setText(_translate("MainWindow", "Симуляция"))
