#!/usr/bin/env python3

import sys
import math

class vector_2d :
    """Two dimensional vector in the (xOy) plane with basic arithmetics"""

    # Constructor
    # \code
    # v1 = vector_2d()
    # v2 = vector_2d(1.34, 2.35)
    # \endcode
    def __init__(self, x_ = 0.0, y_ = 0.0) :
        self.x = x_
        self.y = y_
        return

    # Provide a human-friendly string representation of the object
    def __repr__(self) :
        return "({},{})".format(self.x, self.y)

    # Provide a human-friendly string representation of the object
    def __str__(self) :
        return "({},{})".format(self.x, self.y)

    def get_x(self) :
        return self.x

    def get_y(self) :
        return self.y
    
    def set_x(self, x_) :
        self.x = x_
        return
    
    def set_y(self, y_) :
        self.y = y_
        return

    def __neg__(self) :
        x = -self.x
        y = -self.y
        return vector_2d(x, y);

    def zero(self) :
        self.x = 0.0
        self.y = 0.0
        return

    def mag2(self) :
        return self.x**2 + self.y**2

    def mag(self) :
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other_) :
        x = self.x + other_.x
        y = self.y + other_.y
        return vector_2d(x, y);

    def __iadd__(self, other_) :
        self.x += other_.x
        self.y += other_.y
        return self 

    def __sub__(self, other_) :
        x = self.x - other_.x
        y = self.y - other_.y
        return vector_2d(x, y);

    def __isub__(self, other_) :
        self.x -= other_.x
        self.y -= other_.y
        return self

    def __mul__(self, factor_) :
        x = self.x * factor_
        y = self.y * factor_
        return vector_2d(x, y);

    def __imul__(self, factor_) :
        self.x *= factor_
        self.y *= factor_
        return self

    def __rmul__(self, factor_) :
        x = self.x * factor_
        y = self.y * factor_
        return vector_2d(x, y);

    def __truediv__(self, divider_) :
        x = self.x / divider_
        y = self.y / divider_
        return vector_2d(x, y);

    def __itruediv__(self, divider_) :
        self.x /= divider_
        self.y /= divider_
        return self
    
    def __complex__(self) :
        return complex(self.x, self.y)

    def plain_print(self, out_, endl_ = True) :
        out_.write("{:16.14e} {:16.14e}".format(self.x, self.y))
        if endl_ :
            out_.write('\n')
        return

# Test program:
if __name__ == "__main__" :

    OA = vector_2d(3.2, 1.3)
    OB = vector_2d(5.0, 0.45)
    OC = vector_2d(-4.0, 1.23)

    sys.stdout.write("OA = {}\n".format(OA))
    xA = OA.get_x()
    sys.stdout.write("xA = {}\n".format(xA))

    OA.set_x(3.0)
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

    AB.plain_print(sys.stdout)
    
    sys.exit(0)
