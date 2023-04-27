from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy

rate = 0.008
rangle = [0, 72, 144, 216, 288]    # tea pot mouth direction in the start
length = [0.1, 0.2, 0.3, 0.4, 0.5]
angle = 0
direction = [rate, rate, rate, rate, rate]     #Up and Down speed


def init_my_scene(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix.
    gluPerspective(45, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def func(R, angle):
    #Draw the Sticks
    glLineWidth(7)
    glColor3d(1, 0, 1)
    glBegin(GL_LINE_STRIP)
    glVertex3d(0, 0, 0)
    glVertex3d(0, R, 0)
    glEnd()
    # Draw the teapot
    glPushMatrix()
    glRotate(angle, 0, 1, 0)
    glTranslatef(0, R, 0)
    glLineWidth(1)
    glutWireTeapot(0.3)
    glPopMatrix()


def DrawGLScene():
    global rangle, length, angle, direction, up
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 2, 4, 0, 1, 0, 0, 1, 0)
    glColor3d(1, 1, 1)
    glRotate(angle, 0, 1, 0)
    glPushMatrix()
    glRotate(90, 1, 0, 0)
    glutSolidCylinder(1.6, 0.5, 50, 20)
    glPopMatrix()

    for i in range(5):
        glTranslate(1.2 * numpy.cos(i * 72 * numpy.pi / 180), 0, 1.2 * numpy.sin(i * 72 * numpy.pi / 180))       #location of the bots
        func(2 * length[i], rangle[i])   #In the very start
        glTranslate(-1.2 * numpy.cos(i * 72 * numpy.pi / 180), 0, -1.2 * numpy.sin(i * 72 * numpy.pi / 180))

    for i in range(5):
        if (length[i] >= 0.6):          #max range
            direction[i] = -rate
        if (length[i] <= 0.2):          #min range
            direction[i] = rate
        length[i] += direction[i]

        rangle[i] += 1           #tea pot rotation

    angle += 2          #Main Rotation

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("MOHAMED ALAA")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    init_my_scene(800, 600)
    glutMainLoop()


main()
