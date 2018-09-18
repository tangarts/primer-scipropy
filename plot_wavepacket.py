#Exercise 5.15 & 5.21 Plot and animate a wave packet

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def f(x,t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

fig = plt.figure()
ax = plt.axes(xlim=(-6,6),ylim=(-2,2))
line, = ax.plot([],[])
ax.set_title('Animation of a wave packet')

def init():
    line.set_data([],[])
    return line,

def animate(t):
    x = np.linspace(-6,6,256)
    y = f(x,t)
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig,animate,np.linspace(-2,2),\
                               init_func=init, \
                               interval=20, blit=True)

plt.show()