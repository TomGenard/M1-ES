# Position wrapper to move and rotate generated points on a plane
# by  Tom Genard - 2019.03.20
# 
# 

import sys
import math
from vector_2d import *
from random_vector import *
from rectangle import *
from rectangle_perimeter_generator import *
from kl_generator import *

class position_2d_wrapper_generator :
    """Translation of a point on a plane"""
    
    def __init__(self, gen_, translation_, rotation_) :
        self.gen = gen_
        self.translation = translation_
        self.rotation = rotation_
        return

    def __call__(self, ud01_) :
        r = ud01_

        point = self.gen(r)
        point_x = point.get_x() * math.cos(self.rotation) - point.get_y() * math.sin(self.rotation)
        point_y = point.get_x() * math.sin(self.rotation) + point.get_y() * math.cos(self.rotation)

        point.set_x(point_x)
        point.set_y(point_y)
        point = point + self.translation
        
        return point

if __name__ == "__main__" :
    rectangle1 = rectangle(4.0,10.0)
    gen1 = rectangle_perimeter_generator(rectangle1)
    
    seed = 31415926
    kl_gen = kl_generator(seed)
    
    OA = vector_2d(10.0,-5.0)
    theta = 1
    wr = position_2d_wrapper_generator(gen1,OA,theta)
    
    nb_rectangles = 1000
    
    #sys.stdout.write("aaaaaaaaa = {}\n".format(OA_translated))
    rng_file = open("prng_translation.data","w")
    for i in range(nb_rectangles) :
        wr = position_2d_wrapper_generator(gen1,OA,theta)
        OA_translated = wr(kl_gen)

        # We transform the segment into a vector to plot in into Gnuplot
        rng_file.write("{} {}\n".format(OA_translated.get_x(),OA_translated.get_y()))

    sys.exit(0)
