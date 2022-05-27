# #!/usr/bin/env python


# #############################################################################
# ##
# ## Copyright (C) 2015 Riverbank Computing Limited.
# ## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
# ## All rights reserved.
# ##
# ## This file is part of the examples of PyQt.
# ##
# ## $QT_BEGIN_LICENSE:BSD$
# ## You may use this file under the terms of the BSD license as follows:
# ##
# ## "Redistribution and use in source and binary forms, with or without
# ## modification, are permitted provided that the following conditions are
# ## met:
# ##   * Redistributions of source code must retain the above copyright
# ##     notice, this list of conditions and the following disclaimer.
# ##   * Redistributions in binary form must reproduce the above copyright
# ##     notice, this list of conditions and the following disclaimer in
# ##     the documentation and/or other materials provided with the
# ##     distribution.
# ##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
# ##     the names of its contributors may be used to endorse or promote
# ##     products derived from this software without specific prior written
# ##     permission.
# ##
# ## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# ## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# ## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# ## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# ## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# ## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# ## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# ## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# ## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# ## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# ## $QT_END_LICENSE$
# ##
# #############################################################################


# import sys
# import math

# from PyQt5.QtCore import pyqtSignal, QSize, Qt, QTimer
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QLabel,
#         QMainWindow, QMessageBox, QOpenGLWidget, QScrollArea,
#         QSizePolicy, QSlider, QWidget)

# import OpenGL.GL as gl


# class GLWidget(QOpenGLWidget):
#     xRotationChanged = pyqtSignal(int)
#     yRotationChanged = pyqtSignal(int)
#     zRotationChanged = pyqtSignal(int)

#     def __init__(self, parent=None):
#         super(GLWidget, self).__init__(parent)

#         self.gear1 = 0
#         self.gear2 = 0
#         self.gear3 = 0
#         self.xRot = 0
#         self.yRot = 0
#         self.zRot = 0
#         self.gear1Rot = 0

#         timer = QTimer(self)
#         timer.timeout.connect(self.advanceGears)
#         timer.start(20)

#     def setXRotation(self, angle):
#         self.normalizeAngle(angle)

#         if angle != self.xRot:
#             self.xRot = angle
#             self.xRotationChanged.emit(angle)
#             self.update()

#     def setYRotation(self, angle):
#         self.normalizeAngle(angle)

#         if angle != self.yRot:
#             self.yRot = angle
#             self.yRotationChanged.emit(angle)
#             self.update()

#     def setZRotation(self, angle):
#         self.normalizeAngle(angle)

#         if angle != self.zRot:
#             self.zRot = angle
#             self.zRotationChanged.emit(angle)
#             self.update()

#     def initializeGL(self):
#         lightPos = (5.0, 5.0, 10.0, 1.0)
#         reflectance1 = (0.8, 0.1, 0.0, 1.0)
#         reflectance2 = (0.0, 0.8, 0.2, 1.0)
#         reflectance3 = (0.2, 0.2, 1.0, 1.0)

#         gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
#         gl.glEnable(gl.GL_LIGHTING)
#         gl.glEnable(gl.GL_LIGHT0)
#         gl.glEnable(gl.GL_DEPTH_TEST)

#         self.gear1 = self.makeGear(reflectance1, 1.0, 4.0, 1.0, 0.7, 20)
#         self.gear2 = self.makeGear(reflectance2, 0.5, 2.0, 2.0, 0.7, 10)
#         self.gear3 = self.makeGear(reflectance3, 1.3, 2.0, 0.5, 0.7, 10)

#         gl.glEnable(gl.GL_NORMALIZE)
#         gl.glClearColor(0.0, 0.0, 0.0, 1.0)

#     def paintGL(self):
#         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

#         gl.glPushMatrix()
#         gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
#         gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
#         gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

#         self.drawGear(self.gear1, -3.0, -2.0, 0.0, self.gear1Rot / 16.0)
#         self.drawGear(self.gear2, +3.1, -2.0, 0.0,
#                 -2.0 * (self.gear1Rot / 16.0) - 9.0)

#         gl.glRotated(+90.0, 1.0, 0.0, 0.0)
#         self.drawGear(self.gear3, -3.1, -1.8, -2.2,
#                 +2.0 * (self.gear1Rot / 16.0) - 2.0)

#         gl.glPopMatrix()

#     def resizeGL(self, width, height):
#         side = min(width, height)
#         if side < 0:
#             return

#         gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

#         gl.glMatrixMode(gl.GL_PROJECTION)
#         gl.glLoadIdentity()
#         gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
#         gl.glMatrixMode(gl.GL_MODELVIEW)
#         gl.glLoadIdentity()
#         gl.glTranslated(0.0, 0.0, -40.0)

#     def mousePressEvent(self, event):
#         self.lastPos = event.pos()

#     def mouseMoveEvent(self, event):
#         dx = event.x() - self.lastPos.x()
#         dy = event.y() - self.lastPos.y()

