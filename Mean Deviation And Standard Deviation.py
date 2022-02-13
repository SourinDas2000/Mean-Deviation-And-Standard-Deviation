
# Given below is the frequency distribution of unit test marks of a class of 65 students. The total marks of the test is 20 but the highest marks obtained is 19 while the lowest is 4. Every other student performed inside this range. This program calculates the Mean Deviation and Standard Deviation of the following data.


'''

 Frequency distribution of test marks of 60 student :
    
               score      Frequency                     
       
               4 - 5            4
               6 - 7           10
               8 - 9           20
              10 - 11          15
              12 - 13           8 
              14 - 15           3
              16 - 17           4
              18 - 19           1
                       
                    Total :    65                  
'''
                                                               

from statistics import mean

import math


# Mid-points :

list1 = list(range(4, 6))

midpoint1 = mean(list1)

list2 = list(range(6, 8)) 

midpoint2 = mean(list2)

list3 = list(range(8, 10))

midpoint3 = mean(list3)

list4 = list(range(10, 12))

midpoint4 = mean(list4)

list5 = list(range(12, 14))

midpoint5 = mean(list5)

list6 = list(range(14, 16))

midpoint6 = mean(list6)

list7 = list(range(16, 18))

midpoint7 = mean(list7)

list8 = list(range(18, 20))

midpoint8 = mean(list8)


midpointlist = [midpoint1, midpoint2, midpoint3, midpoint4, midpoint5, midpoint6, midpoint7, midpoint8] # (x)


# Mean :
    
frequency = [4, 10, 20, 15, 8, 3, 4, 1] # (f)

frequency_multiplied_by_midpointlist = [x*y for x,y in zip(frequency, midpointlist)] # (fx)

summation_of_fx = sum(frequency_multiplied_by_midpointlist) # (Σfx)

summation_of_frequency = sum(frequency) # (Σf)

mean = summation_of_fx / summation_of_frequency # (x̅ = Σfx / Σf)

print("RESULT : ")

print("\n\n Mean of the given data is " + str(mean))  


# Mean Deviation :
    
midpoint_minus_mean = [abs(midpoint1 - mean), abs(midpoint2 - mean), abs(midpoint3 - mean), abs(midpoint4 - mean), abs(midpoint5 - mean), abs(midpoint6 - mean), abs(midpoint7 - mean), abs(midpoint8 - mean)] # (|x -x̅|)

frequency_multiplied_by_midpoint_minus_mean = [x*y for x,y in zip(frequency, midpoint_minus_mean)] # (f|x -x̅|)

summation_of_frequency_multiplied_by_midpoint_minus_mean = sum(frequency_multiplied_by_midpoint_minus_mean) # (Σf|x -x̅|)

mean_deviation = summation_of_frequency_multiplied_by_midpoint_minus_mean / summation_of_frequency # (md = Σf|x -x̅| / Σf)

print("\n Mean Deviation of the given data is " + str(mean_deviation))


# Standard Deviation :
    
midpoint_minus_mean_square = [i*i for i in midpoint_minus_mean] # (|x -x̅|²)

frequency_multiplied_by_midpoint_minus_mean_square = [x*y for x,y in zip(frequency, midpoint_minus_mean_square)] # (f|x -x̅|²)

summation_of_frequency_multiplied_by_midpoint_minus_mean_square = sum(frequency_multiplied_by_midpoint_minus_mean_square) # (Σf|x -x̅|²)

variance = summation_of_frequency_multiplied_by_midpoint_minus_mean_square / summation_of_frequency # (σ² = (Σf|x -x̅|² / Σf)

standard_deviation = math.sqrt(variance) # (σ = √(Σf|x -x̅|² / Σf)

print("\n Standard Deviation of the given data is " + str(standard_deviation) + "\n")


''' Created by Sourin Das '''