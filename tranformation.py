import os
import OpenGL.GL as gl
import OpenGL.GLUT as glut
from shape import line, points

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # gl.glMatrixMode(gl.GL_PROJECTION)
    # gl.glOrtho(-10, 10, -10, 10, 1, 0)
    gl.glLoadIdentity()
    gl.glMatrixMode(gl.GL_MODELVIEW)
    
    gl.glPointSize(5.5)
    gl.glBegin(gl.GL_LINES)
    gl.glColor3ub(0,255,0)
    gl.glVertex2f(0,0)
    gl.glVertex2f(0.5,0.5)
    gl.glEnd()

    gl.glPointSize(5.5)
    gl.glTranslatef(0.1, 0.2, 0)
    gl.glBegin(gl.GL_LINES)
    gl.glColor3ub(255,0,0)
    gl.glVertex2f(0,0)
    gl.glVertex2f(0.5,0.5)
    gl.glEnd()

    gl.glPointSize(5.5)
    gl.glScalef(0.2, 0.2, 0)
    gl.glBegin(gl.GL_LINES)
    gl.glColor3ub(0,0,255)
    gl.glVertex2f(0,0)
    gl.glVertex2f(0.5,0.5)
    gl.glEnd()

    gl.glPointSize(5.5)
    gl.glRotatef(45, 0, 0, 1)
    gl.glBegin(gl.GL_LINES)
    gl.glColor3ub(0,255,255)
    gl.glVertex2f(0,0)
    gl.glVertex2f(0.5,0.5)
    gl.glEnd()
    
    gl.glFlush()

def reshape(width, height):
    gl.glViewport(0,0, width, height)

def keyboard(key, x, y):
    if key == b'q':
        os._exit(0)

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGBA)
glut.glutCreateWindow('Hello World')
glut.glutReshapeWindow(512, 512)
glut.glutInitWindowPosition(0,0)

glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)

glut.glutMainLoop()