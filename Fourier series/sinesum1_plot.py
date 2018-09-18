# Exercise 5.29
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from sinesum1 import f, S

T = 2*pi

xlist  = [x/10. for x in range(-100,101)]

ylist = [S(1,n,T) for n in xlist]

print xlist