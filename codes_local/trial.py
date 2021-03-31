import numpy as np
import matplotlib.pyplot as plt

a = 2

Y=np.empty(a)
Y2=np.empty(a)



c=[]
d=[]

for i in range(a):
    inp1=int(input("Element of x : "))
    
    c.append(inp1)


for i in range(a):
    inp=int(input("Element of x : "))
    
    d.append(inp)


X=np.array(c)
Y=np.array(d)

print(Y)
print(Y2)  


Y2=2*Y



print(X)
print(Y)
print(Y2)

plt.figure()
plt.subplot(3,2,1)
plt.plot(X,Y)
plt.subplot(3,2,2)
plt.plot(X,Y2)
plt.show()
