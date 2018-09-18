#Exercise 8.35
import numpy as np
import matplotlib.pyplot as plt
import random as rnd

class Particle(object):
    def __init__(self,x,y,step):
        self.x = np.zeros()
        self.y = np.zeros()
        self.step = step
        
    def move(self,steps):
        up = 1; left = 2; down = 3; right = 4
        for i in range(steps):
            direction = rnd.randint(1,4)
            if direction == up:
                self.y[i] += 1
            elif direction == right:
                self.x[i] += 1
            elif direction == down:
                self.y[i] -= 1
            elif direction == left:
                self.x[i] -= 1
                     
        return self.x, self.y
    

