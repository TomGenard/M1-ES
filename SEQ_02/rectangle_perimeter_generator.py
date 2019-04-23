# PRNG - Inverse Tranform Method
# by  Tom Genard - 2019.02.28
# 
# Living on the surface of a rectangular planet

import sys
import math
from vector_2d import *
from test_functions_library import *
from segment_2d_uniform_generator import *
from kl_generator import *
from rectangle import *

class rectangle_perimeter_generator :
    def __init__(self,rectangle_) :
        self.rectangle = rectangle_

        weight_tot = self.rectangle.get_perimeter()
        weight1 = self.rectangle.get_a() / weight_tot
        weight2 = ( self.rectangle.get_a() + self.rectangle.get_b() ) / weight_tot
        weight3 = ( 2 * self.rectangle.get_a() + self.rectangle.get_b() ) / weight_tot

        OA = vector_2d(-self.rectangle.get_a()/2,self.rectangle.get_b()/2)
        OB = vector_2d(self.rectangle.get_a()/2,self.rectangle.get_b()/2)
        OC = vector_2d(self.rectangle.get_a()/2,-self.rectangle.get_b()/2)
        OD = vector_2d(-self.rectangle.get_a()/2,-self.rectangle.get_b()/2)

        AB = segment_2d(OA,OB)
        BC = segment_2d(OB,OC)
        CD = segment_2d(OC,OD)
        DA = segment_2d(OD,OA)
        
        self.points = []
        self.points.append(OA)
        self.points.append(OB)
        self.points.append(OC)
        self.points.append(OD)
        
        self.weights = []
        self.weights.append(weight1)
        self.weights.append(weight2)
        self.weights.append(weight3)
        self.weights.append(1)

        self.generators = []
        self.generators.append(segment_2d_uniform_generator(AB))
        self.generators.append(segment_2d_uniform_generator(BC))
        self.generators.append(segment_2d_uniform_generator(CD))
        self.generators.append(segment_2d_uniform_generator(DA))
        
        return

    def generate_point_on_rectangle_perimeter(self,ud01_) :
        r1 = ud01_()
        r2 = ud01_
        
        for i in range(len(self.weights)) :
            if r1 < self.weights[i] :
                point = self.generators[i].generate_random_point_on_segment(r2)
                #generate a segment on the initial segment
                #need to transform it into a vector, and add the initial point
                #of the segment to place it in the correct referential
                point = self.points[i] + point.get_vector()
                
                return point

    def __call__ (self,ud01_) :
        r = self.generate_point_on_rectangle_perimeter(ud01_)

        return r

if __name__ == "__main__" :
    seed = 314159262
    kl_gen1 = kl_generator(seed)
    
    a = 4.0
    b = 10.0
    rect1 = rectangle(a,b)
    rect1_gen = rectangle_perimeter_generator(rect1)

    rng_file = open("prng_rectangle.data","w")

    nb_rectangles = 1000

    for i in range(nb_rectangles) :
        OM = rect1_gen.generate_point_on_rectangle_perimeter(kl_gen1)
        OM = rect1_gen(kl_gen1)
        # We transform the segment into a vector to plot in into Gnuplot
        rng_file.write("{} {}\n".format(OM.get_x(),OM.get_y()))

    rng_file.close()

    sys.exit(0)
