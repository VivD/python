import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

# set up parameters
v_C = np.array([5.31146, 0.52655])
v_k1 = np.array([9694.09, 0.0])
v_k2 = np.array([0.0, 60.5227])
v_k3 = np.array([2.85e-5, 321.07])
lo = 0
hi = 1

# set up path
v_goal = 2000 # m
speed_limit = 25 / 2.23694 # mph > m/s

# set up the gekko model
gek = GEKKO()

# set up the time
num_points = 200
max_time = 300
gek.time = np.linspace(0, 1, num_points)

# set up the Manipulated Variables
G = gek.MV(value=0, lb=0)
Fb = gek.MV(value=0, lb=0)

# set up the time variable (to minimize)
tf = gek.FV(value=120, lb=0, ub=max_time)

# turn them 'on'
for s in (G, Fb, tf):
	s.STATUS = 1

# set up the variables
x = gek.Var(value=0, lb=0, ub=v_goal)
v = gek.Var(value=0, lb=0, ub=speed_limit)
a = gek.Var(value=0, ub=3, lb=-3)
Fe = gek.Var(value=0)
Fd = gek.Var(value=0)
FUEL = gek.Var(value=0)

# add stops
gek.fix(x, num_points-1, v_goal) # destination
# stop sign
gek.fix(v, int(num_points/3), 0) 

# set up the parameters
m = gek.Param(value=1600)
C = gek.Param(value=v_C[lo])
k1 = gek.Param(value=v_k1[lo])
k2 = gek.Param(value=0*v_k2[lo])
k3 = gek.Param(value=v_k3[lo])

# set up the equations
gek.Equation(v.dt() / tf == a)
gek.Equation(x.dt() / tf == v)
gek.Equation(Fd == C * v**2)
gek.Equation(Fe == k1*G/(v+1) + k2*G**2 + k3*G**(1/2))
gek.Equation(a == (Fe - Fd - Fb) / m)
gek.Equation(FUEL.dt() / tf == G/3600)
gek.Equation(G * Fb < 1)

# set up the goal
#goal = np.full(max_time+1, v_goal)
#goal = gek.Param(value=goal)
last = np.zeros(num_points)
last[-1] = 1
last = gek.Param(value=last)
#arrive = np.zeros(max_time+1)
#arrive[min_time:] = 1
#arrive = gek.Param(value=arrive)

# set up the solver
gek.options.IMODE = 6

# set up the objective
gek.Obj(tf + 7*FUEL*last)

# solve
gek.solve(disp=False)

# calculate the instantaneous mpg
mpg = np.array(v.value) *2.23694/ (np.array(G.value)**2+0.1) * np.array(G.value)

print(FUEL[-1], "gallons used")
print(tf.NEWVAL, "seconds taken")
print(v_goal/FUEL[-1], "average miles per gallon")

# plot the results
time = np.linspace(0, 1, num_points)*tf.NEWVAL
plt.figure(figsize=(10, 10))
plt.subplot(611)
plt.plot(time, np.array(x.value)*3.28084/5280)
plt.plot([0, tf.NEWVAL], np.full(2,v_goal)*3.28084/5280, label='goal')
plt.ylabel('position\n(mi)')
plt.subplot(612)
plt.plot(time, np.array(v.value)*2.23694)
plt.ylabel('velocity\n(mph)')
plt.subplot(613)
plt.plot(time, np.array(a.value)*2.23694)
plt.ylabel('acceleration\n(mph/s)')
plt.subplot(614)
plt.plot(time, np.array(G.value)/3600*3785.41)
plt.ylabel('Fuel Rate\n(mL/s)')
plt.subplot(615)
plt.plot(time, mpg)
plt.ylabel('Fuel Efficiency\n(mpg)')
plt.subplot(616)
plt.plot(time, Fb, label='Fb')
plt.plot(time, Fe, '--', label='Fe')
plt.plot(time, Fd, '--', label='Fd')
plt.ylabel('Force (N)')
plt.xlabel('Time (s)')
plt.legend()
plt.show()
