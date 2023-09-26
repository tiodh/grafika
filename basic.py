import os
import OpenGL.GL as gl
import OpenGL.GLUT as glut
from shape import line, points

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glMatrixMode(gl.GL_MODELVIEW)
    
    points([[0,0]], [255,0,0])

    line([[0,0], [10,10], [20,20]], [255,255,0])
    
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