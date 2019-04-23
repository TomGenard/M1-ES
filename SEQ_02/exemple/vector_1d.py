#!/usr/bin/env python3

import sys

class vector_1d :
    """One dimensional vector with basic arithmetics"""

    # Constructor
    # \code
    # v1 = vector_1d()
    # v2 = vector_1d(2.35)
    # \endcode
    def __init__(self, coordinate_ = 0.0) :
        self.coordinate = coordinate_
        return

    # Provide a human-friendly string representation of the object
    def __repr__(self) :
        return "{:16.14e}".format(self.coordinate)

    # Provide a human-friendly string representation of the object
    def __str__(self) :
        return "{}".format(self.coordinate)

    # Return the coordinate
    # \code
    # v1 = vector_1d(4.0)
    # x = v1.get_coordinate()
    # \endcode
    def get_coordinate(self) :
        return self.coordinate

    # Set the coordinate
    # \code
    # v1 = vector_1d(4.0)
    # x = v1.get_coordinate()
    # v1.set_coordinate(3.5)
    # x = v1.get_coordinate()
    # \endcode
    def set_coordinate(self, coordinate_) :
        self.coordinate = coordinate_
        return

    # Negation operator
    # \code
    # v1 = vector_1d(4.0)
    # v2 = -v1
    # \endcode
    def __neg__(self) :
        c = -self.coordinate
        return vector_1d(c);

    # Construct the null vector
    # \code
    # v1 = vector_1d(4.0)
    # v1.zero()
    # \endcode
    def zero(self) :
        self.coordinate = 0.0
        return

    # Return the magnitude of the vector
    # \code
    # v1 = vector_1d(4.0)
    # l = v1.mag()
    # \endcode
    def mag(self) :
        return abs(self.coordinate)

    # Add two vectors
    # \code
    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v3 = v1 + v2
    # v3 = v2 + v1
    # \endcode
    def __add__(self, other_) :
        c = self.coordinate + other_.coordinate
        return vector_1d(c);

    # Add a vector to the current one
    # \code
    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v1 += v2
    # \endcode
    def __iadd__(self, other_) :
        self.coordinate += other_.coordinate
        return self 

    # \code
    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v3 = v1 - v2
    # v3 = v2 - v1
    # \endcode
    def __sub__(self, other_) :
        c = self.coordinate - other_.coordinate
        return vector_1d(c);

    # \code
    # v1 = vector_1d(4.0)
    # v2 = vector_1d(2.0)
    # v1 -= v2
    # \endcode
    def __isub__(self, other_) :
        self.coordinate -= other_.coordinate
        return self

    # \code
    # v1 = vector_1d(4.0)
    # v2 = v1 * 3.4
    # \endcode
    def __mul__(self, factor_) :
        c = self.coordinate * factor_
        return vector_1d(c);

    # \code
    # v1 = vector_1d(4.0)
    # v1 *= 0.5
    # \endcode
    def __imul__(self, factor_) :
        self.coordinate *= factor_
        return self

    # \code
    # v1 = vector_1d(4.0)
    # v2 = 3.4 * v1
    # \endcode
    def __rmul__(self, factor_) :
        c = self.coordinate * factor_
        return vector_1d(c);

    # \code
    # v1 = vector_1d(4.0)
    # v2 = v1 / 3.4
    # \endcode
    def __truediv__(self, divider_) :
        c = self.coordinate / divider_
        return vector_1d(c);
 
    # \code
    # v1 = vector_1d(4.0)
    # v1 /= 3.4
    # \endcode
    def __itruediv__(self, divider_) :
        self.coordinate /= divider_
        return self 

    # \code
    # v1 = vector_1d(4.0)
    # if v1 : print("not null")
    # \endcode
    def __bool__(self) :
        return self.coordinate != 0.0

    # \code
    # v1 = vector_1d(4.0)
    # x = float(v1)
    # \endcode
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
    
