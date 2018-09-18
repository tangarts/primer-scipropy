import random as rnd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(xlim=(0,1),ylim=(0,1))

npart = 10
nsteps = 100

xpos = np.random.rand(npart); ypos = np.random.rand(npart)
plt.plot(xpos,ypos,'ro')

plt.show()