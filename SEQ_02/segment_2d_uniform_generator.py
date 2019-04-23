# Random point generator on a 2d plane
# by  Tom Genard - 2019.02.20
# 
# Recalibrating splines

import sys
import math
from vector_2d import *
from segment_2d import *
from collision_detection_2d import *
from test_functions_library import *
from kl_generator import *
rng_file = open("prng_vector.data","w")
class segment_2d_uniform_generator :

    def __init__(self, segment_) :
        self.segment = segment_
        return

    def generate_random_point_on_segment(self,ud01) :
        r = ud01()
        vector = self.segment.get_vector() * r
        new_finish = self.segment.get_start() + vector
        
        point = segment_2d(self.segment.get_start(),new_finish)

        return point

if __name__ == "__main__" :
    seed = 314159262
    kl_gen1 = kl_generator(seed)

    OA = vector_2d(1.0,2.0)
    OB = vector_2d(4.785,8.0)
    AB = segment_2d(OA,OB)

    nb_vectors = 1000

    segment_gen = segment_2d_uniform_generator(AB)
    rng_file = open("random_segments_data.csv","w")

    for i in range(nb_vectors) :
        OM = segment_gen.generate_random_point_on_segment(kl_gen1)

        # We transform the segment into a vector to plot in into Gnuplot
        OM = OM.get_start() + OM.get_vector()
        rng_file.write("{} {}\n".format(OM.get_x(),OM.get_y()))
        
    rng_file.close()
    
    #sys.stdout.write("OM = {}\n".format(OM))

    sys.exit(0)
