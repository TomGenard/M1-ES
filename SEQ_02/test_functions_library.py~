# PRNG - Inverse Tranform Method
# by  Tom Genard - 2019.02.07
# 
# Doubt everything, except those testing functions. They are legit

import sys
import random

def test_value_positive_and_integer(value_to_test) :
    try :
        value_to_test = int(value_to_test)
    except :
        sys.stderr.write("ERROR : Format incorrect\n")
        sys.exit(1)

    if (value_to_test < 0) :
        sys.stderr.write("ERROR : Valeur négative\n")
        sys.exit(1)
        
def test_value_float(value_to_test) :
    try :
        value_to_test = float(value_to_test)
    except :
        sys.stderr.write("ERROR : Format incorrect\n")
        sys.exit(1)
        
def test_value_integer(value_to_test) :
    try :
        value_to_test = int(value_to_test)
    except :
        sys.stderr.write("ERROR : Format incorrect\n")
        sys.exit(1)
        
def test_value_positive(value_to_test) :
    if (value_to_test < 0) :
        sys.stderr.write("ERROR : Valeur négative\n")
        sys.exit(1)
        
def test_value_max_above_min(value_max, value_min) :
    if (value_max < value_min) :
        sys.stderr.write("ERROR : Valeur maximale inférieure à valeur minimale\n")
        sys.exit(1)
    elif (value_max == value_min) :
        sys.stderr.write("ERROR : Valeur maximale inférieure et valeur minimale égales\n")
        sys.exit(1)
