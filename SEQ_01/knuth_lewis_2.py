# PRNG - Inverse Tranform Method
# by  Tom Genard - 2019.02.07
# 
# Please don't break it, it's very precious

import sys
import random
import math
from test_functions_library import *

def itm_uniform_distribution(_seed, _nb_shoot, _max, _min) :
    random.seed(_seed)
    rng_file = open("prng_uni.data","w")
    for i in range(_nb_shoot) :
        _rand_value = random.random()
        _rand_value = _rand_value * (_max - _min) + _min
        #print("{:f}".format(_rand_value))
        rng_file.write("{:f}".format(_rand_value))
    rng_file.close()

def itm_exponential_distribution(_seed, _nb_shoot, _lambda) :
    random.seed(_seed)
    rng_file = open("prng_exp.data","w")
    for i in range(_nb_shoot) :
        _rand_value = random.random()
        _rand_value = -( math.log(1-_rand_value) ) / _lambda
        #print("{:f}".format(_rand_value))
        rng_file.write("{:f}\n".format(_rand_value))
    rng_file.close()
    
def itm_sine_distribution(_seed, _nb_shoot) :
    random.seed(_seed)
    rng_file = open("prng_cos.data","w")
    for i in range(_nb_shoot) :
        _rand_value = random.random()
        if (_rand_value > 0.5) :
            _rand_value = _rand_value - 1
        _rand_value = math.acos(-2*_rand_value)
        if (_rand_value >= math.pi) :
            _rand_value = 0
        #print("{:f}".format(_rand_value))
        rng_file.write("{:f}\n".format(_rand_value))
    rng_file.close()

def is_below(_x,_y):
    if (_y < math.cos(_x)):
        return True
    return False
    
def main() :
    input_seed     = input("Veuillez inserez la graine : ")
    test_value_positive_and_integer(input_seed)
    input_seed     = int(input_seed)
    
    input_nb_shoot = input("Veuillez inserez le nombre de lancer : ")
    test_value_positive_and_integer(input_nb_shoot)
    input_nb_shoot = int(input_nb_shoot)
    
    input_setting  = input("Utiliser quelle distribution (u : uniform, e : exponential, s : sine, r : rejet method sine) : ")

    if (input_setting == "u"):
        input_max      = input("Veuillez inserez le nombre maximal : ")
        test_value_integer(input_max)
        input_max      = int(input_max)
    
        input_min      = input("Veuillez inserez le nombre minimal : ")
        test_value_integer(input_min)
        input_min      = int(input_min)
    
        test_value_max_above_min(input_max, input_min)
        
        itm_uniform_distribution(input_seed, input_nb_shoot, input_max, input_min)
    elif (input_setting == "e"):
        input_lambda   = input("Veuillez inserez lambda : ")
        test_value_float(input_lambda)
        input_lambda = float(input_lambda)
        test_value_positive(input_lambda)
        
        itm_exponential_distribution(input_seed, input_nb_shoot, input_lambda)
    elif (input_setting == "s"):
        
        itm_sine_distribution(input_seed, input_nb_shoot)

    elif (input_setting == "r"):
        rng_file = open("prng_cos.data","w")
        for i in range(input_nb_shoot):
            j = 0
            while (j != 1) :
                x = random.random()
                x = math.pi + x*math.pi
                y = random.random()
                if is_below(x,y) :
                    j = 1
                else :
                    j = 0
            print (i)
            X = x
            rng_file.write("{:f}\n".format(X))
        rng_file.close()

    else :
        print ("Excuse me, what the fuck ?")

if __name__ == "__main__" :
    main()
