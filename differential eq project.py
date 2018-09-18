
def init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', '--mass', type=float, default=m)
    parser.add_argument('--b', '--boxheight', type=float, default=b)
    parser.add_argument('--L', '--spring_length', type=float, default=L)
    parser.add_argument('--k', '--spring_stiffness', type=float, default=k)
    parser.add_argument('--beta', '--spring_damping', type=float, default=beta)
    parser.add_argument('--S0', '--initial_position', type=float, default=S0)
    parser.add_argument('--dt', '--timestep', type=float, default=dt)
    parser.add_argument('--g', '--gravity', type=float, default=g)
    parser.add_argument('--w', type= float, default= w_formula)
    parser.add_argument('--N', type=int, default=N)
    args= parser.parse_args()
    
    from scitools.StringFunction import StringFunction as SF 
    w = SF(args.w, independent_variables='t')  
    return (args.m, args.b, args.L, args.k, args.beta, 
            args.S0, args.dt, args.g, args.w, args.N)  

   
def solve(m,k,beta,S0,dt,g,w,N):
    S = [0.0]*(N+1)
    gamma = beta*dt/2.0
    t= 0
    S[0] = S0
    i = 0
    S[i+1] =(1/(2.0*m))*(2*m*S[i] - dt**2*k*S[i] + 
            m*(w(t+dt)- 2*w(t) + w(t-dt)) +dt**2*m*g)
    t = dt
    for i in range(1,N):
        S[i+1]= (1/(m + gamma))*(2*m*S[i]- m*S[i-1] + 
         gamma*dt*S[i-1]- dt**2*k*S[i] + 
         m*(w(t+dt)- 2*w(t) + w(t-dt)) + dt**2*m*g)
        t +=dt
    return S

from math import pi
#default parameters
m = 1; b = 2; L = 10; k = 1; beta = 0; S0 = 1;
dt = 2*pi/40; g = 9.81; w_formula = '0'; N = 80;
m, b, L, k, beta, S0, dt, g, w, N = \
init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N)
S = solve(m, k, beta, S0, dt, g, w, N)
