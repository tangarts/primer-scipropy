# Exercise 3.21

def C(x,n):
    cj = 1
    s = cj
    for j in range(1,n):
        cj *= -x**2/float(2*j*(2*j-1))
        s += cj
    return s
from math import pi

xlist = [4*pi,6*pi,8*pi,10*pi]
def table(xlist):
    from math import cos
    print '%7s %9s %9s %9s %9s' %('x' ,'n=5' ,'n=25' ,'n=50', 'n=100')
    
