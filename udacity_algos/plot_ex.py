import numpy as np
import matplotlib.pyplot as plt
import math as m

t = np.linspace(0,6,100)
y = np.sin(m.pi*t/2)
z = np.sin(m.pi*t) + np.cos(m.pi*t)

#print(t)

plt.plot(t,y,'r--')
plt.plot(t,z)
plt.show()
