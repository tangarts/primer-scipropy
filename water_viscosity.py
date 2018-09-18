#Exercise 5.30
import numpy as np
import matplotlib.pyplot as plt

def mu(T):
    A = 2.414E-5 #Pa s
    B = 247.8 #K
    C = 140. #K
    return A*10**(B/(T-C))

C = range(101)
T = [i + 273 for i in C]
viscosity = [mu(i) for i in T]

fig = plt.figure()
ax = fig
