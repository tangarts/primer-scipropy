def derivative(f):
    def df(x,h=.1E-5):
        return (f(x+h)-f(x-h))/2*h
    return df
    
from math import sin, cos, pi, exp
   
def test_diff():
    x = 1
    f = x**2
    df = 2*x
    success = abs(diff(f,x,h=1E-5) - df) < 1E-5
    if not success:
        print  'Error: Unsuccessful'
    
test_diff()
