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
    theta_rad = theta * round(PI/180, 4)
    alpha_rad = alpha * round(PI/180, 4)
    cos_theta = cos(theta_rad)
    sin_theta = sin(theta_rad)
    cos_alpha = cos(alpha_rad)
    sin_alpha = sin(alpha_rad)
    
    T = Matrix([[cos_theta, -sin_theta*cos_alpha, sin_theta*sin_alpha, a*cos_theta], 
                [sin_theta, cos_theta*cos_alpha, -cos_theta*sin_alpha, a*sin_theta], 
                [0, sin_alpha, cos_alpha, d], 
                [0, 0, 0, 1]])
    
    return T

def MDH(alpha: float, a: float, theta: float, d: float) -> Matrix:
    cos_theta = cos(theta * round((PI/180), 4))
    sin_theta = sin(theta * round((PI/180), 4))
    cos_alpha = cos(alpha * round((PI/180), 4))
    sin_alpha = sin(alpha * round((PI/180), 4))
    
    T = Matrix([[cos_theta, -sin_theta, 0, a], \
                [sin_theta * cos_alpha, cos_theta * cos_alpha, -sin_alpha, -d * sin_alpha], \
                [sin_theta * sin_alpha, cos_theta * sin_alpha, cos_alpha , d * cos_alpha],\
                [0, 0, 0, 1]])
    
    return T

def jacobian_calculator(alpha: float, a: float, theta: float, d: float) -> Matrix:
    """
    Calculate the Jacobian matrix for a given set of parameters.

    Args:
        alpha (float): The alpha parameter.
        a (float): The a parameter.
        theta (float): The theta parameter.
        d (float): The d parameter.

    Returns:
        Matrix: The Jacobian matrix.
    """
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
