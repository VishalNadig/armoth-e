def display(N: int, R: float, r: float, E: float):
    """
    Generate Cycloid Drive Profile

    Args:
        N (int): Number of teeth/rollers
        R (int): Radius of Roller's Pitch Circle Diameter
        r (float): Radius of the roller/bearings in the drive casing.
        E (float): Eccentricity of the input shaft to the cycloid disc. E<R/N
        Ratio is N-1:1

    Returns:
        dict: X and Y coordinates of the parametric equation
    """
    _N = 1 - N
    R_EN = R / (E * N)
    X = f"({R}*cos(t)) - ({r}*cos(t + arctan(sin({N}*t)/({R_EN} - cos({N}*t))))) - ({r}*cos({N}*t))"
    Y = f"(-{R}*sin(t)) + ({r}*sin(t + arctan(sin({N}*t)/({R_EN} - cos({N}*t))))) + ({r}*sin({N}*t))"
    t_1 = "(-10/360)*(2*pi)"
    t_2 = "(190/360)*(2*pi)"
    Eccentricity_limit = R / N

    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"t_1 = {t_1}")
    print(f"t_2 = {t_2}")
    print(f"Eccentricity should be less than: {Eccentricity_limit}")


display(N=16, r= 6.5, E=1.5, R=37.5)
# N 25 ul
# E 1 mm
# Rr 2 mm
# R 31.5 mm