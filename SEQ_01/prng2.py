#!/usr/bin/env python3
import sys
import random

def prng_save_state(out_, label_, state_) :
    out_.write("{:s}.state[0]={:d}\n".format(label_, state_[0]))
    out_.write("{:s}.state[1]=".format(label_))
    for j in range(len(state_[1])) :
        out_.write("{:d} ".format(state_[1][j]))
    out_.write("\n")
    return

if __name__ == "__main__" :
    # Define parameters:
    seed1 = 314159
    seed2 = 951413
    nevents = 4
    count_save_period = 5
    seed_log_path = "prng_seed.log"
    state_log_path = "prng_state.log"
    # Save the seeds:
    fseed = open(seed_log_path, "w")
    fseed.write("prng1.seed={:d}\n".format(seed1))
    fseed.write("prng2.seed={:d}\n".format(seed2))
    fseed.close()
    # Instantiate two PRNGs:
    g1 = random.Random(seed1)
    g2 = random.Random(seed2)
    # Event loop:
    for i in range(nevents) :
        # Use PRNG #1 for 3 shoots:
        r1a = g1.random()
        r1b = g1.random()
        r1c = g1.random()
        # Use PRNG #2 for 1 shoot:
        r2 = g2.random()
        # Print results for this event:
        sys.stdout.write("{:16.14f} {:16.14f} {:16.14f} {:16.14f}\n"
                         .format(r1a, r1b, r1c, r2))
        # Save states:
        if (i % count_save_period) == 0 or (i + 1 == nevents) :
            fstate = open(state_log_path, "w")
            fstate.write("count={:d}\n".format(i))
            prng_save_state(fstate, "prng1", g1.getstate()) 
            prng_save_state(fstate, "prng2", g2.getstate())
        fstate.close()
    sys.exit(0)
