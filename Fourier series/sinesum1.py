# Exercise 3.7, 4.18 

from math import sin, pi

def f(t,T):
    if 0 < t < T/2:
        return 1
    elif abs(t-T/2) < 1E-14:
        return 0
    elif T/2 < t < T:
        return -1
    
def S(t,n,T):
    s = 0
    for i in range(1,n+1):
        s += sin((2*(2*i-1)*pi*t)/T)/float(2*i-1)
    s = 4*s/pi
    return s

def table(n_values, alpha_values, T):
    t_list = [2*alpha*T for alpha in alpha_values]
    table = []
    for n in n_values:        
        print 'n = %s' %n
        error0 = abs(f(t_list[0],T)- S(t_list[0],n,T))
        print 'error for 0.01T= %f' %error0
        error1 = abs(f(t_list[1],T)- S(t_list[1],n,T))
        print 'error for 0.25T= %f' %error1
        error2 = abs(f(t_list[2],T)- S(t_list[2],n,T))
        print 'error for 0.49T= %f' %error2
        
if __name__ == '__main__':
    T = 2*pi
    n_list  = [1,3,5,10,30,100]
    alpha_list = [0.01, 0.25, 0.49]
    table(n_list, alpha_list, T)



