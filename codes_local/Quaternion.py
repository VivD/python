import numpy as np

def euler_to_quaternion(angles):
    roll = angles[0]
    pitch = angles[1]
    yaw = angles[2]
    
    # TODO: complete the conversion
    # and return a numpy array of
    # 4 elements representing a quaternion [a, b, c, d]
    ans = np.eye(4)
    r1 = np.array(np.cos(yaw/2), 0, 0, np.sin(yaw/2))
    print(str(r1)) 
    r2 = np.array(np.cos(pitch/2), 0, np.sin(pitch/2), 0)
    print(str(r2))
    r3 = np.array(np.cos(roll/2), np.sin(roll/2), 0, 0)

    ans = np.dot(ans, r3)
    print(ans)
    ans = np.dot(r2, np.array(ans))
    print(ans)
    ans = np.dot(r1, np.array(ans))
    return str(ans)                

def quaternion_to_euler(quaternion):
    a = quaternion[0]
    b = quaternion[1]
    c = quaternion[2]
    d = quaternion[3]
    
    # TODO: complete the conversion
    # and return a numpy array of
    # 3 element representing the euler angles [roll, pitch, yaw]

euler = np.array([np.deg2rad(90), np.deg2rad(30), np.deg2rad(0)])

q = euler_to_quaternion(euler) # should be [ 0.683  0.683  0.183 -0.183]
print(q)

#assert np.allclose(euler, quaternion_to_euler(q))
