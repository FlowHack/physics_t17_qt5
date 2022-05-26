from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import QOpenGLWidget
from time import sleep


class OpenGLDraw:
    def __init__(self, widget: QOpenGLWidget, height=55, need_ball=False):
        self.opengl = widget
        self.width = self.opengl.width()
        self.height = self.opengl.height()
        self.xrot = 0.0
        self.yrot = 0.0
        self.water_color = (0.2, 0.3, 1, 1)
        self.ball_color = (0, 0, 0, 1)
        self.lightpos = (1, 1.0, 1.0)
        self.ambient = (1, 1.0, 1.0, 1)
        self.z_ball = height
        self.need_ball = need_ball

        self.initialize()

    def initialize(self):
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        self.opengl.resizeGL(self.width, self.height)
        glutInit(sys.argv)

        self.opengl.paintGL = self.paintGL

    def paintGL(self):
        self.loadScene()

        self.draw_cylinder()
        if self.need_ball:
            self.draw_ball()

        self.opengl.update()

    def draw_cylinder(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.need_ball:
            glTranslatef(0, 0, 0)
        glColor4f(0.2, 0.3, 1, 0.3)
        glutSolidCylinder(15, 60, 500, 500)
        glDisable(GL_BLEND)

    def draw_ball(self):
        if self.need_ball:
            for i in range(self.z_ball):
                glTranslatef(0, 0, i)
                glColor4f(0.1, 0.1, 0.1, 1)
                glutWireSphere(5, 500, 500)
                glTranslatef(0, 0, -i)
                self.opengl.update()
                sleep(0.1)

    def loadScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        x, y, width, height = glGetDoublev(GL_VIEWPORT)
        gluPerspective(45, width / float(height or 1), .25, 200)

        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_BLEND)
        glLoadIdentity()

        gluLookAt(100, 0, 0, 0, 0, 0, 0, 1, 0)
        glRotatef(-90, 1.0, 0, 0)
        glTranslatef(0, 0, -30)

        glEnable(GL_ALPHA_TEST)
        glClearColor(0.3, 0.3, 0.3, 1.0)
