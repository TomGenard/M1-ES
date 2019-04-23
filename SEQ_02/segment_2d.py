# Random point generator on a 2d plane
# by  Tom Genard - 2019.02.28
# 
# 

import sys
import math
from vector_2d import *
from collision_detection_2d import *

class segment_2d :

    def __init__(self, start_ = vector_2d(0.0,0.0), finish_ = vector_2d(0.0,0.0)) :
        self.start = start_
        self.finish = finish_
        return

    def __repr__(self) :
        return "({},{})".format(self.start, self.finish)

    def __str__(self) :
        return "({},{})".format(self.start, self.finish)

    def get_start(self) :
        return self.start

    def get_finish(self) :
        return self.finish

    def set_start(self, start_) :
        self.start = start_
        return

    def set_finish(self, finish_) :
        self.finish = finish_
        return

    def get_vector(self) :
        x = self.finish.get_x()-self.start.get_x()
        y = self.finish.get_y()-self.start.get_y()
        return vector_2d(x,y)

    def get_length(self) :
        _vector = self.get_vector()
        return _vector.mag()

    def inside(self, point_, error_, error_mag_) :
        return collision_detection_on_segment(point_,self.start,self.finish)

if __name__ == "__main__" :
    OA = vector_2d(2.0,4.0)
    OB = vector_2d(4.0,8.0)
    OL = vector_2d(2.2,4.4)
    OM = vector_2d(12.0,24.0)
    ON = vector_2d(2.0,6.0)
    OP = vector_2d(2.0,4.05)
    error = 0.1
    error_mag = 0.1

    AB = segment_2d(OA,OB)
    sys.stdout.write("Length = {}\n".format(AB.get_length()))
    AB_vector = AB.get_vector()
    sys.stdout.write("Vector = {}\n".format(AB_vector))
    
    is_inside = AB.inside(OL,error,error_mag)
    sys.stdout.write("OL is inside? = {}\n".format(is_inside))
    is_inside = AB.inside(OM,error,error_mag)
    sys.stdout.write("OM is inside? = {}\n".format(is_inside))
    is_inside = AB.inside(ON,error,error_mag)
    sys.stdout.write("ON is inside? = {}\n".format(is_inside))
    is_inside = AB.inside(OP,error,error_mag)
    sys.stdout.write("OP is inside? = {}\n".format(is_inside))