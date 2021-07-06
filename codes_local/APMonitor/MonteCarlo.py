from math import sqrt
import sys
import random
import matplotlib.pyplot as plt 
import numpy as np
sys.setrecursionlimit(3500)
N_trials = 3000
vec      = np.array([0, 0])
a_square = 0
a_circle = 0
i        = 0

def length(x, y):
    return sqrt(x**2 + y**2)

def sim(N_trials):
    val_x = random.uniform(-1.0, 1.0)
    val_y = random.uniform(-1.0, 1.0)
    dist     = length(val_x, val_y)
    if N_trials == 0:
        return vec
    else:
        if dist > 1:
            return sim(N_trials - 1) + np.array([0, 1])
        else:
            return sim(N_trials - 1) + np.array([1, 1]) 
Ac, As = sim(N_trials)
print(4 * Ac/As)
print(sys.getrecursionlimit())