#!/usr/bin/env python3

import sys

from vector_1d import *

# The representation of a 1D segment (closed interval)
# built from 2 points on the real axis.
class segment_1d :
    """One dimensional segment (interval)"""

    # Constructor
    # \code
    # A = vector_1d(3.0)
    # B = vector_1d(5.0)
    # AB = segment_1d(A, B)
    # \endcode 
    def __init__(self, first_, last_) :
        if first_.get_coordinate() > last_.get_coordinate() :
            raise Exception("segment_1d::__init__: invalid bounds (first > last)!")
        self.first = first_
        self.last = last_
        return

    # Provide a human-friendly string representation of the object
    def __repr__(self) :
        return "({};{})".format(self.first, self.last)

    # Provide a human-friendly string representation of the object
    def __str__(self) :
        return '({};{})'.format(self.first, self.last)

    # Return the first point
    def get_first(self) :
        return self.first

    # Return the last point
    def get_last(self) :
        return self.last

    # Return the length of the segment
    def get_length(self) :
        return (self.last - self.first).mag()

    # Check if a point is inside the interval/segment (including bounds)
    def inside(self, point_) :
        if (point_.get_coordinate() < self.first.get_coordinate()) :
            return False
        if (point_.get_coordinate() > self.last.get_coordinate()) :
            return False
        return True

    # Locate a point with respect to the segment, taking into account
    # a given tolerance on the position.
    # \return a integer code with the following possible values:
    #   * -1 : the point is outside the segment
    #   *  0 : the point is on some bound of the segment
    #   * +1 : the point is inside the segment
    def locate(self, point_, resolution_ = 1e-7) :
        res = abs(resolution_)
        if (point_.get_coordinate() < self.first.get_coordinate() - res ) :
            return -1
        if (point_.get_coordinate() < self.first.get_coordinate() + res ) :
            return 0
        if (point_.get_coordinate() < self.last.get_coordinate() - res ) :
            return 1
        if (point_.get_coordinate() < self.last.get_coordinate() + res ) :
            return 0
        return -1
     
    
# Test program:
if __name__ == "__main__" :

    A = vector_1d(3.0)
    B = vector_1d(5.0)
    sys.stdout.write("A = {}\n".format(A))
    sys.stdout.write("B = {}\n".format(B))

    AB = segment_1d(A, B)
    sys.stdout.write("AB = {}\n".format(AB))
    sys.stdout.write("|AB| = {}\n".format(AB.get_length()))
    
    C = vector_1d(3.5)
    if AB.inside(C) :
        sys.stdout.write("C is inside AB\n")
    
    D = vector_1d(1000.0)
    if not AB.inside(D) :
        sys.stdout.write("D is outside AB\n")

    start = vector_1d(-1.0)
    stop  = vector_1d(+8.0)
    nsteps = 100
    step = (stop - start) / nsteps
    epsilon = 0.05
    for i in range(nsteps) :
        running_coordinate = start + i * step
        location = AB.locate(running_coordinate, epsilon)
        print("coordinate={} : location={}".format(running_coordinate, location))

    sys.exit(0)

  
    
    
