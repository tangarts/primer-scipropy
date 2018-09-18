import random 
import numpy as np

def MCint(f,a,b,n):
    s=0
    for i in range(n):
        x = random.uniform(a,b)
        s+=f(x)
    I = (float(b-a)/n)*s
    return I

def MCint_vec(f,a,b,n):
    x = np.random.uniform(a,b,n)
    s = np.sum(f(x))
    I = (float(b-a))/n*s
    return I

def MCint2(f,a,b,n,N):
    s= 0
    I_values = []
    i_values = []
    for i in range(1,n+1):
        x= random.uniform(a,b)
        s+= f(x)
        if i % N==0:
            I = (float(b-a)/i)*s
            I_values.append(I)
            i_values.append(i)
    return I_values, i_values

y = lambda x: 3*x**2

I , i = MCint2(y,0,2,100000,N=1000)

import matplotlib.pyplot as plt
error= 6.5 - np.array(I)
plt.plot(i,error)
plt.title('Monte Carlo integration')
plt.xlabel('n')
plt.ylabel('Error')
plt.show()