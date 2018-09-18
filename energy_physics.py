#Exercise 5.45
import sys
import numpy as np
from matplotlib import pyplot

class Energy:
    def __init__(self,g,v0,m):
        self.g = 9.81
        self.v0 = v0
        self.m = m

    def y(self,t):
        self.y = self.v0*t-.5*self.g*t**2
        return self.y
    
    def v(self,t):
        v = self.v0-self.g*t
        return v
    
#plot P, K and P+K t [0,2*v0/g]

print Energy.v(10)