#!/usr/bin/env python3
# Author: F.Mauger
# Date: 2019-02-28
# Copyright: CC-BY

import sys

from square import *
from vector_2d import *
from kl_generator import *

class square_uniform_surface_generator :
    """A random generator of points uniformly distributed on the surface of a square"""

    # Constructor
    def __init__(self, sq_) :
        self.sq = sq_
        return

    # Randomize a point in the square referential of the square
    # \param ud01_ a *callable* uniform deviate generator in the [0,1) interval
    def shoot(self, ud01_) :
        rx = ud01_()
        ry = ud01_()
        x = self.sq.get_side_length() * (-0.5 + rx)
        y = self.sq.get_side_length() * (-0.5 + ry)
        return vector_2d(x,y)

    
# Test program:
if __name__ == "__main__" :

    # Instantiate a square:
    sq1 = square(2.5)

    # Instantiate a K&L generator:
    seed = 314159
    kl1 = kl_generator(seed)

    # Instantiate a 2D-point generator on the surface of the square:
    gen1 = square_uniform_surface_generator(sq1)

    # Random loop:
    nshoots = 1000
    for i in range(nshoots) :
        p = gen1.shoot(kl1)
        p.plain_print(sys.stdout)
        
    sys.exit(0)

