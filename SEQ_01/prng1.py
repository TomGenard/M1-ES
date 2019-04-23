#!/usr/bin/env python3
import sys
import random

def run() :
    seed = 123456
    nshoots = 1000
    count_save_period = 200
    seed_log_path = "prng_seed.log"
    state_log_path = "prng_state.log"
    fseed = open(seed_log_path, "w")
    fseed.write("seed={:d}\n".format(seed))
    fseed.close()
    random.seed(seed)
    for i in range(nshoots) :
        r = random.random()
        if (i % count_save_period) == 0 or (i + 1 == nshoots) : 
            state = random.getstate()
            state0 = state[0]
            state1 = state[1]
            state2 = state[2] # Not used (None)
            sys.stderr.write("INFO : PRNG internal state is : \n")
            sys.stderr.write("INFO : |-- count    = {}\n".format(i))
            sys.stderr.write("INFO : |-- state[0] = {}\n".format(state0))
            sys.stderr.write("INFO : |-- state[1] = ({} ... {}) [len={}]\n"
                             .format(state1[0], state1[-1], len(state1)))
            sys.stderr.write("INFO : `-- state[2] = {}\n".format(state2))
            fstate = open(state_log_path, "w")
            fstate.write("count={:d}\n".format(i))
            fstate.write("prng.state[0]={:d}\n".format(state0))
            fstate.write("prng.state[1]=")
            for j in range(len(state1)) :
                fstate.write("{:d} ".format(state1[j]))
            fstate.write("\n")
        sys.stdout.write("{:16.14f}\n".format(r))
    return 0

if __name__ == "__main__" :
    error_code = run()
    sys.exit(error_code)
    
