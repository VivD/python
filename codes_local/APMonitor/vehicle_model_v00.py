import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Simulation time step definition
tf        = 300.0               #final time for simulation
nsteps    = 301                 #number of time steps
delta_t   = tf  / (nsteps - 1)   #length of each time step
ts        = np.linspace(0,tf,nsteps)

#Vehicle data
m     = 500                #mass in Kg
load  = 200.0              #total passenger weight in kg
rho   = 1.19               #air density in kg/m^3
A     = 7.58               #area in m^2
Cd    = 0.7                #coefficient of drag dimensionless
Fp    = 30                 #engine power plant force
Fb    = 100                #brake power plant force
Crr   = 0.411              #rolling resistance factor
wh_rd = 0.265              #dynamic rolling radius in m
Fdr   = 4.71               #final drive ratio
ge    = np.array([1.0,3.65,2.15,1.45,1.0,0.83])

#variables assign
vs        = np.zeros(nsteps)   #variable for actual vehicle speed
acc       = np.zeros(nsteps)
wh_sp     = np.zeros(nsteps)
gb_op     = np.zeros(nsteps)
gb_ip     = np.zeros(nsteps)
gb_rat    = np.zeros(nsteps)
eng_sp    = np.zeros(nsteps)
es        = np.zeros(nsteps)
ies       = np.zeros(nsteps)
sp_store  = np.zeros(nsteps)
v0        = 0.0                #variable for initial velocity

#Drive cycle data
grade = 0                  #road grade factor

#vehicle plant model
def roadLoad(v,t,u,gear,load):
    if u >= 0:
        dv_dt = (1.0 / (m+load)) * (Fp * u * gear * Fdr - 0.5*rho*Cd*A*v**2 - Crr*(m+load)*np.cos(grade) - (m+load)*9.81*np.sin(grade))
    else:
        dv_dt = (1.0 / (m+load)) * (Fb * u - 0.5*rho*Cd*A*v**2 - Crr*(m+load)*np.cos(grade) - (m+load)*9.81*np.sin(grade))        
    return dv_dt

#gear shift plant model
def g_box(vgear): 
    
    if vgear < 0.2:
        g = 0

    elif vgear > 0.2 and vgear <= 7.15111:
        g = 1

    elif vgear > 7.15111 and vgear <= 11.1736:
        g = 2

    elif vgear > 11.1736 and vgear <= 17.8778:
        g = 3

    elif vgear > 17.8778 and vgear <= 20.5594:
        g = 4 

    else:
        g = 5

    return g   

#Advanced cyber driver
step      = np.zeros(nsteps)   #assigning array for pedal position
#step[11:] = 75.0               #75% @ timestep 11
#step[40:] = -50                #-50% @ timestep 40 to simulate braking
ubias     = 0.0
kc        = 2.0
tauI      = 10
sum_int   = 0
sp        = 25
gear      = 1

#Simulation 
for i in range(nsteps - 1):
    if i == 50:
        sp = 0
    if i == 100:
        sp = 15
    if i == 150:
        sp = 20
    if i == 200:
        sp = 10
    if i == 250:
        sp = 0
    sp_store[i+1] = sp
    error = sp - v0
    es[i+1] = error
    sum_int = sum_int + error * delta_t
    u = ubias + kc*error + kc/tauI * sum_int
    ies[i+1] = sum_int
    step[i+1] = u

    if u >= 100.0:
        u = 100.0
        sum_int = sum_int - error * delta_t
    if u <= -50:
        u = -50
        sum_int = sum_int - error * delta_t
        
    v     = odeint(roadLoad,v0,[0,delta_t],args=(u,gear,load))
    v0    = v[-1]
    vgear = v[0]
    if v0 < 0:
        v0 = 0
    vs[i+1] = v0
    gb_rat[i] = g_box(vgear)
    gear      = ge[int(gb_rat[i])]
    acc[i] = (v[1] - v[0]) / delta_t
    wh_sp[i] = (v[0])*60 / 2*np.pi*wh_rd
    gb_op[i] = wh_sp[i] * Fdr
    gb_ip[i] = gb_op[i] * gear
    eng_sp[i]= gb_ip[i]
 
print(f'Top speed in kmph:{max(vs)*3.6: .2f}')

plt.figure()
plt.subplot(3,2,1)
plt.plot(ts,vs,'b-',linewidth=3)
plt.plot(ts,sp_store,'k--',linewidth=2)
plt.ylabel('Velocity (m/s)')
plt.legend(['Velocity (m/s)','Set Point'],loc = 'best')

plt.subplot(3,2,2)
plt.plot(ts,step,'r--',linewidth=3)
plt.ylabel('Gas Pedal')
plt.legend(['Gas Pedal (%)'], loc = 'best')
plt.xlabel('Time (sec)')
    
plt.subplot(3,2,3)
plt.plot(ts,wh_sp,'b--',linewidth=3)
plt.legend(['Wheel Speed'], loc = 'best')
plt.xlabel('Time (sec)')

plt.subplot(3,2,4)
plt.plot(ts,acc,'k--',linewidth=3)
plt.legend(['Vehicle Acceleration'], loc = 'best')
plt.xlabel('Time (sec)')

plt.subplot(3,2,5)
plt.plot(ts,gb_rat,'k-',linewidth=3)
plt.legend(['Current Gear'], loc = 'best')
plt.xlabel('Time (sec)')

plt.subplot(3,2,6)
plt.plot(ts,eng_sp,'b-',linewidth=3)
plt.legend(['Engine Speed'], loc = 'best')
plt.xlabel('Time (sec)')
plt.show()
