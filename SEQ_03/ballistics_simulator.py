# Two dimentional ballistic with wind
# by  Tom Genard - 2019.03.30
# 
# Or as I call it, Norman ballistics

import sys
import math
from kl_generator import *
from vector_2d import *
from test_functions_library import *

class ballistics_simulator :
    def __init__(self,duration_sim_,nb_step_sim_,num_winds_,duration_wind_,x0_,z0_,friction_val_,vx0_,vz0_,g_,mass_) :
        if ( duration_sim_ < num_winds_ * duration_wind_ ) :
            sys.stderr.write("ERROR : Total wind duration superior to the duration of the simulation!\n")
            sys.exit(1)

        test_value_float(duration_sim_)
        test_value_float(nb_step_sim_)
        test_value_float(num_winds_)
        test_value_float(duration_wind_)
        test_value_float(x0_)
        test_value_float(z0_)
        test_value_float(friction_val_)
        test_value_float(vx0_)
        test_value_float(vz0_)
        test_value_float(g_)
        test_value_float(mass_)

        test_value_positive(duration_sim_)
        test_value_positive(nb_step_sim_)
        test_value_positive(num_winds_)
        test_value_positive(duration_wind_)
        test_value_positive(g_)
        test_value_positive(mass_)

        self.duration_sim  = duration_sim_
        self.nb_step_sim   = nb_step_sim_
        self.step_sim      = duration_sim_ / nb_step_sim_
        self.num_winds     = num_winds_
        self.duration_wind = duration_wind_
        self.x0            = x0_
        self.z0            = z0_
        self.friction_val  = friction_val_
        self.vx0           = vx0_
        self.vz0           = vz0_
        self.g             = g_
        self.mass          = mass_
        self.environment   = []

        return

    def generate_environment(self,ud01_) :
        self.environment_cuts = [] # We cut the environment into smaller randomly sized portions to avoid overlap of generated winds

        for i in range(self.num_winds - 1) :
            r01 = ud01_()
            r01 = r01 * self.duration_sim
            self.environment_cuts.append(r01)

        # Let's order these times into an ascending order for simplicity
        i = 0
        j = 1
        is_in_order = 0
        order_index = 0

        while ( is_in_order == 0 ) :
            if ( self.environment_cuts[i] > self.environment_cuts[j] ) :
                c = self.environment_cuts[i]
                self.environment_cuts[i] = self.environment_cuts[j]
                self.environment_cuts[j] = c

                order_index = 0

            else :
                order_index = order_index + 1

            if ( order_index == len(self.environment_cuts) - 1 ) :
                is_in_order = 1

            if ( j == len(self.environment_cuts) - 1 ) :
                i = 0
                j = 1

            else :
                i = i + 1
                j = j + 1

        # We now generate the winds in each portion
        k = 0

        while ( k < len(self.environment_cuts) ) :
            r02 = ud01_()

            if ( k == 0 ) :
                self.environment.append( r02 * ( self.environment_cuts[k] - self.duration_wind ) )

            elif ( k < ( len(self.environment_cuts) - 1 ) ) :
                self.environment.append( r02 * ( self.environment_cuts[k] - self.environment_cuts[k-1] - self.duration_wind ) + self.environment_cuts[k-1] )

            else :
                self.environment.append( r02 * ( self.duration_sim - self.environment_cuts[k] - self.duration_wind ) + self.environment_cuts[k] )

            k = k + 1

        return

    def print_environment(self) :
        for i in range( len(self.environment) ) :
            print (self.environment[i])

        return

    def is_in_wind(self,time_,environment_array_) :
        l = 0

        for l in range(len(environment_array_)) :
            if ( time_ >= environment_array_[l] and time_ <= ( environment_array_[l] + self.duration_wind ) ) :
                return True

        return False

    def ballistics_stepper_sim(self) :

        t_sim = 0
        t = self.duration_sim
        sim_file = open("sim_file.data","w")

        OM = vector_2d(self.x0,self.z0)
        sim_file.write("{} {}\n".format(OM.get_x(),OM.get_y()))

        x = self.x0
        z = self.z0

        vx = self.vx0
        vz = self.vz0

        while ( t_sim < t ) :
            x = OM.get_x()
            z = OM.get_y()

            if ( self.is_in_wind(t_sim,self.environment) == True ) :
                vx = vx*math.exp(- ( self.friction_val / self.mass) )
                # Otherwise, vx is constant in a frictionless world

            vz = vz - ( self.g * self.step_sim ) 

            x = x + vx * self.step_sim
            z = z + vz * self.step_sim

            OM.set_x(x)
            OM.set_y(z)

            sim_file.write("{} {}\n".format(OM.get_x(),OM.get_y()))

            t_sim = t_sim + self.step_sim

        impact_site = ( OM.get_x(), OM.get_y() )
        sim_file.close()

        return impact_site

if __name__ == "__main__" :
    test_duration_sim  = 100
    test_nb_step_sim   = 10000
    test_num_winds     = 10
    test_duration_wind = 1
    test_x0            = 0
    test_z0            = 0
    test_friction_val  = 0.1
    test_vx0           = 20
    test_vz0           = 20
    test_g             = 9.81
    test_mass          = 10

    seed = 4242424242
    kl01 = kl_generator(seed)

    impact_file = open("impact_file.data","w")
    number_sim = 10000
    index_sim = 0

    while ( index_sim < number_sim ) :
        sim01 = ballistics_simulator(test_duration_sim,test_nb_step_sim,test_num_winds,test_duration_wind,test_x0,test_z0,test_friction_val,test_vx0,test_vz0,test_g,test_mass)
        sim01.generate_environment(kl01)
        #sim01.print_environment()
        impact = sim01.ballistics_stepper_sim()

        impact_file.write("{}\n".format(impact[0]))

        if ( index_sim/100 == int(index_sim/100) ) :
            print ( index_sim )
        index_sim = index_sim + 1

    impact_file.close()


    sys.exit(0)