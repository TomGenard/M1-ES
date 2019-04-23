# Simple geometry for a circle
# by  Tom Genard - 2019.02.28
# 
# Tis a circle

import sys
import math
from vector_2d import *
from test_functions_library import *

class circle :

    def __init__(self, r_, start_angle_) :
        test_value_positive(r_)
        
        self.r = r_
        self.start_angle = start_angle_
        
        return
    
    def __repr__(self) :
        return "[{},{}]".format(self.r,self.start_angle)

    def __str__(self) :
        return "[{},{}]".format(self.r,self.start_angle)
    
    def get_radius(self) :
        return self.r

    def get_start_angle(self) :
        return self.start_angle

    def get_perimeter(self) :
        perimeter = 2 * math.pi * self.r
        return perimeter

    def get_surface(self) :
        surface = math.pi * (self.r)**2
        return surface

if __name__ == "__main__" :
    r = 1.0
    cir1 = circle(r,0.0)
    sys.stdout.write("Circle 1 = {}\n".format(cir1))
    sys.stdout.write("Circle 1 perimeter = {}\n".format(cir1.get_perimeter()))
    sys.stdout.write("Circle 1 surface = {}\n".format(cir1.get_surface()))