#         if event.buttons() & Qt.LeftButton:
#             self.setXRotation(self.xRot + 8 * dy)
#             self.setYRotation(self.yRot + 8 * dx)
#         elif event.buttons() & Qt.RightButton:
#             self.setXRotation(self.xRot + 8 * dy)
#             self.setZRotation(self.zRot + 8 * dx)

#         self.lastPos = event.pos()

#     def advanceGears(self):
#         self.gear1Rot += 2 * 16
#         self.update()

#     def xRotation(self):
#         return self.xRot

#     def yRotation(self):
#         return self.yRot

#     def zRotation(self):
#         return self.zRot

#     def makeGear(self, reflectance, innerRadius, outerRadius, thickness, toothSize, toothCount):
#         list = gl.glGenLists(1)
#         gl.glNewList(list, gl.GL_COMPILE)
#         gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE,
#                 reflectance)

#         r0 = innerRadius
#         r1 = outerRadius - toothSize / 2.0
#         r2 = outerRadius + toothSize / 2.0
#         delta = (2.0 * math.pi / toothCount) / 4.0
#         z = thickness / 2.0

#         gl.glShadeModel(gl.GL_FLAT)

#         for i in range(2):
#             if i == 0:
#                 sign = +1.0
#             else:
#                 sign = -1.0

#             gl.glNormal3d(0.0, 0.0, sign)

#             gl.glBegin(gl.GL_QUAD_STRIP)

#             for j in range(toothCount+1):
#                 angle = 2.0 * math.pi * j / toothCount
#                 gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
#                 gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
#                 gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
#                 gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

#             gl.glEnd()

#             gl.glBegin(gl.GL_QUADS)

#             for j in range(toothCount):
#                 angle = 2.0 * math.pi * j / toothCount
#                 gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
#                 gl.glVertex3d(r2 * math.cos(angle + delta), r2 * math.sin(angle + delta), sign * z)
#                 gl.glVertex3d(r2 * math.cos(angle + 2 * delta), r2 * math.sin(angle + 2 * delta), sign * z)
#                 gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

#             gl.glEnd()

#         gl.glBegin(gl.GL_QUAD_STRIP)

#         for i in range(toothCount):
#             for j in range(2):
#                 angle = 2.0 * math.pi * (i + (j / 2.0)) / toothCount
#                 s1 = r1
#                 s2 = r2

#                 if j == 1:
#                     s1, s2 = s2, s1

#                 gl.glNormal3d(math.cos(angle), math.sin(angle), 0.0)
#                 gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), +z)
#                 gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), -z)

#                 gl.glNormal3d(s2 * math.sin(angle + delta) - s1 * math.sin(angle), s1 * math.cos(angle) - s2 * math.cos(angle + delta), 0.0)
#                 gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), +z)
#                 gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), -z)

#         gl.glVertex3d(r1, 0.0, +z)
#         gl.glVertex3d(r1, 0.0, -z)
#         gl.glEnd()

#         gl.glShadeModel(gl.GL_SMOOTH)

#         gl.glBegin(gl.GL_QUAD_STRIP)

#         for i in range(toothCount+1):
#             angle = i * 2.0 * math.pi / toothCount
#             gl.glNormal3d(-math.cos(angle), -math.sin(angle), 0.0)
#             gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), +z)
#             gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), -z)

#         gl.glEnd()

#         gl.glEndList()

#         return list

#     def drawGear(self, gear, dx, dy, dz, angle):
#         gl.glPushMatrix()
#         gl.glTranslated(dx, dy, dz)
#         gl.glRotated(angle, 0.0, 0.0, 1.0)
#         gl.glCallList(gear)
#         gl.glPopMatrix()

#     def normalizeAngle(self, angle):
#         while (angle < 0):
#             angle += 360 * 16

#         while (angle > 360 * 16):
#             angle -= 360 * 16


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         centralWidget = QWidget()
#         self.setCentralWidget(centralWidget)

#         self.glWidget = GLWidget()
#         self.pixmapLabel = QLabel()

#         self.glWidgetArea = QScrollArea()
#         self.glWidgetArea.setWidget(self.glWidget)
#         self.glWidgetArea.setWidgetResizable(True)
#         self.glWidgetArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.glWidgetArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored,
#                 QSizePolicy.Ignored)
#         self.glWidgetArea.setMinimumSize(50, 50)

#         self.pixmapLabelArea = QScrollArea()
#         self.pixmapLabelArea.setWidget(self.pixmapLabel)
#         self.pixmapLabelArea.setSizePolicy(QSizePolicy.Ignored,
#                 QSizePolicy.Ignored)
#         self.pixmapLabelArea.setMinimumSize(50, 50)

#         xSlider = self.createSlider(self.glWidget.xRotationChanged,
#                 self.glWidget.setXRotation)
#         ySlider = self.createSlider(self.glWidget.yRotationChanged,
#                 self.glWidget.setYRotation)
#         zSlider = self.createSlider(self.glWidget.zRotationChanged,
#                 self.glWidget.setZRotation)

#         self.createActions()
#         self.createMenus()

