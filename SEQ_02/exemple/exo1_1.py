#!/usr/bin/env python3

import random

from vector_1d import *
from segment_1d import *
     
# Test program:
if __name__ == "__main__" :
    A = vector_1d(3.0)
    B = vector_1d(5.0)
    AB = segment_1d(A, B)
    sys.stderr.write("A = {}\n".format(A))
    sys.stderr.write("B = {}\n".format(B))
    sys.stderr.write("AB = {}\n".format(AB))

    seed = 314159
    random.seed(seed)
    a =  float(AB.get_first())
    ab = AB.get_length()

    nshoots = 10
    for i in range(nshoots) :
        r = random.random()
        c = a + ab * r
        C = vector_1d(c)
        sys.stderr.write("C = {}\n".format(C))
        sys.stdout.write("{}\n".format(C.get_coordinate()))
    
    sys.exit(0)

 
