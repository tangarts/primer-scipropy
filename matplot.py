import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi*2,np.pi*2,256)
c,s, e = np.cos(x), np.sin(x), np.exp(x)
plt.plot(x,s)
plt.plot(x,c,'r')

plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(s.min()*1.1, s.max()*1.1)
plt.xticks([-np.pi*2,-np.pi*3/2, -np.pi,-np.pi/2, 0, np.pi/2, np.pi, np.pi*3/2, np.pi*2] ,
[r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$',r'$2\pi$'])
plt.yticks([-1,0,1], [r'$-1$', r'$0$', r'$1$'])

ax  = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()