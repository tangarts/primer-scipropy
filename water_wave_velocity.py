#Exercise 5.31
import numpy as np
from matplotlib import pyplot as plt

def c(l):
    g = 9.81 #m/s**2
    s = 7.9e-2 #N/m
    rho = 1000 #kg/m**3
    h = 50 #m
    return np.sqrt((g*l/2*np.pi)*(1+s*(4*np.pi**2)/rho*g*l**2)*np.tanh(2*np.pi*h/l))

xplot = np.linspace(1, 2e3)
yplot = c(xplot)

plt.plot(xplot,yplot)
plt.show()