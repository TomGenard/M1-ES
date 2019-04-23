#!/usr/bin/env python3
# Author: F.Mauger
# Date: 2019-02-27
# Copyright: CC-BY

import sys

from vector_1d import *

# Square 2D shape
class square :
    """A square shape in the xOy referential"""

    # Constructor
    def __init__(self, a_) :
        if a_ < 0.0 :
            raise Exception("square::__init__: invalid side square length (a > b)!")
        self.a = a_
        return

    # Provide a human-friendly string representation of the object
    def __repr__(self) :
        return "[square:{}]".format(self.a)

    # Provide a human-friendly string representation of the object
    def __str__(self) :
        return "[square:{}]".format(self.a)

    # Return the side length
    def get_side_length(self) :
        return self.a

    # Compute and return the perimeter
    def get_perimeter(self) :
        return 4 * self.a

    # Compute and return the surface
    def get_surface(self) :
        return self.a**2

# Test program:
if __name__ == "__main__" :

    sq1 = square(2.5)

    side = sq1.get_side_length()
    surf = sq1.get_surface()
    peri = sq1.get_perimeter()
    sys.stdout.write("Côté      : {}\n".format(side))
    sys.stdout.write("Surface   : {}\n".format(surf))
    sys.stdout.write("Perimeter : {}\n".format(peri))

    sys.exit(0)

