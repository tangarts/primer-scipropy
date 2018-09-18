# Exercise 7.23

from Class_Polynomial import Polynomial as P
from factorial import factorial

# (ii) reads x and a series of N values from the command line
import sys
x = float(sys.argv[1])
N = int(sys.argv[4])

#(iii) creates a Polynomial object for each N value 
#      for computing with the given Taylor polynomial
def p(x):
    k = 0
    T = 0
    p = []
    for k in range(k,N+1):
        T = x**k/factorial(k)
        p.append(T)
    return p

print p(x), x, N
print P(p(x))


'''

(iv) Prints the values of p(x) for all the given N values as well as the exact value e^x . 
Try the program out with x = 0.5,3,10 and N = 2,5,10,15,25.
'''
