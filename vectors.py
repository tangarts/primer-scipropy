import numpy as np

class vec2D(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return vec2D(self.x + other.x, self.y + other.y)