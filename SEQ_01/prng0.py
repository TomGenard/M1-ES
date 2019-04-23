#!/usr/bin/env python3

# Load the Python system library
# (http://docs.python.org/library/sys.html) :
import sys

# Load the Python random library
# (http://docs.python.org/library/random.html) :
import random

# Define a function that shoots at least 1000 pseudo-random
# real numbers using the uniform deviates distribution
# (flat distribution in the [0,1[ range) :
def run(argv_) :

    # Select the seed of the PRNG :
    seed = 314159
    if len(argv_) > 1 :
        seed = int(argv_[1])
    if seed < 0 :
        sys.stderr.write("ERROR: Invalid seed ({:d} < 0) !\n".format(seed))
        return 1

    # Select the number of shoots:
    nshoots = 1000
    if len(argv_) > 2 :
        nshoots = int(argv_[2])
    if nshoots < 1000 :
        sys.stderr.write("ERROR: Invalid number "
                         "of shots ({:d} < 1000) !\n".format(nshoots))
        return 1

    # Affichages:
    sys.stderr.write("NOTICE: seed    = {:d}\n".format(seed))
    sys.stderr.write("NOTICE: nshoots = {:d}\n".format(nshoots))

    # Save the seed in a dedicated log file:
    seed_log_path = "prng_seed.log"
    fseed = open(seed_log_path, "w")
    fseed.write("seed={:d}\n".format(seed))
    fseed.close()
    sys.stderr.write("NOTICE: seed saved in '{:s}'\n".format(seed_log_path))
   
    # Initialize the PRNG with the seed :
    random.seed(seed)

    # Use the generator :
    for i in range(nshoots) :
        r = random.random()
        sys.stdout.write("{:16.14f}\n".format(r))
    return 0

# Main block : 
if __name__ == "__main__" :
    error_code = run(sys.argv)
    sys.exit(error_code)
