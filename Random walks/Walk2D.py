import random as rnd
import numpy 
import matplotlib.pyplot as plt

def random_walk_2D(np,ns,plot_step):
    
    xpos = numpy.zeros(np) ; ypos = numpy.zeros(np)
    xymax = 3*numpy.sqrt(ns); xymin = -xymax
    NORTH = 1; SOUTH = 2; EAST = 3; WEST = 4
        
    for step in range(ns):
        for i in range(np):
            direction = rnd.randint(1,4)
            if direction == NORTH:
                ypos[i] +=1
            elif direction == SOUTH:
                ypos[i] -= 1
            elif direction == EAST:
                xpos[i] += 1
            elif direction == WEST:
                xpos[i] -=1
                 
        if (step+1) % plot_step == 0:
            plt.plot(xpos, ypos,'ko')
            plt.title('%d particles after %d steps' %(np, step+1))
            plt.xlim(xymin,xymax)
            plt.ylim(xymin,xymax)
            plt.show()
            
rnd.seed(535)
import sys
np = int(sys.argv[1])
ns = int(sys.argv[2]) 
plot_step = int(sys.argv[3])

random_walk_2D(np,ns,plot_step)
