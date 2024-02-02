import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([196.8 , 196.7 ,189.4 ,196.6 ,173.5 ,195.2 ,217.9 ,195.2 ,194.3 ,211.2 ,201.0 ,197.1 ,209.1 ,207.3 ,206.4 ,195.2 ,190.1 ,203.2 ,194.1 ,201.8])
#data = np.array([199.7, 202.2,201.1,201.7,200.3,203.7,203.9,202.0,202.9,201.2,201.8,203.6,200.9])
#To run testcase, comment first data and uncomment second data

# code for question 1
print('Problem 1 Answers:')
# code below this line
sample_size = len(data)                     #Calculate values used to compute confidence interval
sample_mean = sum(data) / sample_size
std_dev = np.std(data, ddof = 1)
std_error = std_dev / m.sqrt(sample_size)

confidence_percent = 90                     #Compute 90% confidence interval
confidence_decimal = confidence_percent / 100
t_score = stats.t.ppf(1 - (1 - confidence_decimal) / 2, sample_size - 1)
max_val = sample_mean + (t_score * std_error)
min_val = sample_mean - (t_score * std_error)
confidence_interval = max_val - min_val

print(f"Sample Mean: {round(sample_mean, 4)}")  #Print statements for pdf answers
print(f"Standard Error: {round(std_error, 4)}")
print(f"Standard Score: {round(t_score, 4)}")
print(f"{confidence_percent}% confidence interval: [{round(min_val,4)},{round(max_val,4)}]")
print(f"Difference in confidence interval: {round(confidence_interval,4)}")

# code for question 2
print('Problem 2 Answers:')
# code below this line
confidence_percent = 95                     #Compute 95% confidence interval
confidence_decimal = confidence_percent / 100
t_score = stats.t.ppf(1 - (1 - confidence_decimal) / 2, sample_size - 1)
max_val = sample_mean + (t_score * std_error)
min_val = sample_mean - (t_score * std_error)
confidence_interval = max_val - min_val

print(f"Standard Error: {round(std_error, 4)}") #Print statements for pdf answers
print(f"Standard Score: {round(t_score, 4)}")
print(f"{confidence_percent}% confidence interval: [{round(min_val,4)},{round(max_val,4)}]")
print(f"Difference in confidence interval: {round(confidence_interval,4)}")

# code for question 3
print('Problem 3 Answers:')
# code below this line
std_dev = 10                                #Compute 95% confidence interval with given std dev
sample_size = len(data)
sample_mean = sum(data) / sample_size
std_error = std_dev / m.sqrt(sample_size)
z_score = stats.norm.ppf(.975)
max_val = sample_mean + (z_score * std_error)
min_val = sample_mean - (z_score * std_error)
confidence_interval = max_val - min_val

print(f"Standard Error: {round(std_error, 4)}") #Print statements for pdf answers
print(f"Standard Score: {round(z_score, 4)}")
print(f"{confidence_percent}% confidence interval: [{round(min_val,4)},{round(max_val,4)}]")
print(f"Difference in confidence interval: {round(confidence_interval,4)}")

# code for question 4
print('Problem 4 Answers:')
# code below this line
print(f"Question four was not provided")    #Question 4 was not given in pdf
