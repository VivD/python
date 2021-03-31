import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Simulation time step definition
tf          = 0.5                        #final time for simulation
nsteps      = 501                        #number of time steps
delta_t     = tf / (nsteps - 1)          #length of each time step
ts          = np.linspace(0,tf,nsteps)   #time step array

v0          = 25.0                       #initial velocity in mps
h0          = 0.0                        #initial height in m
v_diff      = 0.0                        #velocity difference to test zero crossing
curr_het    = 0.0                        #temp var to store current height
v_diff_prev = 0                          #velocity difference from previous time step
switch      = 1                          #flag to identify discontinuity and swith the kinematic eqn

#variable to store simulation output
curr_vel    = v0*np.ones(nsteps)         #instantaneous ball velocities
height      = np.zeros(nsteps)           #instantaneous ball height

def rise_fall(h0,t,v0): ###sqrt.sqrt.square is a math trick to prevent nan's... can be neglected
    if switch == 1:
        dh_dt = np.sqrt(np.sqrt(np.square((v0**2 - 2*9.81*h0))))  #ODE for rising dynamics
    elif switch == 2:
        dh_dt = -np.sqrt(np.sqrt(np.square((v0**2 + 2*9.81*h0)))) #ODE for falling dynamics
    return dh_dt

#Simulation for each time step begins here
for i in range (nsteps - 1):
    curr_het   = odeint(rise_fall, h0, [0,delta_t], args=(v0,)) #solve the ODE for each time step
    h0          = curr_het[1]
    height[i+1] = h0
    v0          = (height[i+1] - height[i]) / delta_t
    curr_vel[i+1] = v0
    v_diff_prev = v_diff
    v_diff      = curr_vel[i+1] - curr_vel[i]
    if h0 < 0:                           #condition to switch from falling to rising
        switch = 1
        v0     = 0*v0                  #new velocity = coeff of res * previous velocity
    elif v_diff > 0 and v_diff_prev < 0: #condition to identify zero crossing
        switch = 2
        
    #print(h0,v0,check,v_diff,switch)
    
    
plt.figure()
plt.subplot(2,1,1)
plt.plot(ts,height,linewidth=1)
plt.subplot(2,1,2)
plt.plot(ts,curr_vel,linewidth=0.5)
plt.draw()
plt.show()
