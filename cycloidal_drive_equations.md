# Cycloidal Drive Equations

$$
X = (R*cos(t))-(R_{r}*cos(t+arctan(sin((1-N)*t)/((R/E*N)-cos((1-N)*t)))))-(E*cos(N*t))
$$

$$
Y = (-R*sin(t))+(R_{r}*sin(t+arctan(sin((1-N)*t)/((R/E*N)-cos((1-N)*t)))))+(E*sin(N*t))
$$


$$
E = eccentricity \\
R = Radius\ of\ Center\ circle\ of\ cycloid \\
R_r = Radius\ of\ rotating\ circle\ of\ cycloid. \\
N = Number\ of\ teeth\\
t = Time\ which\ is\ the\ same\ as\ angle
$$

$$

R = 10\\
E = 0.75\\
Rr = 1.5 \\
N = 10

$$

$$
X = (10*cos(t))-(1.5*cos(t+arctan(sin((1-10)*t)/((10/0.75*10)-cos((1-10)*t)))))-(0.75*cos(10*t))\\
Y = (-10*sin(t))+(1.5*sin(t+arctan(sin((1-10)*t)/((10/0.75*10)-cos((1-10)*t)))))+(0.75*sin(10*t))

$$

## Solidworks

## Equation Driven Curce under Spline
Choose parametric equation.
$$
t_1 = (-10/360)*(2*pi)\\
t_2 = (190/360)*(2*pi)
$$

(28*cos(t))-(4*cos(t+arctan(sin((-1*19)*t)/((28/20*19)-cos((-1*19)*t)))))-(20*cos(19*t))
(-28*sin(t))+(4*sin(t+arctan(sin((-1*19)*t)/((28/20*19)-cos((1-19)*t)))))+(20*sin(19*t))