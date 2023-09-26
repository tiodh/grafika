import OpenGL.GL as gl
def line(vertices: list, color: list):
    '''
    vertices: multidimensional list
    each item of list contain x and y
    '''
    gl.glColor3ub(color[0],color[1],color[2])
    gl.glBegin(gl.GL_LINES)
    for v in vertices:
        gl.glVertex2f(*v)
    gl.glEnd()
    
def points(vertices: list, color: list):
    '''
    vertices: multidimensional list
    each item of list contain x and y
    '''
    gl.glPointSize(5.5)
    gl.glBegin(gl.GL_POINTS)
    for v in vertices:
        gl.glColor3ub(color[0],color[1],color[2])
        gl.glVertex2f(*v)
    gl.glEnd()
