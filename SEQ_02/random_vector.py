# Random point generator on a 2d plane
# by  Tom Genard - 2019.02.20
# 
# It ain't much but it's honest work.

import sys
import math
from vector_2d import *
from collision_detection_2d import *
from test_functions_library import *
from kl_generator import *

def generate_random_point_on_plane(x_min_,x_max_,y_min_,y_max_,ud01_) :
    test_value_max_above_min(x_max_, x_min_)
    test_value_max_above_min(y_max_, y_min_)
    
    x = ud01_()
    x = x * (x_max_ - x_min_) + x_min_

    y = ud01_()
    y = y * (y_max_ - y_min_) + y_min_

    return vector_2d(x,y)

def generate_random_point_on_line(OA_,OB_,ud01_) :
    r = ud01_()
    
    x = r * (OB_.x-OA_.x) + OA_.x
    y = r * (OB_.y-OA_.y) + OA_.y
    
    return vector_2d(x,y)

if __name__ == "__main__" :
    seed = 31415926

    xmin = 0
    xmax = 10
    ymin = 0
    ymax = 10
    
    kl_gen1 = kl_generator(seed)
    kl_gen2 = kl_generator(seed)
    
    OA = generate_random_point_on_plane(xmin,xmax,ymin,ymax,kl_gen1)
    OB = generate_random_point_on_plane(xmin,xmax,ymin,ymax,kl_gen1)

    OM = generate_random_point_on_line(OA,OB,kl_gen2)
    sys.stdout.write("OA = {}\n".format(OA))
    sys.stdout.write("OB = {}\n".format(OB))
    sys.stdout.write("OM = {}\n".format(OM))

    sys.stdout.write("Collision? = {}\n".format(collision_detection_on_segment(OM,OA,OB)))
    error = 0.1
    error_mag = 0.1
    sys.stdout.write("Almost collision? = {}\n".format(collision_detection_on_segment_w_error(OM,OA,OB,error,error_mag)))
    
