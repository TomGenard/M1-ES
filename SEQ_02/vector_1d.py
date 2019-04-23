#!/usr/bin/env python3

import sys

class vector_1d :
    """One dimensional vector with basic arithmetics"""

    def __init__(self, coordinate_) :
        self.coordinate = coordinate_
        return

    def __repr__(self) :
        return "{:16.14e}".format(self.coordinate)

    def __str__(self) :
        return "{}".format(self.coordinate)

    # v1 = vector_1d(4.0)
    # x = v1.get_coordinate()
    def get_coordinate(self) :
        return self.coordinate

    # v1 = vector_1d(4.0)
    # x = v1.get_coordinate()
    # v1.set_coordinate(3.5)
    # x = v1.get_coordinate()
    def set_coordinate(self, coordinate_) :
        self.coordinate = coordinate_
        return

    # v1 = vector_1d(4.0)
    # v2 = -v1
    def __neg__(self) :
        c = -self.coordinate
        return vector_1d(c);

    # v1 = vector_1d(4.0)
    # v1.zero()
    def zero(self) :
        self.coordinate = 0.0
        return

    # v1 = vector_1d(4.0)
    # l = v1.mag()
    def mag(self) :
        return abs(self.coordinate)

    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v3 = v1 + v2
    # v3 = v2 + v1
    def __add__(self, other_) :
        c = self.coordinate + other_.coordinate
        return vector_1d(c);

    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v1 += v2
    def __iadd__(self, other_) :
        self.coordinate += other_.coordinate
        return self 

    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v3 = v1 - v2
    # v3 = v2 - v1
    def __sub__(self, other_) :
        c = self.coordinate - other_.coordinate
        return vector_1d(c);

    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v1 -= v2
    def __isub__(self, other_) :
        self.coordinate -= other_.coordinate
        return self

    # v1 = vector_1d(4.0)
    # v2 = v1 * 3.4
    def __mul__(self, factor_) :
        c = self.coordinate * factor_
        return vector_1d(c);

    # v1 = vector_1d(4.0)
    # v1 *= 0.5
    def __imul__(self, factor_) :
        self.coordinate *= factor_
        return self

    # v1 = vector_1d(4.0)
    # v2 = 3.4 * v1
    def __rmul__(self, factor_) :
        c = self.coordinate * factor_
        return vector_1d(c);

    # v1 = vector_1d(4.0)
    # v2 = v1 / 3.4
    def __truediv__(self, divider_) :
        c = self.coordinate / divider_
        return vector_1d(c);
 
    # v1 = vector_1d(4.0)
    # v1 /= 3.4
    def __itruediv__(self, divider_) :
        self.coordinate /= divider_
        return self 

    # v1 = vector_1d(4.0)
    # if v1 : print("not null")
    def __bool__(self) :
        return self.coordinate != 0.0

    # v1 = vector_1d(4.0)
    # x = float(v1)
    def __float__(self) :
        return self.coordinate
      

# Test program:
if __name__ == "__main__" :

    OA = vector_1d(3.2)
    OB = vector_1d(5.0)
    OC = vector_1d(-4.0)

    sys.stdout.write("OA = {}\n".format(OA))
    a = OA.get_coordinate()
    sys.stdout.write("a = {}\n".format(a))

    OA.set_coordinate(3.0)
    sys.stdout.write("OA = {}\n".format(OA))
    
    sys.stdout.write("OB = {}\n".format(OB))
    sys.stdout.write("OC = {}\n".format(OC))
    sys.stdout.write("|OC| = {}\n".format(OC.mag()))
    
    AB = OB - OA
    sys.stdout.write("AB = {}\n".format(AB))
   
    BA = -AB
    sys.stdout.write("BA = {}\n".format(BA))
   
    ABtimes2 = AB * 2
    sys.stdout.write("ABx2 = {}\n".format(ABtimes2))
   
    twoTimesAB = 2 * AB 
    sys.stdout.write("2xAB = {}\n".format(twoTimesAB))
 
    ABhalf = AB / 2
    sys.stdout.write("AB/2 = {}\n".format(ABhalf))

    AB *= 3.5
    sys.stdout.write("AB = {}\n".format(AB))
  
    sys.exit(0)
    
