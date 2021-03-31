import numpy as np
import matplotlib.pyplot as plt

p = 23 # modulo
g = 5  # base
s = np.linspace(0, 100, num=1000)
v = np.zeros(1000)
#client to server
secvalCS = 4
#server to client
secvalSC = 3

for i in range(len(s)):
  v[i] = np.mod(g**s[i], p)

plt.figure()
plt.plot(s, v, linewidth = 2)
plt.grid()
plt.show()
