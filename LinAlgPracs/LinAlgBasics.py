import numpy as np

A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
print(A)
print()

A = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
B = A[[0, 2], 1:]
print(B)
print()

a = np.array([1, 2, 3, 4])
b = np.ones((5, 5))
print(b)
print()
b = np.ones(5, )
print(b)
print()
b = a[:2]
print(b)
print()
b = a[4:]
print(b)
print()
b = a[:5]
print(b)
print()
#b = np.ones(5, 5)
#b = a[4]
##b = a[:2, :2]

# x = np.random.rand(100)
# print(x)
# print()

x = np.array([1, 2, 3, 4, 5])
y = x**3
print(y)
print()

# we haven't figured this out yet, this is question number 7
x = np.array([1, 2, 3, 4, 5])
(x > 1)[:3] # The following piece of code returns the numerical indices of the first three elements of the one-dimensional array x that are greater than 1.
(x > 1).nonzero()[0][:3] # The following piece of code returns the numerical indices of the first three elements of the one-dimensional array x that are greater than 1.
# The nonzero() method returns a tuple of arrays, one for each dimension of the input array, containing the indices of the non-zero elements.
# The [0] index is used to access the first array in the tuple, which contains the row indices of the non-zero elements.
# The [:3] index is used to select the first three elements of this array.
# The result is an array of the indices of the first three elements of x that are greater than 1.

# import pdb; pdb.set_trace()
# x = np.arange(5)
# y = -np.arange(5)
# x[y < -2] = 0
# x *= 9
# print(x)

# data = {'a': 3, 'c': 9, 'b': 5}
# data['b'] = 100
# print(data)
# 7, 8, 13 are not done yet.
x = 5
y = x in [2, 5, 9]
print(y)
print()

if x in [2, 5, 9]:
    y = True
else:
    y = False

print(y)
print()

y = False
if x in [2, 5, 9]:
    y = True

print(y)
print()
# if x == [2, 5, 9]:
#     y = True
# else:
#     y = False

# print(y)
# print()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x,y)
plt.show()