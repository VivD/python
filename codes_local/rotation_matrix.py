#import matplotlib.pyplot as plt 
#from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from enum import Enum

#%matplotlib inline
np.set_printoptions(precision=3, suppress=True)

#plt.rcParams["figure.figsize"] = [12, 12]

class Rotation(Enum):
    ROLL = 0
    PITCH = 1
    YAW = 2  


class EulerRotation:
    
    def __init__(self, rotations):
        """
        `rotations` is a list of 2-element tuples where the
        first element is the rotation kind and the second element
        is angle in degrees.
        
        Ex:
        
            [(Rotation.ROLL, 45), (Rotation.YAW, 32), (Rotation.PITCH, 55)]
            
        """
        self._rotations = rotations
        self._rotation_map = {Rotation.ROLL : self.roll, Rotation.PITCH : self.pitch, Rotation.YAW : self.yaw}

    def roll(self, phi):
        """Returns a rotation matrix along the roll axis"""
        return np.array([[1., 0, 0],
                         [0, np.cos(phi), -np.sin(phi)],
                         [0, np.sin(phi), np.cos(phi)]]) 
    
    def pitch(self, theta):
        """Returns the rotation matrix along the pitch axis"""
        return np.array([[np.cos(theta), 0, np.sin(theta)],
                         [0., 1, 0],
                         [-np.sin(theta), 0, np.cos(theta)]])

    def yaw(self, psi):
        """Returns the rotation matrix along the yaw axis"""
        return np.array([[np.cos(psi), -np.sin(psi), 0],
                         [np.sin(psi), np.cos(psi), 0],
                         [0., 0, 1]])

    def rotate(self):
        """Applies the rotations in sequential order"""
        t = np.eye(3)
        for r in self._rotations:
            kind = r[0]
            angle = np.deg2rad(r[1])
            t = np.dot(self._rotation_map[kind](angle), t)
        return t

# Test your code by passing in some rotation values
rotations = [
    (Rotation.ROLL, 25),
    (Rotation.PITCH, 75),
    (Rotation.YAW, 90),
]

R = EulerRotation(rotations).rotate()
print('Rotation matrix ...')
print(R)
##phi = 45
##phi_rad = np.deg2rad(45)
##print(str(phi_rad))
# Should print
# Rotation matrix ...
# [[ 0.    -0.906  0.423]
#  [ 0.259  0.408  0.875]
#  [-0.966  0.109  0.235]]
