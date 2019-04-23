#!/usr/bin/env python3

import random

from vector_1d import *
from segment_1d import *
from kl_generator import *

class global_random_wrapper_generator :

    def __init__(self) :
        return

    def __call__(self) :
        return random.random()

class random_wrapper_generator :

    def __init__(self, rndm_) :
        self.ud01 = rndm_
        return

    def __call__(self) :
        return self.ud01.random()

class segment_1d_uniform_generator :
    """Generator of random points uniformly distributed along a 1D segment"""

    def  __init__(self, segment_) :
        self.segment = segment_
        self.a = float(self.segment.get_first())
        self.ab = float(self.segment.get_length())
        return

    def shoot(self, ud01_ ) :
        r = ud01_() # Callable interface
        x = self.a + self.ab * r
        return vector_1d(x)
        
# Test program:
if __name__ == "__main__" :
    A = vector_1d(3.0)
    B = vector_1d(5.0)
    AB = segment_1d(A, B)
    sys.stderr.write("A = {}\n".format(A))
    sys.stderr.write("B = {}\n".format(B))
    sys.stderr.write("AB = {}\n".format(AB))

    seed_a = 314159
    random.seed(seed_a)
    ud01_a = global_random_wrapper_generator()

    seed_b = 951413
    g1 = random.Random(seed_b)
    ud01_b = random_wrapper_generator(g1)
    
    seed_c = 123456
    ud01_c = kl_generator(seed_c)
    
    g = segment_1d_uniform_generator(AB)

    nshoots = 10000
    for i in range(nshoots) :
        Ca = g.shoot(ud01_a)
        sys.stdout.write("{}\n".format(Ca.get_coordinate()))
        Cb = g.shoot(ud01_b)
        sys.stdout.write("{}\n".format(Cb.get_coordinate()))
        Cc = g.shoot(ud01_c)
        sys.stdout.write("{}\n".format(Cc.get_coordinate()))
    
    sys.exit(0)

 
