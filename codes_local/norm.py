#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
i = 1
count = len(world)

def sense(p, Z):
    q=p
    for i in range(count):
        if Z == world[i]:
            q[i] = p[i] * pHit
        else:
            q[i] = p[i] * pMiss
        i += 1
    
    return q
print (sense(p,Z))
