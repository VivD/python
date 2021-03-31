import numpy as np
import matplotlib.pyplot as plt
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
Fb    = 50                 #brake power plant force
Crr   = 0.005              #rolling resistance factor
wh_rd = 0.265              #dynamic rolling radius in m
Igb_i = 0.2                #gearbox input inertias
Igb_o = 0.2                #gearbox output inertias
Fdr   = 4.71               #final drive ratio
Fef   = 0.9604             #final drive ratio efficiency
wh_inr= 0.4                #wheel inertia rear
wh_inf= 0.35               #wheel inertia front
mdamp = 0.35
vdamp = 0.15
gb    = np.array([1.0,3.65,2.15,1.45,1.0,0.83])
ge    = np.array([0.0,0.95,0.95,0.95,0.95,0.95])
ws    = 0.0

#engine data
eng_i   = 0.1
eng_spd = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000])
eng_trq = np.array([31.93184024, 43.84989124, 52.39157764, 58.77201955, 60.621201, 60.99103728, 59.97387807, 56.73770113, 50.7270955])
eng_brk = np.array([0, -1.619401501, -2.80112692, -3.588943867, -4.245457989, -4.639366462, -5.033274935, -5.252112976, -5.3834158])

#variables assign
vs        = np.zeros(nsteps)   #variable for actual vehicle speed
acc       = np.zeros(nsteps)
wh_sp     = np.zeros(nsteps)
wh_spt    = np.zeros(nsteps)
gb_op     = np.zeros(nsteps)
gb_opt    = np.zeros(nsteps)
gb_ip     = np.zeros(nsteps)
gb_ipt    = np.zeros(nsteps)
gb_rat    = np.zeros(nsteps)
gb_eff    = np.zeros(nsteps)
eng_sp    = np.zeros(nsteps)
eng_tq    = np.zeros(nsteps)
eng_re    = np.zeros(nsteps)
es        = np.zeros(nsteps)
ies       = np.zeros(nsteps)
sp_store  = np.zeros(nsteps)
act_ped   = np.zeros(nsteps)
test      = np.zeros(nsteps)
v0        = 0.0                #variable for initial velocity
eng_wmin  = 1000
eng_wmax  = 9000
eng_w     = eng_wmin
eng_t     = 0
vgear     = 0.0

#Drive cycle data
grade = 0                  #road grade factor

#vehicle plant model
def roadload(ws,t,whl_t,u):
    Iw    = ((m + load)*wh_rd**2) + wh_inf + wh_inr
    if u >= 0:
        dw_dt = 1/Iw * (whl_t - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
    else:
        if v0 > 0.1:
            dw_dt = 1/Iw * (Fb*u*wh_rd - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
        else:
            dw_dt = 1/Iw * (Fb*0*wh_rd - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
    return dw_dt

#gear shift plant model & efficiency
def g_box(vgear):
    gvar = 0
    evar = 0
    if u > 0 or u < 0:
        gvar = 1
        evar = ge[gvar]
    else:
        gvar = 0
        evar = ge[gvar]
        
    if vgear > 0.2 and vgear <= 7.15111:
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

    elif vgear > 20.5594:
        gvar = 5
        evar = ge[gvar]

    return gvar, evar  

#engine wide open throttle torque table
def eng_wot(eng_w):

    if eng_w < 1000:
        eng_w = 1000
    if eng_w > 9000:
        eng_w = 9000
        
    for e in range (np.size(eng_spd)):
        esvar = eng_w - eng_spd[e]
        if esvar <= 1000:
            break
    if u > 0:
        etvar = eng_trq[e] + (eng_w - eng_spd[e]) * ((eng_trq[e] - eng_trq[e+1]) / (eng_spd[e] - eng_spd[e+1]))
    if u <= 0:
        etvar = eng_brk[e] + (eng_w - eng_spd[e]) * ((eng_brk[e] - eng_brk[e+1]) / (eng_spd[e] - eng_spd[e+1]))
    return etvar

def eng_dyn(eng_sp, t):        
    dw_dt = (vart / eng_i) + (Fc * wh_rd * Fef * Fdr * gear)
    return dw_dt

#Advanced cyber driver
step      = np.zeros(nsteps)   #assigning array for pedal position
#step[11:] = 75.0               #75% @ timestep 11
#step[40:] = -50                #-50% @ timestep 40 to simulate braking
ubias     = 0.0
kc        = 15.0
tauI      = 09.0
sum_int   = 0
sp        = 0
gear      = 1

#Simulation 
for i in range(nsteps - 1):
    if i == 5/delta_t:
        sp = 25
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
    u = ubias + kc*error + tauI * sum_int
    ies[i+1] = sum_int
    step[i+1] = u

    if u >= 100.0:
        u = 100.0
        sum_int = sum_int - error * delta_t
    if u <= -50:
        u = -50
        sum_int = sum_int - error * delta_t

    if v0 < 0.1 and u < 0:
        act_ped[i+1] = -50
    else:
        act_ped[i+1] = u

    if u > 0:
        eng_tq[i+1]= eng_wot(eng_w) * act_ped[i+1]/100
    if u <= 0:
        eng_tq[i+1]= eng_wot(eng_w)

    gb_rat[i+1], gb_eff[i+1] = g_box(vgear)
    gear       = gb[int(gb_rat[i+1])]
    gb_ipt[i+1]  = eng_tq[i+1] #- Igb_i * (gb_ip[i] - gb_ip[i-1])/delta_t #+ vdamp * gb_ip[i] #** 2 #+ mdamp * gb_ip[i]
    gb_opt[i+1]  = gb_ipt[i+1] * gear * gb_eff[i+1] - (Igb_o + Igb_i) * (gb_op[i] - gb_op[i-1])/delta_t
    wh_spt[i+1]  = gb_opt[i+1] * Fdr * Fef - (wh_inf + wh_inr) * (wh_sp[i] - wh_sp[i-1])/delta_t
    whl_t      = wh_spt[i+1]
    wh_spd     = odeint(roadload, ws, [0,delta_t], args=(whl_t,u))
    ws         = wh_spd[-1]
    wh_sp[i+1]   = ws
    gb_op[i+1]   = wh_sp[i+1] * Fdr
    gb_ip[i+1]   = gb_op[i+1] * gear
    eng_sp[i+1]  = gb_ip[i+1] * 60 / (2 * np.pi)
    if eng_sp[i+1] < eng_wmin:
        eng_sp[i+1] = eng_wmin
    if eng_sp[i+1] > eng_wmax:
        eng_sp[i+1] = eng_wmax
    eng_w      = eng_sp[i+1]
    vs[i+1]    = wh_sp[i+1] * wh_rd
    v0         = vs[i+1]
    vgear      = vs[i+1]
    acc[i] = (vs[i+1] - vs[i]) / (delta_t * 9.81)
   
 
print(f'Top speed in kmph:{max(vs)*3.6: .2f}')

plt.figure()
plt.subplot(3,2,1)
plt.plot(ts,vs,'b-',linewidth=3)
plt.plot(ts,sp_store,'k--',linewidth=2)
plt.ylabel('Velocity [m/s]')
plt.legend(['Velocity [m/s]','Set Point [m/s]'],loc = 'best')

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
plt.plot(ts, eng_sp, 'b-',linewidth=3)
plt.legend(['Engine Speed'], loc = 'best')
plt.xlabel('Time (sec)')
plt.show()
