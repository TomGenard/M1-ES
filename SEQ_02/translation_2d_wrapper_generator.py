# Translation wrapper to move generated points on a plane
# by  Tom Genard - 2019.02.28
# 
# 

import sys
import math
from vector_2d import *
from random_vector import *
from rectangle import *
from rectangle_perimeter_generator import *
from kl_generator import *

class translation_2d_wrapper_generator :
    """Translation of a point on a plane"""
    
    def __init__(self, gen_, translation_) :
        self.gen = gen_
        self.translation = translation_
        return

    def __call__(self, ud01_) :
        r = ud01_
        
        point = self.gen(r)
        return point + self.translation

if __name__ == "__main__" :
    rectangle1 = rectangle(4.0,10.0)
    gen1 = rectangle_perimeter_generator(rectangle1)
    
    seed = 31415926
    kl_gen = kl_generator(seed)
    
    OA = vector_2d(10.0,-5.0)
    wr = translation_2d_wrapper_generator(gen1,OA)
    
    OA_translated = wr(kl_gen)
    nb_rectangles = 1000
    
    #sys.stdout.write("aaaaaaaaa = {}\n".format(OA_translated))
    rng_file = open("prng_translation.data","w")
    for i in range(nb_rectangles) :
        wr = translation_2d_wrapper_generator(gen1,OA)
        OA_translated = wr(kl_gen)

        # We transform the segment into a vector to plot in into Gnuplot
        rng_file.write("{} {}\n".format(OA_translated.get_x(),OA_translated.get_y()))

    sys.exit(0)