from apm import *
import numpy as np

def init_mhe(s,a):
    apm(s,a,'clear all')
    # load model and data files
    apm_load(s,a,'mhe.apm')
    csv_load(s,a,'mhe.csv')
    # classify variables
    apm_info(s,a,'FV','ua')
    apm_info(s,a,'MV','tc')
    apm_info(s,a,'SV','ca')
    apm_info(s,a,'CV','t')
    # options
    apm_option(s,a,'nlc.imode',5) # 5 = MHE
    apm_option(s,a,'nlc.ev_type',1) # 1 = l1-norm, 2 = sq_error
    apm_option(s,a,'nlc.nodes',3) # 3 = collocation nodes
    apm_option(s,a,'nlc.solver',3) # 3 = IPOPT
    # FV tuning
    apm_option(s,a,'ua.status',1) # estimate this parameter
    apm_option(s,a,'ua.fstatus',0) # no measurement (feedback status)
    apm_option(s,a,'ua.lower',10000) # lower bound
    apm_option(s,a,'ua.upper',100000) # upper bound
    # MV tuning
    apm_option(s,a,'tc.status',0) # don't estimate this parameter
    apm_option(s,a,'tc.fstatus',1) # measurement available (feedback status)
    # CV tuning
    apm_option(s,a,'t.status',1) # estimate this parameter
    apm_option(s,a,'t.fstatus',1) # measurement available (feedback status)
    apm_option(s,a,'t.meas_gap',0.1) # measurement deadband gap

    msg = 'MHE Initialized'
    return msg

def init_sim(s,a):
    apm(s,a,'clear all')
    # load model and data files
    apm_load(s,a,'sim.apm')
    csv_load(s,a,'sim.csv')
    # classify variables
    apm_info(s,a,'FV','ua')
    apm_info(s,a,'MV','tc')
    apm_info(s,a,'SV','ca')
    apm_info(s,a,'SV','t')
    # options
    apm_option(s,a,'nlc.imode',4) # 4 = simulation
    apm_option(s,a,'nlc.nodes',3) # 3 = collocation nodes
    apm_option(s,a,'nlc.solver',3) # 3 = IPOPT
    # MV tuning
    apm_option(s,a,'tc.fstatus',1) # measurement available (feedback status)
    msg = 'Simulator Initialized'
    return msg

# specify server and application name
s = 'http://byu.apmonitor.com'
# name for the process
a1 = 'sim'
# name for the model / estimator
a2 = 'mhe'

# initialize cstr simulator (plant)
msg = init_sim(s,a1)
print (msg)
# initialize moving horizon estimation (model)
msg = init_mhe(s,a2)
print (msg)

# number of cycles to run
cycles = 50

# step in the jacket cooling temperature at cycle 6
Tc_meas = np.empty(cycles)
Tc_meas[0:5] = 280
Tc_meas[5:cycles] = 300
dt = 0.1 # min
time = np.linspace(0,cycles*dt-dt,cycles) # time points

# allocate storage
Ca_meas = np.empty(cycles)
T_meas = np.empty(cycles)
UA_mhe = np.empty(cycles)
Ca_mhe = np.empty(cycles)
T_mhe = np.empty(cycles)

for i in range (0,cycles):
    
    ## Process
    # input Tc (jacket cooling temperature)
    apm_meas(s,a1,'Tc',Tc_meas[i])
    # solve process model, 1 time step
    output = apm(s,a1,'solve')
    # retrieve Ca and T measurements from the process
    Ca_meas[i] = apm_tag(s,a1,'Ca.model')
    T_meas[i] = apm_tag(s,a1,'T.model')
    
    ## Estimator
    # input process measurements, don't use Ca_meas
    # input Tc (jacket cooling temperature)
    apm_meas(s,a2,'Tc',Tc_meas[i])
    # input T (reactor temperature)
    apm_meas(s,a2,'T',T_meas[i])
    # solve process model, 1 time step
    output = apm(s,a2,'solve')
     # check if successful
    if (apm_tag(s,a2,'nlc.appstatus')==1):
        # retrieve solution
        UA_mhe[i] = apm_tag(s,a2,'UA.newval')
        Ca_mhe[i] = apm_tag(s,a2,'Ca.model')
        T_mhe[i] = apm_tag(s,a2,'T.model')
    else:
        # display failed run
        print (output)        
        # failed solution
        UA_mhe[i] = 0
        Ca_mhe[i] = 0
        T_mhe[i] = 0
        
    print ('MHE results: Ca (estimated)=' + str(Ca_mhe[i]) + \
        ' Ca (actual)=' + str(Ca_meas[i]) + \
        ' UA (estimated)=' + str(UA_mhe[i]) + \
        ' UA (actual)=50000')
    
    # open web-viewer on first cycle
    if i==1:
        apm_web(s,a2)

# plot results
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(411)
plt.plot(time,Tc_meas,'k-',linewidth=2)
plt.ylabel('Jacket T (K)')
plt.legend('T_c')

plt.subplot(412)
plt.plot([0,time[-1]],[50000,50000],'k--')
plt.plot(time,UA_mhe,'r:',linewidth=2)
plt.axis([0,time[-1],10000,100000])
plt.ylabel('UA')
plt.legend(['Actual UA','Predicted UA'])

plt.subplot(413)
plt.plot(time,T_meas,'ro')
plt.plot(time,T_mhe,'b-',linewidth=2)
plt.ylabel('Reactor T (K)')
plt.legend(['Measured T','Predicted T'])

plt.subplot(414)
plt.plot(time,Ca_meas,'go')
plt.plot(time,Ca_mhe,'m-',linewidth=2)
plt.ylabel('Reactor C_a (mol/L)')
plt.legend(['Measured C_a','Predicted C_a'])
plt.show()
