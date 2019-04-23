# Uniform generator for the circle
# by  Tom Genard - 2019.02.28
# 
# Random points for our good friend the circle

import sys
import math
from vector_2d import *
from test_functions_library import *
from kl_generator import *
from circle import *

class circle_perimeter_generator :
    def __init__(self, circle_) :
        self.circle = circle_

        return

    def generate_point_on_circle_perimeter(self,ud01_) :
        r_theta = ud01_()
        r_theta = r_theta * 2 * math.pi

        x_ = self.circle.get_radius() * math.cos(r_theta)
        y_ = self.circle.get_radius() * math.sin(r_theta)
        
        return ( vector_2d(x_,y_) )

    def __call__(self, ud01_) :
        r_vector = self.generate_point_on_circle_perimeter(ud01_)

        return r_vector

if __name__ == "__main__" :
    seed = 314159262
    kl_gen1 = kl_generator(seed)
    
    r = 5.0
    start_theta = 0.0
    cir1 = circle(r,start_theta)
    cir1_gen = circle_perimeter_generator(cir1)
    
    rng_file = open("prng_circle.data","w")
    nb_circles = 1000

    for i in range(nb_circles) :
        OM = cir1_gen.generate_point_on_circle_perimeter(kl_gen1)
        OM = cir1_gen(kl_gen1)
        # We transform the segment into a vector to plot in into Gnuplot
        rng_file.write("{} {}\n".format(OM.get_x(),OM.get_y()))

    rng_file.close()

    sys.exit(0)
