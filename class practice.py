#Class Practice

class spring():
    def __init__(self,k):
        self.k = k
    def force(self,x):
        F = self.k*x
        return F
    def energy(self,x):
        Ep = 0.5*self.k*x**2
        return Ep

s = spring(5.0)


def table(self,f,a,b,n,heading=''):
    print heading 
    h = (b-a)/float(n)
    for i in range(n+1):
        x = a +i*h
        print 'function value= %10.4f at x = %g' %(f, x)

class Derivative():
    def __init__(self,f,h):
        self.f = f
        self.h = float(h)
    def __call__(self,x):
        f = self.f
        h = self.h
        return (f(x+h)-f(x-h))/float(2*h)

def f(x):
    return 0.25*x**4

df = Derivative(f,1e-5)
for x in (1,5,10):
    df_value = df(x)
    exact = x**3
    print "f'(%d)=%g (error=%.2E)" %(x,df_value,exact)
