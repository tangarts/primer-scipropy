# Exercise 5.27

from math import e, cos, factorial, pi
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0,15), ylim=(-.5,1.4))
line, = ax.plot([],[])

def init():
    line.set_data([],[])
    return line,

def fk(x,k):
    return (-x)**k/float(factorial(k))

def S(x,N,M):
    s = 0
    for k in range(N,M):
        s += fk(x,k)
    return s

def animate(k):
    x = np.linspace(0,15,256)
    y = fk(x,k)
    line.set_data(x,y)
    return line,
'''
anim = animation.FuncAnimation(fig,animate,frames= range(0,31),\
                               init_func=init, \
                               interval=20, blit=True)
'''
x = np.linspace(0,15,256)
y = S(x,0,31)

print S(1,0,50)