#         centralLayout = QGridLayout()
#         centralLayout.addWidget(self.glWidgetArea, 0, 0)
#         centralLayout.addWidget(self.pixmapLabelArea, 0, 1)
#         centralLayout.addWidget(xSlider, 1, 0, 1, 2)
#         centralLayout.addWidget(ySlider, 2, 0, 1, 2)
#         centralLayout.addWidget(zSlider, 3, 0, 1, 2)
#         centralWidget.setLayout(centralLayout)

#         xSlider.setValue(15 * 16)
#         ySlider.setValue(345 * 16)
#         zSlider.setValue(0 * 16)

#         self.setWindowTitle("Grabber")
#         self.resize(400, 300)

#     def grabFrameBuffer(self):
#         image = self.glWidget.grabFramebuffer()
#         self.setPixmap(QPixmap.fromImage(image))

#     def clearPixmap(self):
#         self.setPixmap(QPixmap())

#     def about(self):
#         QMessageBox.about(self, "About Grabber",
#                 "The <b>Grabber</b> example demonstrates two approaches for "
#                 "rendering OpenGL into a Qt pixmap.")

#     def createActions(self):
#         self.grabFrameBufferAct = QAction("&Grab Frame Buffer", self,
#                 shortcut="Ctrl+G", triggered=self.grabFrameBuffer)

#         self.clearPixmapAct = QAction("&Clear Pixmap", self,
#                 shortcut="Ctrl+L", triggered=self.clearPixmap)

#         self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
#                 triggered=self.close)

#         self.aboutAct = QAction("&About", self, triggered=self.about)

#         self.aboutQtAct = QAction("About &Qt", self,
#                 triggered=QApplication.instance().aboutQt)

#     def createMenus(self):
#         self.fileMenu = self.menuBar().addMenu("&File")
#         self.fileMenu.addAction(self.grabFrameBufferAct)
#         self.fileMenu.addAction(self.clearPixmapAct)
#         self.fileMenu.addSeparator()
#         self.fileMenu.addAction(self.exitAct)

#         self.helpMenu = self.menuBar().addMenu("&Help")
#         self.helpMenu.addAction(self.aboutAct)
#         self.helpMenu.addAction(self.aboutQtAct)

#     def createSlider(self, changedSignal, setterSlot):
#         slider = QSlider(Qt.Horizontal)
#         slider.setRange(0, 360 * 16)
#         slider.setSingleStep(16)
#         slider.setPageStep(15 * 16)
#         slider.setTickInterval(15 * 16)
#         slider.setTickPosition(QSlider.TicksRight)

#         slider.valueChanged.connect(setterSlot)
#         changedSignal.connect(slider.setValue)

#         return slider

#     def setPixmap(self, pixmap):
#         self.pixmapLabel.setPixmap(pixmap)
#         size = pixmap.size()

#         if size - QSize(1, 0) == self.pixmapLabelArea.maximumViewportSize():
#             size -= QSize(1, 0)

#         self.pixmapLabel.resize(size)


# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import QOpenGLWidget


def init():
    global xrot         # Величина вращения по оси x
    global yrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    global greencolor   # Цвет елочных иголок
    global water_color    # Цвет елочного ствола
    global lightpos     # Положение источника освещения

    xrot = 0.0                          # Величина вращения по оси x = 0
    yrot = 0.0                          # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)        # Первые три числа цвет в формате RGB, а последнее - яркость
    greencolor = (0.2, 0.8, 0.0, 0.8)   # Зеленый цвет для иголок
    water_color = (0.2, 0.2, 1, 1)    # Коричневый цвет для ствола
    lightpos = (1.0, 1.0, 1.0)          # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 1.0, 0.0, 0.0)                   # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Определяем положение источника света


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global water_color

    glClear(GL_COLOR_BUFFER_BIT)                           # Очищаем экран и заливаем серым цветом
    glPushMatrix()                                              # Сохраняем текущее положение "камеры"
    glRotatef(-5, 1.0, 0.0, 0.0)                              # Вращаем по оси X на величину xrot
    glRotatef(yrot, 0.0, 1.0, 0.0)                              # Вращаем по оси Y на величину yrot
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                 # Источник света вращаем вместе с елкой

    # Рисуем ствол елки
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, коричневый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, water_color)
    glTranslatef(0.0, 0.0, -0.8)                                # Сдвинемся по оси Z на -0.7
    # Рисуем цилиндр с радиусом 0.1, высотой 0.2
    # Последние два числа определяют количество полигонов
    glutSolidCylinder(0.5, 1.3, 20, 20)
    # Рисуем ветки елки
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, зеленый цвет
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
    glTranslatef(0.0, 0.0, 0.2)                                 # Сдвинемся по оси Z на 0.2
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z на -0.3
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z на -0.3
    glutWireSphere(0.1, 500, 500)

    glPopMatrix()                                               # Возвращаем сохраненное положение "камеры"
    glutSwapBuffers()                                           # Выводим все нарисованное в памяти на экран


# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(500, 600)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(50, 50)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком "Happy New Year!"
glutCreateWindow(b"Happy New Year!")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
