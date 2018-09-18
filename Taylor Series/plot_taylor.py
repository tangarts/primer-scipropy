from math import factorial,pi,sin
import numpy as np

def S(x,n):
    s = 0
    for j in range(0,n+1):
        s += (-1)**j*x**(2*j+1)/float(factorial(2*j+1))
    return s

import matplotlib.pyplot as plt 

xplot = np.linspace(0,4*pi,256)

plt.plot(xplot,S(xplot,1))
plt.plot(xplot,S(xplot,12))
plt.plot(xplot,S(xplot,50))
plt.xlabel('x')
plt.ylabel('S(x)')
plt.axis([0,4*pi,-10,10])
plt.show()

