import numpy as np
import matplotlib.pyplot as plt
n = 360
t = np.arange(0,361,1);
a = np.zeros(n+1)
for i in range(n+1):
    a[i] = np.cos(np.radians(i))
    #print(a[i])
plt.plot(t,a,linewidth=1)
plt.show()