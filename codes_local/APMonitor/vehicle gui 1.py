from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


root=Tk()

root.title("VEHICLE MODEL")


#root.geometry("600X600")


#simulation time step defination

label_1=Label(root,text="final time for simulation=").grid(row=0,column=0)


label_2=Label(root,text="no. of time steps=").grid(row=1,column=0)


#taking in the vehicle data


label_3=Label(root,text="mass of vehicle in kg=").grid(row=2,column=0)

label_4=Label(root,text="passenger load in kg=").grid(row=3,column=0)

label_5=Label(root,text="area of vehicle in m^2=").grid(row=4,column=0)

label_6=Label(root,text="coefficient of drag=").grid(row=5,column=0)


label_7=Label(root,text="engine power plant force=").grid(row=6,column=0)

label_8=Label(root,text="brake power plant force=").grid(row=7,column=0)

label_9=Label(root,text="rolling resistance factor=").grid(row=8,column=0)



label_10=Label(root,text="wheel radius in m =").grid(row=9,column=0)



label_11=Label(root,text="final drive ratio =").grid(row=10,column=0)

label_12=Label(root,text="final drive ratio efficiency =").grid(row=11,column=0)

label_13=Label(root,text="wheel inertia=").grid(row=12,column=0)

label_14=Label(root,text="number of gears =").grid(row=13,column=0)
label_15=Label(root,text="maximun engine rpm =").grid(row=14,column=0)


##########################################################################

#store all values

array_1=[]
a=[]
array_2=[]

array_4=[]
b=[]
array_5=[]

array_6=[]
c=[]
array_7=[]

array_10=[]
array_11=[]
array_12=[]
array_13=[]
array_14=[]
array_15=[]
array_16=[]
c=[]
d=[]

for i in range(15):
    
   array_1.append(StringVar())


   a.append(Entry(root,textvariable=array_1[i]).grid(row=0+i,column=1))

   


#####function just to take values of gb anf ge

def tqeffic():
  for i in range(15):

    # if i==14:
       # array_2.append(int(array_1[i].get()))
        #break
      
     array_2.append(float(array_1[i].get()))
        
  array_3=np.array(array_2)## used to store initial values of page 1

  intvar=int(array_2[14])
  
  eng_spd=np.linspace(1000,int(intvar),int(intvar*.001))  ## for filling speed values

  print(eng_spd)
  #for i in range(14):  used to print 
     #lb=Label(text=array_2[i]).grid(row=12+i,column=2)
  
  
  label_16=Label(root,text="transmission ratios for each gear=").grid(row=15,column=0)

  label_17=Label(root,text="gear torque transmission efficiency=").grid(row=16,column=0)

  
  for i in range(int(array_3[13])):
      array_4.append(StringVar())   # for gb
      
      b.append(Entry(root,textvariable=array_4[i]).grid(row=15,column=1+i))
      
      array_6.append(StringVar())# for ge
      
      c.append(Entry(root,textvariable=array_6[i]).grid(row=16,column=1+i))

      
  def fill():
        for i in range(int(array_3[13])):
            array_5.append(float(array_4[i].get()))

            array_7.append(float(array_6[i].get()))

        array_8=np.array(array_5)  #storing gb values as np array

        array_9=np.array(array_7)  # storing ge values as np array

        
  label_18=Label(text="speed values").grid(row=17,column=0)
  label_18=Label(text="engine torque").grid(row=17,column=1)
  label_18=Label(text="engine brake").grid(row=17,column=2)


  def finalize():
     for i in range(len(eng_spd)):
        array_11.append(float(array_10[i].get()))

        array_14.append(float(array_13[i].get()))
        
     array_12=np.array(array_11)
     array_15=np.array(array_14)
        
    # print(array_12)
     #print(array_15)
  
  
  for i in range(len(eng_spd)):
                 label=Label(text=eng_spd[i]).grid(row=18+i,column=0)
                 array_10.append(StringVar())
                 c.append(Entry(root,textvariable=array_10[i]).grid(row=18+i,column=1))

                 array_13.append(StringVar())
                 d.append(Entry(root,textvariable=array_13[i]).grid(row=18+i,column=2))

   

  btn_3=Button(text="finilize",command=finalize).grid(row=18+len(eng_spd),column=3) 
        
  btn_2=Button(text="OK",command=fill).grid(row=15 ,column=int(array_3[13])+1) ## button to store the values for gb and ge
      
 
    
  
btn_1=Button(text="continue",command=tqeffic).grid(row=12,column=3)  #button to take the values for gb and ge  
  
#eng_spd=np.linspace(1000,array_3,(array_3)/1000)







##########################################################################

#main program##

