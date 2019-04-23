import sys
import csv

class stat_analysis :

    def __init__(self, data_file_, nb_column_) :
        self.data_file = data_file_

        return 
        
    def get_mean(self, column_id_) :
        fname = self.data_file
        total = 0
        total_line_number = 0

        input_file = open(self.data_file, "r")
        for line in input_file :
            line_array = line.split()
            total = total + float(line_array[column_id_])

            total_line_number = total_line_number + 1
        input_file.close()
        mean = total / total_line_number
        
        return ( mean )

    def get_variance(self, column_id_) :
        fname = self.data_file
        
        total_line_number = 0
        mean = self.get_mean(column_id_)
        value_minus_mean_sum = 0
        variance = 0

        input_file = open(self.data_file, "r")
        for line in input_file :
            line_array = line.split()
            value_minus_mean_sum = value_minus_mean_sum + (float(line_array[column_id_]) - mean)**2

            total_line_number = total_line_number + 1
        input_file.close()
        
        variance = value_minus_mean_sum / total_line_number
        
        return ( variance )

    def __str__(self) :
       return ("test")

if __name__ == "__main__" :
    data_file = "random_segments_data.csv"

    stat = stat_analysis(data_file, 2)
    print ( "Mean X value" )
    print ( stat.get_mean(0) )
    print ( "Variance X value" )
    print ( stat.get_variance(0) )
    print ( "Mean Y value" )
    print ( stat.get_mean(1) )
    print ( "Variance Y value" )
    print ( stat.get_variance(1) )

    sys.exit(0)
