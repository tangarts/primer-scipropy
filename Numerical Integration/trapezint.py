def trapezint1(f,a,b):
    return (b-a)/2.*(f(a)+f(b))
    
from math import pi, sin, cos
 
trapezint2 = lambda f,a,b: .5*(b-a)/2.*(f(a)+f(b)+2*(f((a+b)/2.)))         

def trapezint(f,a,b,n):
    sum = 0
    h = (b-a)/float(n)
    for i in range(1,n):
        sum += f(a + i*h)
    integral= .5*h*(f(a)+f(b))+h*sum
    return integral
    
def test_trapezint(a,b,n):
    f = lambda x : cos(x)
    F = lambda x : sin(x)
    
    exact = F(b) - F(a)
    approx = trapezint(f,a,b,n)
    if abs(exact - approx)< 1E-14:
        print 'Success'
    else:
        print 'Error: cannot integrate function exactly'

    #midpoint rule#
    
def midpointint(f,a,b,n):
    h= (b-a)/float(n)
    sum = 0
    for i in range(0,n):
        sum += f(a +i*h +.5*h)
    integral = h*sum
    return integral

print midpointint(cos,0,pi/2,10)
    
def trapezoidal(f,a,x,n):
    h = (x-a)/float(n)
    I = 0.5*f(a)
    for i in range(1,n):
        I += f(a + i*h)
    I += 0.5*f(x)
    I *=h
    return I
