#!/usr/bin/env python3
# Author: F.Mauger
# Date: 2019-02-14
# Copyright: CC-BY

import sys

# Knuth & Lewis generator
class kl_generator :
    """Knuth & Lewis uniform deviated random real number generator in [0,1)"""

    # Parameters of the congruence.
    # These are static values associated to the class
    # and sharable/used by any instance of this class.
    a = 1664525
    c = 1013904223
    M = 2**32

    # Constructor with a given seed (if omitted, use default value = 0)
    # \code
    # kl1 = kl_generator();
    # kl2 = kl_generator(314159);
    # \endcode
    def __init__(self, seed_ = 0) :
        """Constructor"""
        # Internal state as a tuple with one unique integer element
        self._state_ = (seed_,)
        return

    # Return the internal state of the generator as a tuple
    def get_state(self) :
        return self._state_

    # Force the internal state of the generator as a tuple
    def set_state(self, state_) :
        self._state_ = state_
        return
    
    # Randomize a real number in the [0,1) interval
    # \code
    # kl = kl_generator(314159);
    # r = kl.shoot()
    # \endcode
    def shoot(self) :
        """Randomize a real number uniformly distributed in [0,1)"""
        u = (self.a * self._state_[0] + self.c) % self.M
        self._state_ = (u,) # Mise à jour de l'état du générateur
        return u * 1.0 / self.M

    # Provide a *callable* interface through
    # the '()' operator. This makes a K&L generator
    # instance an *object-function*:
    # \code
    # kl = kl_generator(314159);
    # r = kl()
    # \endcode
    # which is equivalent to:
    # \code
    # r = kl.shoot()
    # \endcode
    def __call__(self) :
        return self.shoot()
    
# Test function:
if __name__ == "__main__" :
    
    seed = 314159
    sys.stderr.write("Seed : {}\n".format(seed))

    nshoots = 10

    sys.stderr.write("From the first K&L generator...\n")
    kl_gen = kl_generator(seed)
    for i in range(nshoots) :
        r = kl_gen() # On note l'utilisation de l'opérateur '()'.
                     # Cela est rendu possible car on a équipé la
                     # classe d'une méthode '__call__' sans argument.
        sys.stdout.write("{}\n".format(r))

    saved_state = kl_gen.get_state()
    
    sys.stderr.write("From the second K&L generator...\n")
    kl_gen2 = kl_generator()
    kl_gen2.set_state(saved_state)
    for i in range(nshoots) :
        r = kl_gen2()
        sys.stdout.write("{}\n".format(r))
   
    sys.exit(0)
