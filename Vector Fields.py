''' Vector Fields- plotting'''
import numpy as np
import matplotlib.pyplot as plt

#create rect grid in xy plane to plot points
x = y = np.linspace(-10.,10.,11) 
#equally spaced coords [-10,10], 11*11 grid points
xv, yv = np.meshgrid(x,y,indexing='ij', sparse = False)

Rv = -.5*yv**2+xv #field
dRdx, dRdy= np.gradient(Rv) #gradient

fig = plt.figure(1) # get current figure
ax = fig.gca()      # get current axes
ax.quiver(xv,yv,dRdx,dRdy,color='r',angles='xy',scale_units='xy')
plt.axis()


