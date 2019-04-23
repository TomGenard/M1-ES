# PRNG - Inverse Tranform Method
# by  Tom Genard - 2019.02.28
# 
# 

import sys
import math
from vector_2d import *
from test_functions_library import *

class rectangle :

    def __init__(self, a_, b_) :
        test_value_positive(a_)
        test_value_positive(b_)
        
        self.a = a_
        self.b = b_
        
        return
    
    def __repr__(self) :
        return "[{},{}]".format(self.a,self.b)

    def __str__(self) :
        return "[{},{}]".format(self.a,self.b)
    
    def get_a(self) :
        return self.a

    def get_b(self) :
        return self.b

    def get_perimeter(self) :
        perimeter = self.a * 2 + self.b * 2
        return perimeter

    def get_surface(self) :
        surface = self.a * self.b
        return surface

if __name__ == "__main__" :
    a = 2.0
    b = 4.0
    rect1 = rectangle(a,b)
    sys.stdout.write("Rectangle 1 = {}\n".format(rect1))
    sys.stdout.write("Rectangle 1 perimeter = {}\n".format(rect1.get_perimeter()))
    sys.stdout.write("Rectangle 1 surface = {}\n".format(rect1.get_surface()))

    a2 = 554
    b2 = 999
    rect2 = rectangle(a2,b2)
    sys.stdout.write("Rectangle 2 = {}\n".format(rect2))
    sys.stdout.write("Rectangle 2 perimeter = {}\n".format(rect2.get_perimeter()))
    sys.stdout.write("Rectangle 2 surface = {}\n".format(rect2.get_surface()))

    A = 554
    B = -999
    rect3 = rectangle(A,B)
