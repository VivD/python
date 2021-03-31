import numpy as np
import matplotlib.pyplot as plt
#from mpldatacursor import datacursor

theta = np.linspace(0, 360, 360)
x     = np.matrix([[3], [2]])
xx    = np.zeros(np.size(theta))
yy    = np.zeros(np.size(theta))
for i in range(np.size(theta)):
    stiff = np.matrix([[np.cos(theta[i]* np.pi / 180.), -np.sin(theta[i]* np.pi / 180.)], [np.sin(theta[i]* np.pi / 180.), np.cos(theta[i]* np.pi / 180.)]])
    #xx[i] = stiff*x
    yy[i] = np.transpose(x)*stiff*x

datacursor()
plt.plot(theta, yy)
plt.grid(True)
plt.show()