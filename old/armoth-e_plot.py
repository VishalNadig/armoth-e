L1 = 9  # Length of link 1 between 0 and 1
L2 = 10.5  # Length of link 2 between 1 and 2
L3 = 18  # Length of link 3 between 2 and 3
PI = 3.14159265
from math import acos, atan2, sqrt, sin, cos, sqrt
import matplotlib.pyplot as plt
from kinematic_calculator import DH
def forward_kinematics(theta1: float, theta2: float, theta3: float, theta4: float) -> list:
    """
    Calculates the forward kinematics of a robotic arm based on the given joint angles.

    Args:
        theta1 (float): The angle of joint 1 in degrees.
        theta2 (float): The angle of joint 2 in degrees.
        theta3 (float): The angle of joint 3 in degrees.
        theta4 (float): The angle of joint 4 in degrees.

    Returns:
        list: A list containing the X, Y, and Z coordinates of the end effector.

    Raises:
        None
    """
    theta1 = theta1 * PI / 180
    theta2 =  ((theta2 * PI / 180) ) # Greater than 90 -> 90 + (theta2 - 90); Less than 90 -> 90 - (90 - theta2)
    # TODO Make it so that theta3 is 90-(180-theta3) if theta3 > 180.
    theta3 = ((theta3 * PI / 180))# - 1.5708) # 1.5708 -> 90 degrees
    # theta3 = theta3 + 90
    # if theta3 > 180:
    #     theta3 = (theta3)-180
    # theta3 = ((theta3 * PI / 180))# - 1.5708) # 1.5708 -> 90 degrees
    max_horizontal = L2 + L3
    max_vertical = L1 + L2 + L3
    X = L3 * cos(theta1) * cos(theta2) * cos(theta3) + L3 * cos(theta1) * sin(theta2) * sin(theta3) + L2 * cos(theta1) * cos(theta2)

    Y = L3 * sin(theta1) * cos(theta2) * cos(theta3) - L3 * sin(theta1) * sin(theta2) * sin(theta3) + L2 * sin(theta1) * cos(theta2)

    Z = L3 * sin(theta2) * cos(theta3) + L3 * cos(theta2) * sin(theta3) + L2 * sin(theta2) + L1


    print(f"Theta 1: {theta1 * (180/PI)}", f"Theta 2: {theta2 * (180/PI)}", f"Theta 3: {theta3 * (180/PI)}")

    if abs(X) > max_horizontal:
        print(
            f"Unreachable! X: {X} is greater than max horizontal distance reachable of {max_horizontal}\n"
        )
    elif Z > max_vertical:
        print(
            f"Unreachable! Z: {Z} is greater than max vertical distance reachable of {max_vertical}\n"
        )
    elif Z < 0:
        print(f"Unreachable! Z: {Z} is lesser than 0. Cannot go below the table!\n")
    else:
        print(
            f"X: {X}",
            f"Y: {Y}",
            f"Z: {Z}",
            f"r: {sqrt(X ** 2 + Z ** 2)}",
            max_horizontal,
            str(max_vertical) + "\n",
        )
    return [X,Y,Z]


def kinematic_plot(theta1: float, theta2: float, theta3: float, theta4: float):
    """
    Generate the function comment for the given function body in a markdown code block with the correct language syntax.

    Args:
        theta1 (float): The value of theta1.
        theta2 (float): The value of theta2.
        theta3 (float): The value of theta3.
        theta4 (float): The value of theta4.

    Returns:
        None

    Raises:
        None
    """
    ax = plt.axes(projection = '3d')
    x_range = []
    y_range = []
    z_range = []
    theta1 = theta1 * PI/180
    for theta3 in range(0, 126):
        theta1 = theta1 * PI / 180
        theta2 =  ((theta2 * PI / 180) ) # Greater than 90 -> 90 + (theta2 - 90); Less than 90 -> 90 - (90 - theta2)
        # TODO Make it so that theta3 is 90-(180-theta3) if theta3 > 180.
        theta3 = ((theta3 * PI / 180))# - 1.5708) # 1.5708 -> 90 degrees
        max_horizontal = L2 + L3
        max_vertical = L1 + L2 + L3
        X = L3 * cos(theta1) * cos(theta2) * cos(theta3) + L3 * cos(theta1) * sin(theta2) * sin(theta3) + L2 * cos(theta1) * cos(theta2)

        Y = L3 * sin(theta1) * cos(theta2) * cos(theta3) - L3 * sin(theta1) * sin(theta2) * sin(theta3) + L2 * sin(theta1) * cos(theta2)

        Z = L3 * sin(theta2) * cos(theta3) + L3 * cos(theta2) * sin(theta3) + L2 * sin(theta2) + L1


        print(f"Theta 1: {theta1 * (180/PI)}", f"Theta 2: {theta2 * (180/PI)}", f"Theta 3: {theta3 * (180/PI)}")

        if Z > 0:
            x_range.append(X)
            y_range.append(Y)
            z_range.append(Z)
        if abs(X) > max_horizontal:
            print(
                f"Unreachable! X: {X} is greater than max horizontal distance reachable of {max_horizontal}\n"
            )
        elif Z > max_vertical:
            print(
                f"Unreachable! Z: {Z} is greater than max vertical distance reachable of {max_vertical}\n"
            )
        elif Z < 0:
            print(f"Unreachable! Z: {Z} is lesser than 0. Cannot go below the table!\n")
        else:
            print(
                f"X: {X}",
                f"Y: {Y}",
                f"Z: {Z}",
                f"r: {sqrt(X ** 2 + Z ** 2)}",
                max_horizontal,
                str(max_vertical) + "\n",
            )
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.plot3D(x_range, y_range, z_range)
    plt.show()

def kinematic_tester(theta1: float, theta2: float, theta3: float, theta4: float) -> list:
    x_range = []
    y_range = []
    z_range = []

    theta1 = theta1 * PI / 180
    theta2 =  ((theta2 * PI / 180))
    theta3 = ((theta3 * PI / 180))
    theta4_rad = theta4 * PI/180

    max_horizontal = L2 + L3
    max_vertical = L1 + L2 + L3
    return DH(alpha=90, theta = theta1, d = 9, a = 0) * DH(alpha=90, theta = theta2, d = 9, a = 0) * DH(alpha=90, theta = theta1, d = 9, a = 0)

kinematic_plot(0,0,0,0)