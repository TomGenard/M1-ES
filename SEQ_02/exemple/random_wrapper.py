#!/usr/bin/env python3
# Author: F.Mauger
# Date: 2019-02-14
# Copyright: CC-BY

import sys
import random

# Wrapper for a random module's Random generator
class random_wrapper_generator :
    """Wrapper around a random module's uniform deviates random real number generator in [0,1)"""
    def __init__(self, r_) :
        self.r = r_
        return

    def __call__(self) :
        return self.r.random()

    
# Wrapper for the random module's global Random generator
class random_global_wrapper_generator :
    """Wrapper around the random module's global uniform deviates random real number generator in [0,1)"""

    def __init__(self) :
        return

    # Provide a *callable* interface through the '()' operator.
    def __call__(self) :
        return random.random()

    
# Test function:
if __name__ == "__main__" :

    # Initialize the random module's global uniform deviates generator
    seed = 666
    sys.stderr.write("Seed : {}\n".format(seed))
    random.seed(seed)
    
    # Initialize a random module's uniform deviates generator
    seed1 = 314159
    sys.stderr.write("Seed1 : {}\n".format(seed1))
    r1 = random.Random(seed1)
    
    # Initialize another random module's uniform deviates generator
    seed2 = 123456
    sys.stderr.write("Seed2 : {}\n".format(seed2))
    r2 = random.Random(seed2)
   
    nshoots = 10
    
    sys.stderr.write("Fire points from the random module's global generator...\n")
    wr = random_global_wrapper_generator()
    for i in range(nshoots) :
        r = wr() 
        sys.stdout.write("{}\n".format(r))
    
    sys.stderr.write("Fire points from the first Random generator...\n")
    wr1 = random_wrapper_generator(r1)
    for i in range(nshoots) :
        r = wr1() 
        sys.stdout.write("{}\n".format(r))

    sys.stderr.write("Fire points from the second Random generator...\n")
    wr2 = random_wrapper_generator(r2)
    for i in range(nshoots) :
        r = wr2() 
        sys.stdout.write("{}\n".format(r))
  
    sys.exit(0)

    
 
