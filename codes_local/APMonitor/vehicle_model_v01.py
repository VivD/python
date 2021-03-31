import numpy as np
import matplotlib.pyplot as plt
from scipy import *
from scipy.integrate import odeint

#Simulation time step definition
tf        = 300                 #final time for simulation
nsteps    = 3001                 #number of time steps
delta_t   = tf / (nsteps - 1)   #length of each time step
ts        = np.linspace(0,tf,nsteps)

#Vehicle data
m     = 300                #mass in Kg
load  = 60.0               #total passenger weight in kg
rho   = 1.19               #air density in kg/m^3
A     = 0.7                #area in m^2
Cd    = 0.5                #coefficient of drag dimensionless
Fp    = 30                 #engine power plant force
Fb    = 100                #brake power plant force
Crr   = 0.411              #rolling resistance factor
wh_rd = 0.265              #dynamic rolling radius in m
Fdr   = 4.71               #final drive ratio
gb    = np.array([1.0,3.65,2.15,1.45,1.0,0.83])
ge    = np.array([0.0,0.95,0.95,0.95,0.95,0.95])

#engine data
eng_spd = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000])
eng_trq = np.array([31.93184024, 43.84989124, 52.39157764, 58.77201955, 60.621201, 60.99103728, 59.97387807, 56.73770113, 50.7270955])

#variables assign
vs        = np.zeros(nsteps)   #variable for actual vehicle speed
acc       = np.zeros(nsteps)
wh_sp     = np.zeros(nsteps)
gb_op     = np.zeros(nsteps)
gb_ip     = np.zeros(nsteps)
gb_rat    = np.zeros(nsteps)
gb_eff    = np.zeros(nsteps)
eng_sp    = np.zeros(nsteps)
eng_tq    = np.zeros(nsteps)
es        = np.zeros(nsteps)
ies       = np.zeros(nsteps)
sp_store  = np.zeros(nsteps)
act_ped   = np.zeros(nsteps)
v0        = 0.0                #variable for initial velocity

#Drive cycle data
grade = 0                  #road grade factor

#vehicle plant model
def roadLoad(v,t,u,gear,load):
    if u >= 0:
        dv_dt = (1.0 / (m+load)) * (Fp * u* gear * Fdr - 0.5*rho*Cd*A*v**2 - 2*Crr*(m+load)*np.cos(grade) - (m+load)*9.81*np.sin(grade))
    else:
        dv_dt = (1.0 / (m+load)) * (Fb * u - 0.5*rho*Cd*A*v**2 - Crr*(m+load)*np.cos(grade) - (m+load)*9.81*np.sin(grade))        
    return dv_dt

#gear shift plant model
def g_box(vgear): 
    
    if vgear < 0.2:
        gvar = 0
        evar = ge[gvar]

    elif vgear > 0.2 and vgear <= 7.15111:
        gvar = 1
        evar = ge[gvar]

    elif vgear > 7.15111 and vgear <= 11.1736:
        gvar = 2
        evar = ge[gvar]

    elif vgear > 11.1736 and vgear <= 17.8778:
        gvar = 3
        evar = ge[gvar]

    elif vgear > 17.8778 and vgear <= 20.5594:
        gvar = 4
        evar = ge[gvar]

    else:
        gvar = 5
        evar = ge[gvar]

    return gvar, evar  

#engine plant model
def engine(eng_sp):

    if eng_sp < 1000:
        eng_sp = 1000
    if eng_sp > 9000:
        eng_sp = 9000
        
    for e in range (np.size(eng_spd)):
        esvar = eng_sp - eng_spd[e]
        if esvar <= 1000:
            break

    etvar = eng_trq[e] + (eng_sp - eng_spd[e]) * ((eng_trq[e] - eng_trq[e+1]) / (eng_spd[e] - eng_spd[e+1]))
    return etvar

#Advanced cyber driver
step      = np.zeros(nsteps)   #assigning array for pedal position
#step[11:] = 75.0               #75% @ timestep 11
#step[40:] = -50                #-50% @ timestep 40 to simulate braking
ubias     = 0.0
kc        = 1.0    #0.02
tauI      = 3.0    #0.35
sum_int   = 0
sp        = 25
gear      = 1

#Simulation 
for i in range(nsteps - 1):
    if i == 50/delta_t:
        sp = 0
    if i == 100/delta_t:
        sp = 15
    if i == 150/delta_t:
        sp = 20
    if i == 200/delta_t:
        sp = 10
    if i == 250/delta_t:
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
    if u <= -100:
        u = -100
        sum_int = sum_int - error * delta_t

    act_ped[i+1] = u
        
    v     = odeint(roadLoad,v0,[0,delta_t],args=(u,gear,load))
    v0    = v[-1]
    vgear = v[-1]
    if v0 < 0:
        v0 = 0
    vs[i+1] = v0
    gb_rat[i], gb_eff[i] = g_box(vgear)
    gear      = gb[int(gb_rat[i])]
    acc[i] = (vs[i+1] - vs[i]) / delta_t
    wh_sp[i] = (vs[i])*60 / 2*np.pi*wh_rd
    gb_op[i] = wh_sp[i] * Fdr
    gb_ip[i] = gb_op[i] * gear
    eng_sp   = gb_ip[i]
    eng_tq[i]= engine(eng_sp)
    
    
 
print(f'Top speed in kmph:{max(vs)*3.6: .2f}')

plt.figure()
plt.subplot(3,2,1)
plt.plot(ts,vs,'b-',linewidth=3)
plt.plot(ts,sp_store,'k--',linewidth=2)
plt.ylabel('Velocity (m/s)')
plt.legend(['Velocity (m/s)','Set Point'],loc = 'best')

plt.subplot(3,2,2)
plt.plot(ts,act_ped,'r--',linewidth=3)
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
plt.plot(ts,gb_ip,'b-',linewidth=3)
plt.legend(['Engine Speed'], loc = 'best')
plt.xlabel('Time (sec)')
plt.show()
