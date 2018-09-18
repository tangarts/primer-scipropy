import random as rnd
import numpy as np
import matplotlib.pyplot as plt

# 1-D

Np = 50
ns = 200
positions = np.zeros(Np)
head = 1 ; tail = 2
'''
for step in range(ns):
    for p in range(Np):
        coin = rnd.randint(1,2)
        if coin == head:
            positions[p] += 1
        elif coin == tail:
            positions[p] -= 1
       
plt.plot(positions,np.zeros(Np),'ko')
plt.xlim(-2.5*np.sqrt(ns),2.5*np.sqrt(ns))
plt.ylim(-.2,.2)
plt.title('Random walk of %d particles after %d steps' %(Np,step+1))
plt.show()
'''
#vectorisation

moves= np.random.randint(1,3,size=Np*ns)
moves = 2*moves-3
print moves