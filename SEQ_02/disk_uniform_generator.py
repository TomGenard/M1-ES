# Uniform generator for the circle
# by  Tom Genard - 2019.02.28
# 
# Random points for our good friend the disk

import sys
import math
from vector_2d import *
from test_functions_library import *
from kl_generator import *
from circle import *
from translation_2d_wrapper_generator import *

class disk_surface_generator :
    def __init__(self, circle_) :
        self.circle = circle_

        return

    def generate_point_on_disk_surface(self,ud01_) :
        r = ud01_()
        r = self.circle.get_radius() * math.sqrt(r)
        
        r_theta = ud01_()
        r_theta = r_theta * 2 * math.pi

        x_ = r * math.cos(r_theta)
        y_ = r * math.sin(r_theta)
        
        return ( vector_2d(x_,y_) )

    def __call__(self, ud01_) :
        r_vector = self.generate_point_on_disk_surface(ud01_)

        return r_vector

if __name__ == "__main__" :
    seed = 314159262
    kl_gen1 = kl_generator(seed)
    
    r = 5.0
    start_theta = 0.0
    cir1 = circle(r,start_theta)
    cir1_gen = disk_surface_generator(cir1)
    
    rng_file = open("prng_circle.data","w")
    nb_circles = 1000

    OM = vector_2d(1.8,-3.7) # Translation

    for i in range(nb_circles) :
        wr = translation_2d_wrapper_generator(cir1_gen,OM)
        OM_translated = wr(kl_gen1)
        
        # We transform the segment into a vector to plot in into Gnuplot
        rng_file.write("{} {}\n".format(OM_translated.get_x(),OM_translated.get_y()))

    rng_file.close()

    sys.exit(0)
