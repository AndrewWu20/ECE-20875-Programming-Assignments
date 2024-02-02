import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
myFile = open('vehicle_survey_1.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close() # No longer need to have file open

#To run testcases, replace the files in the myfile lines with the testcase files

# code for question 2
print('Problem 2 Answers:')
# code below this line
sample_size = len(data1)                            #Calculates all the necessary values to obtain the p value
sample_mean = sum(data1) / sample_size
std_dev = np.std(data1, ddof = 1)
std_error = std_dev / m.sqrt(sample_size)
z_score = (sample_mean - 8) / std_error
p_val = 2 * stats.norm.cdf(-abs(z_score))

print(f"Sample size: {round(sample_size, 4)}")      #Print statments to get answers for pdf
print(f"Sample mean: {round(sample_mean, 4)}")  
print(f"Standard deviation: {round(std_dev, 4)}")
print(f"Standard error: {round(std_error, 4)}")
print(f"Z score: {round(z_score, 4)}")
print(f"P value: {round(p_val, 4)}")

# code for question 3
print('Problem 3 Answers:')
# code below this line
sig_lvl = .05                                       #Declare values to be used later
p_val2 = 2 * stats.norm.cdf(-abs(z_score))
while p_val2 >= sig_lvl:                          #While the p value is greater than the significance level, calculate and update values
    sample_size = sample_size + 1
    std_error = np.std(data1, ddof = 1) / m.sqrt(sample_size)
    z_score = (sample_mean - 8) / std_error
    p_val2 = 2 * stats.norm.cdf(-abs(z_score))

print(f"Largest standard error: {round(std_error, 4)}") #Print statements for pdf answers
print(f"Minimum sample size: {round(sample_size, 4)}")

# code for question 5
print('Problem 5 Answers:')
myFile1 = open('vehicle_survey_2.txt')
data1 = myFile1.readlines()
myFile2 = open('vehicle_survey_3.txt')
data2 = myFile2.readlines()
data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close() # No longer need to have file open
myFile2.close() # No longer need to have file open
# code below this line
sample_size_data1 = len(data1)                      #Calculate values to use to obtain p value
sample_size_data2 = len(data2)
sample_mean_data1 = sum(data1) / sample_size_data1
sample_mean_data2 = sum(data2) / sample_size_data2
std_dev_data1 = np.std(data1, ddof = 1)
std_dev_data2 = np.std(data2, ddof = 1)
std_error_data12 = m.sqrt(((std_dev_data1 ** 2) / sample_size_data1) + (((std_dev_data2 ** 2) / sample_size_data2)))
t_data12 = (sample_mean_data1 - sample_mean_data2) / ((std_error_data12))
p_val_data12 = 2 * stats.norm.cdf(-abs(t_data12))

print(f"Sample size for data1: {round(sample_size_data1, 4)}")  #Print statements for pdf answers
print(f"Sample size for data2: {round(sample_size_data2, 4)}")
print(f"Sample mean for data1: {round(sample_mean_data1, 4)}")
print(f"Sample mean for data1: {round(sample_mean_data2, 4)}")
print(f"Standard error: {round(std_error_data12, 4)}")
print(f"Two sample t score: {round(t_data12, 4)}")
print(f"P value: {p_val_data12:.4e}")









