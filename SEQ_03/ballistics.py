# Two dimentional ballistics
# by  Tom Genard - 2019.03.14
# 
# It's family friendly

import sys
import math
from kl_generator import *
from vector_2d import *
from test_functions_library import *

def calculate_impact_point(x0_, z0_, v0_, alpha0_, g_) :
  
    t_impact = ( v0_ * math.sin(alpha0_) / g_ ) * ( 1 + math.sqrt( 1 + ( 2*g_ * z0_ ) / ( v0_**2 * math.sin(alpha0_)**2 ) ) )
    x_impact = v0_ * math.cos( alpha0_ ) * t_impact + x0_
    angle_impact = math.asin( ( ( ( g_ * t_impact ) / 2 * v0_ ) - ( z0_ / ( v0_ * t_impact ) ) ) % 2 - 1 )
    vx_impact = v0_ * math.cos( angle_impact )
    vz_impact = -g_ * t_impact + v0_ * math.sin( angle_impact )

    v_impact = vector_2d(vx_impact,vz_impact)

    return (x_impact, t_impact, angle_impact, v_impact)

def calculate_apogee_point(x0_, z0_, v0_, alpha0_, g_) :

    t_apogee = ( v0_ * math.sin( alpha0_ ) ) / g_
    x_apogee = v0_ * math.cos(alpha0_) * t_apogee + x0_
    z_apogee = ( ( v0_**2 * math.sin( alpha0_ )**2 ) / ( 2 * g_ ) ) + z0_
    
    vx_apogee = v0_ * math.sin( alpha0_ )

    return (t_apogee, x_apogee, z_apogee, vx_apogee)

if __name__ == "__main__" :
    g = 10
    m = 0.12
    x0 = 0
    z0 = 1
    v0 = 6
    alpha0 = 35
    alpha0 = ( alpha0 * math.pi )/180 # Converting in radians

    impact_tuple = calculate_impact_point(x0, z0, v0, alpha0, g)
    apogee_tuple = calculate_apogee_point(x0, z0, v0, alpha0, g)

    delta_alpha0 = 5
    delta_alpha0 = ( delta_alpha0 * math.pi )/180 # Converting in radians

    print("\nImpact calculation :")
    print("   | Time : {}".format(impact_tuple[1]))
    print("   | X : {}".format(impact_tuple[0]))
    print("   | Alpha : {}".format(impact_tuple[2]))
    print("   | Speed : {}".format(impact_tuple[3]))
    print("\nApogee calculation :")
    print("   | Time : {}".format(apogee_tuple[0]))
    print("   | X : {}".format(apogee_tuple[1]))
    print("   | Z : {}".format(apogee_tuple[2]))
    print("   | Speed : {}".format(apogee_tuple[3]))

    alpha_max = alpha0 + delta_alpha0
    alpha_min = alpha0 - delta_alpha0
    
    impact_max_tuple = calculate_impact_point(x0, z0, v0, alpha_min, g)
    impact_min_tuple = calculate_impact_point(x0, z0, v0, alpha_max, g)
    
    print("\nImpact max calculation :")
    print("   | Time : {}".format(impact_max_tuple[1]))
    print("   | X : {}".format(impact_max_tuple[0]))
    print("   | Alpha : {}".format(impact_max_tuple[2]))
    print("   | Speed : {}".format(impact_max_tuple[3]))
    print("\nImpact min calculation :")
    print("   | Time : {}".format(impact_min_tuple[1]))
    print("   | X : {}".format(impact_min_tuple[0]))
    print("   | Alpha : {}".format(impact_min_tuple[2]))
    print("   | Speed : {}".format(impact_min_tuple[3]))
    print("\n")

    nb_shoots = 1000000
    seed = 314159
    kl_1 = kl_generator(seed)
    
    rng_file = open("prng_ballistics.data","w")

    for i in range(nb_shoots) :
        #r = kl_1()
        r = random.gauss(alpha0,delta_alpha0)
        alpha0 = r * ( alpha_max - alpha_min ) + alpha_min
        impact_tuple = calculate_impact_point(x0, z0, v0, alpha0, g)
        
        rng_file.write("{}\n".format(impact_tuple[1]))

    rng_file.close()
    
    sys.exit(0)
