'''
PROJECT G.U.R.U.M.U.R.T.H - E
Generally Underperforming Robot Usually Managing Uninteresting Routines and Tasks at Hand - Eagerly
MG996R Servo Motor Features
Operating Voltage is +5V typically
Current: 2.5A (6V)
Stall Torque: 9.4 kg/cm (at 4.8V)
Maximum Stall Torque: 11 kg/cm (6V)
Operating speed is 0.17 s/60°
Gear Type: Metal
Rotation : 0°-180°
Weight of motor : 55gm
Package includes gear horns and screws
'''
# TODO: Solve the Inverse Kinematics.
# TODO: Get the raspberry's talking wirelessly.
# TODO: Add an image recognition. Use OpenCV.
# TODO: Further complex tasks like pick and place!
# FEAT: Make FK calculations completely autonomous.


# from machine import PWM, Pin
# from ulab import numpy as np
from math import acos, atan2, cos, sin, sqrt
from time import sleep
import sympy
import kinematic_calculator as kc

# led = Pin(25, Pin.OUT) # Pin 25 is the on board LED Pin
# SERVOS = {"BASE": PWM(Pin(4)), "ARM":PWM(Pin(5)), "SHOULDER":PWM(Pin(6)), "WRIST":PWM(Pin(7))}


'''
base: 1600-8000
shoulder: 1500-7500
arm: 1600-8000
wrist: 1600-8000
'''

L1 = 9 # Length of link 1 between 0 and 1
L2 = 10.5 # Length of link 2 between 1 and 2
L3 = 18 # Length of link 3 between 2 and 3
PI = 3.14159265

# servo = PWM(Pin(0))
# servo.freq(50)

# def set_frequency(frequency = 50):
    # SERVOS.get("BASE").freq(frequency)

def classic_matrix_generator(theta1: float = sympy.symbols('theta1'), theta2: float = sympy.symbols('theta2'), theta3: float = sympy.symbols('theta3')) -> sympy.Matrix:
    # TODO: Make the matrix more generic to take in any number of joints and calculate the matrix.
    """Generate a classic Homogenous Transformation Matrix by default. If values of theta1, theta2 and theta3 are specified then print the values of the X, Y and Z. Useful for getting forward kinematics of one joint of a robot. Can be chained together to produce the complete kinematic matrix of the robot.

    Args:
        theta1 (float, optional): Angle of first joint in degrees. Defaults to sympy.symbols('theta1').
        theta2 (float, optional): Angle of second joint in degrees. Defaults to sympy.symbols('theta2').
        theta3 (float, optional): Angle of third joint in degrees. Defaults to sympy.symbols('theta3').

    Returns:
        sympy.Matrix: Resultant 4x4 matrix of the of the two links of a joint.
    """
    HTM = kc.DH(a = 0, theta=theta1, d = L1, alpha = 90) * kc.DH(a = L2, theta= theta2, d = 0, alpha = 0) * kc.DH(a = L3, theta= theta3, d = 0, alpha = 0)
    return HTM

def modified_matrix_generator(theta1: float = sympy.symbols('theta1'), theta2: float = sympy.symbols('theta2'), theta3: float = sympy.symbols('theta3')) -> sympy.Matrix:
    """Generate a modified Homogenous Transformation Matrix by default. If values of theta1, theta2 and theta3 are specified then print the values of the X, Y and Z. Useful for getting forward kinematics of one joint of a robot. Can be chained together to produce the complete kinematic matrix of the robot.

    Args:
        theta1 (float, optional): Angle of first joint in degrees. Defaults to sympy.symbols('theta1').
        theta2 (float, optional): Angle of second joint in degrees. Defaults to sympy.symbols('theta2').
        theta3 (float, optional): Angle of third joint in degrees. Defaults to sympy.symbols('theta3').

    Returns:
        sympy.Matrix: Resultant 4x4 matrix of the of the two links of a joint.
    """
    HTM = kc.MDH(a = 0, theta=theta1, d = L1, alpha = 90) * kc.MDH(a = L2, theta= theta2, d = 0, alpha = 0) * kc.MDH(a = L3, theta= theta3, d = 0, alpha = 0)
    return HTM

def forward_kinematics(theta1: float, theta2: float, theta3: float):
    """
    Function to calculate the forward kinematics of the robot and calculate the X, Y and Z positions of the end effector where angles θ1, θ2, θ3 and θ4 are given using classical Denavit Hartenberg parameters.

    Args:
        theta1 (float): Angle of Z0(base)
        theta2 (float): Angle of Z1(arm)
        theta3 (float): Angle of Z2(shoulder)
        theta4 (float): Angle of Z3(Wrist)

    """
    theta1 = theta1* (PI / 180)
    theta2 = theta2* (PI / 180)
    theta3 = theta3* (PI / 180)
    # print(classic_matrix_generator(theta1, theta2, theta3))
    matrix = classic_matrix_generator()
    print(f"X = {matrix[3]}\n\n", f"Y = {matrix[7]}\n\n", f"Z = {matrix[11]}\n\n")
forward_kinematics(0,0,0)

# def inverse_kinematics(x: float, y: float, z: float):


# def set_angle(angle: float, servo: PWM):
#     # led.high()
#     duty = int((((angle/18.0) + 2.5) /100) * 65535)
#     print(f"Duty: {duty}")
#     servo.duty_u16(duty)
#     sleep(1)
    # servo.deinit()
    # led.low()

# def home_position():
#     theta1 = 0
#     theta2 = 120
#     theta3 = 0
#     theta4 = 0
#     set_angle(theta1, SERVOS.get("BASE"))
#     set_angle(theta2, SERVOS.get("ARM"))
#     set_angle(theta3, SERVOS.get("SHOULDER"))
#     set_angle(theta4, SERVOS.get("WRIST"))

# set_angle(abs(0), servo)
# servo.deinit()

