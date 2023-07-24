"""This is a very short module for performing symbolic kinematics on
robots using the Denavit-Hartenberg (DH) convention.  This module
includes the essential functions for deriving a DH matrix for one link
of a robot as well as multiplying multiple DH matrices together to
model a robot."""
from sympy import Matrix, cos, sin, eye, diff

PI = 3.14159265
def Rx(th):
    """Create a symbolic Rx rotation matrix.  Theta should be in
    radians if it is numeric."""
    R = Matrix([[1,0,0],\
                [0,cos(th),-sin(th)],\
                [0,sin(th),cos(th)]])
    return R

def HT(R, Px=0, Py=0, Pz=0):
    """Create an HT arbitrary matrix based on an arbitrary rotation
    matrix R and optional Px, Py, and Pz translations."""
    T = eye(4)
    T[0:3,0:3] = R
    T[0,3] = Px
    T[1,3] = Py
    T[2,3] = Pz
    return T

def HTx(alpha, Px=0, Py=0, Pz=0):
    """Create an HT matrix based on an Rx rotation and optional Px,
    Py, and Pz translations.  Alpha should be in
    radians if it is numeric."""
    R = Rx(alpha)
    T = HT(R, Px, Py, Pz)
    return T


def Ry(th):
    """Create a symbolic Ry rotation matrix.  Theta should be in
    radians if it is numeric."""
    R = Matrix([[cos(th),0, sin(th)],\
                [0,1,0],\
                [-sin(th),0,cos(th)]])
    return R

def Rz(th):
    """Create a symbolic Rz rotation matrix.  Theta should be in
    radians if it is numeric."""
    R = Matrix([[cos(th),-sin(th),0],\
                [sin(th),cos(th),0],\
                [0,0,1]])
    return R


def HTz(theta, Px=0, Py=0, Pz=0):
    """Create an HT matrix based on an Rz rotation and optional Px,
    Py, and Pz translations."""
    R = Rz(theta)
    T = HT(R, Px, Py, Pz)
    return T


def DH(alpha: float, a: float, theta: float, d: float) -> Matrix:
    """Note that this function uses sin and cos from sympy, which
    expect inputs in radians.  This is not really an issue for
    symbolic variables, but if you want alpha=90 degrees, use pi/2
    (for example).  Also be sure to use pi from sympy so that
    sin(pi/2)=1, cos(pi/2)=0, and so on."""
    T = Matrix([[cos(theta * round((PI/180), 4)), -sin(theta * round((PI/180), 4))*cos(alpha * round((PI/180), 4)), sin(theta * round((PI/180), 4))*sin(alpha * round((PI/180), 4)), a*cos(theta * round((PI/180), 4))], \
                [sin(theta * round((PI/180), 4)), cos(theta * round((PI/180), 4))*cos(alpha * round((PI/180), 4)), -cos(theta * round((PI/180), 4))*sin(alpha * round((PI/180), 4)), a*sin(theta * round((PI/180), 4))], \
                [0         , sin(alpha * round((PI/180), 4))           , cos(alpha * round((PI/180), 4))  ,          d],\
                [0         , 0                                 , 0                        ,          1]])
    return T

def MDH(alpha: float, a: float, theta: float, d: float) -> Matrix:
    T = Matrix([[cos(theta * round((PI/180), 4)), -sin(theta * round((PI/180), 4)), 0, a], \
                [sin(theta * round((PI/180), 4)) * cos(alpha * round((PI/180), 4)), cos(theta * round((PI/180), 4)) * cos(alpha * round((PI/180), 4)), -sin(alpha * round((PI/180), 4)), -d * sin(alpha * round((PI/180), 4))], \
                [sin(theta * round((PI/180), 4)) * sin(alpha * round((PI/180), 4)), cos(theta * round((PI/180), 4)) * sin(alpha * round((PI/180), 4)), cos(alpha * round((PI/180), 4)) , d * cos(alpha * round((PI/180), 4))],\
                [0                                                , 0                                                , 0                       ,          1]])
    return T

def jacobian_calculator(alpha: float, a: float, theta: float, d: float) -> Matrix:
    pass
#     T = MDH(alpha=alpha, a=a, theta = theta, d=d)
#     px = T[4]1]
#     py = T[4]2]
#     pz = T[4]3]
#     Matrix([diff(px, theta])

def velocity_kinematics():
    pass

def lagrangian_calculator():
    pass
