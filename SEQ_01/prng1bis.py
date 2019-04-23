#!/usr/bin/env python3
# Author: F.Mauger <mauger@lpccaen.in2p3.fr>
# Date: 2019-01-21
# Description: Use a uniform deviates PRNG after loading its internal state 

import sys
import random

def run() :
    state_log_path = "prng_state.log"
    nshoots = 1000
    
    # Restore PRNG internal state from a file :
    fstate = open(state_log_path, "r")
    
    # Parse the saved PRNG's internal state from the file :
    line0  = fstate.readline()
    token0 = line0[:-1].split('=')[1]
    count  = int(token0)
    line1  = fstate.readline()
    token1 = line1[:-1].split('=')[1]
    state0 = int(token1)
    line2  = fstate.readline()
    token2 = line2[:-1].split('=')[1][:-1]
    tokvalues = token2.split()
    sys.stderr.write("DEBUG : values = {}\n".format(tokvalues))
    state1 = ()
    for tokvalue in tokvalues :
        value = int(tokvalue)
        state1 = state1 + (value, )
    state2 = None
    sys.stderr.write("INFO : PRNG internal state is : \n")
    sys.stderr.write("INFO : |-- count    = {}\n".format(count))
    sys.stderr.write("INFO : |-- state[0] = {}\n".format(state0))
    sys.stderr.write("INFO : |-- state[1] = ({} ... {}) [len={}]\n"
                     .format(state1[0], state1[-1], len(state1)))
    sys.stderr.write("INFO : `-- state[2] = {}\n".format(state2))
    fstate.close()
    
    # Force the PRNG's internal state:
    state = (state0, state1, state2)
    random.setstate(state)

    # Randomize more numbers:
    for i in range(nshoots) :
        r = random.random()
        sys.stdout.write("{:16.14f}\n".format(r))
    return 0

if __name__ == "__main__" :
    error_code = run()
    sys.exit(error_code)
