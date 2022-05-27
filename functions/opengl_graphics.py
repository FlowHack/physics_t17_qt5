from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep, perf_counter_ns


class OpenGlWindow:
    def __init__(self, numbers, time, count_simulations=1):
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(321, 600)
        glutInitWindowPosition(50, 50)
        glutInit(sys.argv)
        self.id_window = glutCreateWindow('Simulation of an experiment')
        glutDisplayFunc(self.paintGL)

        self.time = time
        self.numbers = numbers
        self.count_simulations = count_simulations
        self.iteration = 0

        self.initialize()
        glutMainLoopEvent()

    def initialize(self):
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

    def paintGL(self):
        while self.count_simulations > self.iteration:
            for i in self.numbers:
                time_animation_start = perf_counter_ns()
                glClear(GL_COLOR_BUFFER_BIT)
                self.draw_cylinder()
                glTranslatef(0, 0, i)
                glColor4f(0.1, 0.1, 0.1, 1)
                glutWireSphere(5, 500, 500)
                glTranslatef(0, 0, -i)
                glutSwapBuffers()
                time_animation = perf_counter_ns() - time_animation_start
                time_start = perf_counter_ns()
                while True:
                    need_time = self.time - time_animation
                    need_time = need_time if need_time > 0 else 0
                    if perf_counter_ns() - time_start >= need_time:
                        break
            self.iteration += 1
        else:
            sleep(1)
            glutDestroyWindow(self.id_window)

    def draw_cylinder(self):
        glColor4f(0.2, 0.3, 1, 0.3)
        glutSolidCylinder(15, 60, 500, 500)

    def draw_ball(self, z_index, time):
        print('Зашёл')
        for i in range(z_index)[::-1]:
            glTranslatef(0, 0, i)
            glColor4f(0.1, 0.1, 0.1, 1)
            glutWireSphere(5, 500, 500)
            glTranslatef(0, 0, -i)
            glutPostRedisplay()
            glutSwapBuffers()
            sleep(time)
