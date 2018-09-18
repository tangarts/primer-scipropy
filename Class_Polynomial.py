''' Polynomial Class'''
import numpy as np
class Polynomial():
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self,x):
        """Evaluate the polynomial."""
        s= 0
        for i in range(len(self.coeff)):
            s+= self.coeff[i]*x**i
        return s
    def __add__(self,other):
        """Return self + other as Polynomial object."""
        if len(self.coeff)>len(other.coeff):
            result_coeff= self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
    def __mul__(self,other):
        c= self.coeff
        d = other.coeff
        M = len(c)-1
        N = len(d)-1
        result_coeff = np.zeros(M+N+1)
        for i in range(0,M+1):
            for j in range(0,N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)
    def differentiate(self):
        for i in range(1,len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]
    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.differentiate()
        return dpdx
    def __str__(self):
        s = ''
        for i in range(0,len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' %(self.coeff[i],i)
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*',' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]        
        return s

p1 = Polynomial([1,0,2])       
p2 = Polynomial([0,1,0,0,-6,-1])
p3 = p1 + p2 
print (p3)

