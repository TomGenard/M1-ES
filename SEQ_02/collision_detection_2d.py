# Two dimentional vector
# by  Tom Genard - 2019.02.20
# 
# If there is a wall in front of your car, this won't stop it, but it will detect it

import sys
import math
from vector_2d import *
from test_functions_library import *

def collision_detection_on_segment(OM_,OA_,OB_) :
    # OM_ the tested point
    # OA_ and OB_, the two points defining the segment

    AB = OB_ - OA_
    AM = OM_ - OA_
    if (AB.get_x()*AM.get_y() - AB.get_y()*AM.get_x() == 0) and (AM.get_x() <= AB.get_x()) and (AM.get_y() <= AB.get_y()) :
        if (AM.mag() <= AB.mag()) :
            return True
        else :
            return False
    else :
        return False

def collision_detection_on_segment_w_error(OM_,OA_,OB_,error_,error_mag_) :
    # OM_ the tested point
    # OA_ and OB_, the two points defining the segment
    # error is the error on the colinearity
    # error_mag is the error on the magnitude

    AB = OB_ - OA_
    AM = OM_ - OA_
    if (AB.get_x()*AM.get_y() - AB.get_y()*AM.get_x() < error_) and (AB.get_x()*AM.get_y() - AB.get_y()*AM.get_x() > -error_) :
        if (AM.mag() <= AB.mag() + error_mag_) :
            return True
        else :
            return False
    else :
        return True

if __name__ == "__main__" :
    OA = vector_2d(2.0,4.0)
    OB = vector_2d(4.0,8.0)
    OL = vector_2d(2.2,4.4)
    OM = vector_2d(12.0,24.0)
    ON = vector_2d(2.0,6.0)
    OP = vector_2d(2.0,4.05)
    error = 0.1
    error_mag = 0.1

    sys.stdout.write("OA = {}\n".format(OA))
    sys.stdout.write("OB = {}\n".format(OB))
    sys.stdout.write("OL = {}\n".format(OL))
    sys.stdout.write("OM = {}\n".format(OM))
    sys.stdout.write("ON = {}\n".format(ON))
    sys.stdout.write("OP = {}\n".format(OP))

    sys.stdout.write("OL Collision? = {}\n".format(collision_detection_on_segment(OL,OA,OB)))
    sys.stdout.write("OL Almost collision? = {}\n".format(collision_detection_on_segment_w_error(OL,OA,OB,error,error_mag)))

    sys.stdout.write("OM Collision? = {}\n".format(collision_detection_on_segment(OM,OA,OB)))
    sys.stdout.write("OM Almost collision? = {}\n".format(collision_detection_on_segment_w_error(OM,OA,OB,error,error_mag)))

    sys.stdout.write("ON Collision? = {}\n".format(collision_detection_on_segment(ON,OA,OB)))
    sys.stdout.write("ON Almost collision? = {}\n".format(collision_detection_on_segment_w_error(ON,OA,OB,error,error_mag)))

    sys.stdout.write("OP Collision? = {}\n".format(collision_detection_on_segment(OP,OA,OB)))
    sys.stdout.write("OP Almost collision? = {}\n".format(collision_detection_on_segment_w_error(OP,OA,OB,error,error_mag)))
