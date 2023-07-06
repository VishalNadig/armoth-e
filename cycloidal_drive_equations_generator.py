def display(N: int, R: float, r: float , E: float):
    """Generate Cycloid Drive Profile

    Args:
        N (int): Number of teeth/rollers
        R (int): Radius of Roller's Pitch Circle Diameter
        r (float): Radius of the roller/bearings in the drive casing.
        E (float): Eccentricity of the input shaft to the cycloid disc. E<R/N
        Ratio is N-1:1


    Returns:
        dict: X and Y coordinates of the parametric equation
    """
    _N = 1-N
    R_EN = R/(E*N)
    print("X = ({}*cos(t)) - ( {}*cos( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) - ({}*cos({}*t)) ".format(R,r,_N,R_EN,_N,E,N ))
    print("Y = (-{}*sin(t)) + ( {}*sin( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) + ({}*sin({}*t)) ".format(R,r,_N,R_EN,_N,E,N))
    print("t_1 = (-10/360)*(2*pi)\nt_2 = (190/360)*(2*pi)")
    print(f"Eccentricity should be less than: {R/N}")


display(N=16, r= 6.5, E=1.5, R=37.5)
# N 25 ul
# E 1 mm
# Rr 2 mm
# R 31.5 mm