def go():
   intvar=int(array_2[14])# max speed
   tf        = int(array_2[0])               #final time for simulation
   nsteps    = int(array_2[1])               #number of time steps
   delta_t   = tf / (nsteps - 1)   #length of each time step
   ts        = np.linspace(0,tf,nsteps)

#Vehicle data


   m     = array_2[3]                 #mass in Kg
   load  = array_2[4]                #total passenger weight in kg
   rho   = 1.19               #air density in kg/m^3
   A     = array_2[5]                #area in m^2
   Cd    = array_2[6]                 #coefficient of drag dimensionless
   Fp    = array_2[7]                  #engine power plant force
   Fb    = array_2[8]                  #brake power plant force
   Crr   = array_2[9]              #rolling resistance factor
   wh_rd = array_2[10]               #dynamic rolling radius in m
   Fdr   = array_2[11]                #final drive ratio
   Fef   = array_2[12]               #final drive ratio efficiency
   wh_in = array_2[13]                  #wheel inertia
   gb    = np.array(array_5)#np.array([1.0,3.65,2.15,1.45,1.0,0.83])#np.array(array_5)#
   ge    = np.array(array_7)#np.array([0.0,0.95,0.95,0.95,0.95,0.95])#np.array(array_7)#
   ws    = 0.0

#engine data


   eng_i   = 0.1
   eng_spd = np.linspace(1000,int(intvar),int(intvar*.001))#np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000])
   eng_trq = np.array(array_11)#np.array([31.93184024, 43.84989124, 52.39157764, 58.77201955, 60.621201, 60.99103728, 59.97387807, 56.73770113, 50.7270955])#np.array(array_11)#
   eng_brk = np.array(array_14)#np.array([0, -1.619401501, -2.80112692, -3.588943867, -4.245457989, -4.639366462, -5.033274935, -5.252112976, -5.3834158])#np.array(array_14)#

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
   print(array_2)
   print(array_5)
   print(array_7)
   print(array_11)
   print(array_14)
#Drive cycle data


   grade = 0                  #road grade factor

#vehicle plant model


   def roadload(ws,t,whl_t,u):
       Iw    = ((m + load)*wh_rd**2) + wh_in
       if u >= 0:
           dw_dt = 1/Iw * (whl_t - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
       else:
           dw_dt = 1/Iw * (Fb*u*wh_rd - 0.5*rho*Cd*A*wh_rd**3*ws**2 - wh_rd*Crr*(m+load)*np.cos(grade)*ws - wh_rd*(m+load)*9.81*np.sin(grade))
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
   kc        = 5.0#15.02#333.02#27.0     #0.02
   tauI      = 1.0#2.35#47.35#3.9    #0.35
   sum_int   = 0
   sp        = 0
   gear      = 1

#Simulation

   for i in range(nsteps - 1):
    if i == 5/delta_t:
        sp = 7
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
    act_ped[i+1] = u

    if u > 0:
        eng_tq[i+1]= eng_wot(eng_w) * act_ped[i+1]/100
    if u <= 0:
        eng_tq[i+1]= eng_wot(eng_w)

    gb_rat[i+1], gb_eff[i+1] = g_box(vgear)
    gear       = gb[int(gb_rat[i+1])]
    gb_ipt[i+1]  = eng_tq[i+1]
    gb_opt[i+1]  = gb_ipt[i+1] * gear * gb_eff[i+1]

    wh_spt[i+1]  = gb_opt[i+1] * Fdr * Fef
    whl_t      = wh_spt[i+1]
    wh_spd     = odeint(roadload, ws, [0,delta_t], args=(whl_t,u))
    ws         = wh_spd[-1]
    wh_sp[i+1]   = ws
    gb_op[i+1]   = wh_sp[i+1] * Fdr
    gb_ip[i+1]   = gb_op[i+1] * gear
    eng_sp[i+1]  = gb_ip[i+1] * 60 / (2 * np.pi)
    if eng_sp[i+1] < eng_wmin:
        eng_sp[i+1] = eng_wmin
    eng_w      = eng_sp[i+1]
    vs[i+1]    = wh_sp[i+1] * wh_rd
    v0         = vs[i+1]
    vgear      = vs[i+1]
    acc[i] = (vs[i+1] - vs[i]) / (delta_t * 9.81)
    
 
   print(f'Top speed in kmph:{max(vs)*3.6: .2f}')


#plotting


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
   plt.plot(ts, eng_sp, 'b-',linewidth=3)
   plt.legend(['Engine Speed'], loc = 'best')
   plt.xlabel('Time (sec)')
   plt.show()

   




btn=Button(text="go",command=go).grid(row=40,column=20)
root.mainloop()
