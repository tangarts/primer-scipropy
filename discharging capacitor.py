from math import exp
import numpy as np
from matplotlib import pyplot as plt
v0 = 6.0
C = 47e-4
R = 1e4
def v(t):
    return v0*exp(-t/(C*R))
    
tvar = range(0,301,10)
vvar = [v(t) for t in tvar]
print '   t/s  v/V'
for t, v in zip(tvar,vvar):
    print '%5d %5.3f' %(t,v)
        
v = np.array(vvar)
t = np.array(tvar)      

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.title('Discharging a Capacitor: V against t')
plt.plot(t,v)  
plt.show()      
