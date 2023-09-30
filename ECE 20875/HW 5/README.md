# Homework 5: Sampling, Hypothesis Testing, and Confidence Intervals
## Due: 02/17/2022 (NOTE: You have *one* week to complete this homework. This is a challenging homework, please start early!)
This homework will give you practice in hypothesis testing and confidence intervals with Python. It is the first homework that has a writeup component.

# THIS PDF DOCUMENT SHOULD BE SUBMITTED ON GRADESCOPE and Code will be sent to Github!
You will have recieved an email of your enrollment in the course. On Brightspace, under "Content", The modulue "Gradescope" has been added and it can be used as a link to gradescope. https://www.gradescope.com/ You should see the assignment named "homework 5" where you will upload your completed Writeup.pdf (It would be good to confirm you know how to do this prior to 11pm of the due date).

Submit code for this assignment as you normally would for previous assignments.

# Goals

In this homework you will:

1. Formulate hypotheses and carry out appropriate statistical tests
2. Compute confidence intervals based on appropriate assumptions
3. Work with a real dataset (student behavioral data)

# What to Submit

#### Note for this assignment, you will fill in your answers in the provided Writeup.pdf file. In addition, you must convert this file to a PDF and upload that as well. You must fill in your answers here and ensure it is included in your submitted repository to get credit for this homework. 
For this assignment you should submit:

(i) The Writeup.pdf file with all your answers filled in on Gradescope (it is a .pdf with fillable fields, make sure to save the .pdf once you have entered your answers!)

(ii) The problem2.py file on Github showing your work for Problem 2 

(iii) The problem3.py file on Github showing your work for Problem 3 

All your answers to each question should be clear in the writeup. Be sure to give explanations of your results if asked for in the question. It is recommended to have your code files print the values you are calculating for each question, but this is not required.

# Background

Before attempting the homework, please review the notes on sampling and hypothesis testing on the course website. Feel free to copy and modify any of the code we have provided for you here.

## Some motivation and helpful information on hypothesis tests with an example:
A hypothesis test takes the sample you collected and compares how its mean looks with respect to the sampling distribution. From the sample data, you calculate a single 'mean' value (`xbar`) to test against the 'population of means'. This is often done because if one has enough data sampled, the mean is distributed as a Gaussian distribution (per the Central Limit Theorem).  The good thing is that even if not much data could be collected, you have the option to use a Student's t test. The beauty of this is that virtually no matter what data you are testing (rainfall, test scores, salaries, errors, etc.), the methods you're being taught are applicable, regardless of the type of data you collect.

The 'assumed population mean' (null hypothesis) is the value you test against. For example, your friend Jake says "I reckon there's 3.4396 cm of rainfall here daily in spring."  If you want to prove him wrong (by running a hypothesis test), you would:
1. Collect samples of rainfall each day in spring at that location.
2. Compute their sample mean. 
3. Temporarily assume Jake is correct. (Null Hypothesis H0: mu = 3.4396 cm, Alternative Hypothesis H1: mu != 3.4396 cm) (!= means we only care whether Jake is wrong, if we wanted to prove there was more rainfall, H1 would instead be mu >= 3.4396 cm)
4. Hold Jake to a standard (alpha = 0.1, 0.05, 0.01, whatever seems appropriate to prove "your sample was rare beyond a doubt.")
5. Calculate the test statistic (the z-score or t-score, based on the number of datapoints you have collected or information on the true standard deviation value) from the equation in the lecture slides.
As a rule of thumb from the Central Limit Theorem:  if there are more than 29 samples OR you know the population standard deviation, use a Z-score. However, If there are less than 30 samples and you don't know the population standard deviation, use a T-score
6. Determine the p-value from your test statistic. Note: For each p-value, there corresponds a 'critical test statistic' value (or pair of values if a 2 tail test, but you really just care about the side your test point is on for which of the two you'd look at in that case.). This 'critical test statistic' value is either the t-score or z-score you found earlier.
7. Compare the p-value to the alpha value you set. If the p-value is smaller than alpha, you have proved Jake wrong (You reject the null hypothesis). If the p-value is larger than alpha, you have failed to prove Jake wrong, but he is not necessarily right because you have only "failed to reject" the null hypothesis.

## Confidence Intervals
Confidence intervals are somewhat a flipped perspective compared to hypothesis testing. Hypothesis testing yields claims like "I have rejected that the average wind speed is 20km/hr under significance value alpha=0.05" Whereas a confidence interval for the same claim might say something like "I am 95% confident that the true average wind speed falls in the range (15, 19) km/hr." Here, we notice that the value 20 did not fall in the confidence interval, and so if hypothesis tested at alpha = 1 - 0.95 = 0.05 like we had, this confidence interval already shows the result of the test would be to reject H0: mu=20km/hr.

Why do we have both hypothesis testing and confidence intervals then? There's a number of reasons, but arguably one of the main distinguishing factors is that hypothesis testing is used for making or disproving claims, and confidence intervals don't have to involve proving or disproving a claim but can instead provide a valuable way of bounding an unknown value to some level of certainty.

## Python Functions

### Reading .txt files
There are several different file formats for data, including .csv and .json which we will cover later. One of the simplest is storing in text (.txt) files, which is how the data is provided to you in this homework. To get each line of a text file `sample.txt` stored as a separate element in a list `data`, you can write:

```
myFile = open('sample.txt')
data = myFile.readlines()
myFile.close()
```

Each element of `data` will be a string. To convert them to floats, we can use a list comprehension:

```
data = [float(x) for x in data]
```

### Mean and Standard Deviation
While they are relatively easy to write manually, the `numpy` library in Python has built-in functions for finding the mean and standard deviation of a list. To import it, we can write:

```
import numpy as np
```

The mean of `data` is found as

```
avg = np.mean(data)
```

To find the standard deviation, type

```
sd = np.std(data, ddof=x)
```
where `x` is the differential from the number of samples `N` to determine the degrees of freedom. When we are calculating the standard deviation of a sample, the denominator in equation N-1 so we would set  `ddof=1` . If we are calculating the standard deviation of the population (i.e. we know the population mean, the numerator in the standard deviation question would be just N, (in which case `ddof=0`).

### Standard Normal and Student's t Distributions
The two distributions you will rely on heavily in this homework are the `standard normal (z)` and the `student's t` distributions.

To import the standard normal distribution, type

```
from scipy.stats import norm
```

Then, to find the probability that a value lies below a particular point `z_c`, type

```
p = norm.cdf(z_c)
```

Inversely, to find the point `z_c` below which the probability is `p` (i.e., the inverse cdf), type

```
z_c = norm.ppf(p)
```

To import the Student's t distribution, type

```
from scipy.stats import t
```

Then, to find the probability that a value lies below a particular point `t_c`, type

```
p = t.cdf(t_c, df)
```
where `df` is the degrees of freedom for the t distribution.

Inversely, to find the point `t_c` below which the probability is `p` (i.e., the inverse cdf), type

```
t_c = t.ppf(p)
```

## Very Important Notes for Your Analysis:
In this homework, you will work with survey data from vehicle owners on their vehicles age. 

In short, you will be working with three sampled groups, the first group was just asked the age of their vehicles (stored in vehicle_survey_1.txt). After doing that analysis it was decided to more samples whould be collected, one from the population of student vehicles whose owners did not do their own oil changes (stored in vehicle_survey_2.txt), and the population of student vehicles who owners do their own oil changes (stored in vehicle_survey_3.txt). 

You will be doing hypothesis tests to determine such things as 'is the student vehicle mean age 8 years old?' and 'was there a difference in vehicle age if a student changed their own oil?'

# Instructions

## 0) Set up your repository

Click the link on Piazza to set up your repository for HW 5, then clone it.

The repository should contain two files aside from this readme, both of which you will use in Problem 1:

1. `vehicle_survey_1.txt`, a text file containing the age of student vehicles on campus.
2. `vehicle_survey_2.txt`, a text file containing the age of student vehicles whose owners do not personally change their oil.
3. `vehicle_survey_3.txt`, a text file containing the age of student vehicles whose owners do personally change their oil.
#### Note: For both problems 1 and 2 whenever the standard error is computed we do not know the true population mean (i.e., when using `np.std(data, ddof=x)`, `x` should be set to `1`)

## 1) Problem 1: Sampling

Follow the instructions on the Writeup.pdf file, the one that you will submit to Gradescope
Writeup.pdf is a .pdf with fillable fields, make sure to save the .pdf once you have entered your answers!

## 1) Problem 2: Hypothesis Testing

Answer the following questions on the Writeup.pdf - the one you will submit to Gradescope
Use and submit the given problem2.py file for your code

This problem concerns the datasets of vehicle ages in `vehicle_survey_1.txt` and `vehicle_survey_2.txt` and `vehicle_survey_3.txt`.

1. A student exploring making a car maintenance subscription service an "'uber' for oil changes" is pretty confident that the average age of used cars on campus (the `vehicle_survey_1` population) is 8 years old. Formulate null and alternative hypotheses for a statistical test that seeks to challenge this belief. What are the null and alternative hypotheses? What type of test should be used and why?

2. Carry out this statistical test using the `vehicle_survey_1` sample. Report the sample size, the sample mean, the standard error, the standard score (Z or t), and the p-value. Are the results statistically significant at a significance level of 0.05? How about 0.10?
What (if anything) can we conclude about the hypothesis at the two different confidence levels?

3. What is the largest standard error for which the test will be significant at a level of 0.05? What is the corresponding minimum sample size? (You may assume that the population variance and mean does not change.)

4. Suppose the student is also convinced that the mean age is **different** between vehicles whose owners regularly change their own oil (the `vehicle_survey_2` population) and those who do not (the `vehicle_survey_3` population). Formulate null and alternative hypotheses that seek to validate this belief. What are the null and alternative hypotheses, and what type of test can be used?

5. Carry out this statistical test using the `vehicle_survey_2` and `vehicle_survey_3` samples. Report the sample sizes, the sample means, the standard error, the z-score, and the p-value. Are the results significant at levels 0.05 or 0.10? What (if anything) can we conclude about the hypothesis at the two different confidence levels?


## 2) Problem 3: Confidence Intervals 

Answer the following questions on the Writeup.pdf - (reminder! you will upload this .pdf to Gradescope)
Use and submit the given problem3.py file for your code

You are working for a startup that has now built several prototype robots. The following dataset of the weight of the robots:

`[196.8 , 196.7 ,189.4 ,196.6 ,173.5 ,195.2 ,217.9 ,195.2 ,194.3 ,211.2 ,201.0 ,197.1 ,209.1 ,207.3 ,206.4 ,195.2 ,190.1 ,203.2 ,194.1 ,201.8]`


1. Use the sample to construct a 90% confidence interval for the weight of the robots on average. Report whether you will use a z-test or t-test and report the sample mean, the standard error, the standard statistic (t or z value), and the interval. (Think, which distribution should you use here if very few datapoints are available?)

2. Repeat Q1 for a 95% confidence interval. What is the standard statistic (t or z value) and what is the interval? Is your interval wider or narrower compared to using the 90% confidence interval?

3. Repeat part 2 if you are told that the population standard deviation is `10`. (Think, which distribution should you use here now that you have the true population standard deviation?). Report whether you will use a z-test or t-test and the values for the sample mean, standard error, standard statistic, and confidence interval. Is your interval wider or narrower than the interval computed in Q2?


# Submitting your code to github and the writeup on gradescope

Please commit and push the latest version of your code files  as you have done in previous assignments. Please verify your submitted files by looking at GitHub online. 

You will have recieved an email of your enrollment in the course. On Brightspace, under "Content", The modulue "Gradescope" has been added and it can be used as a link to gradescope. https://www.gradescope.com/ You should see the assignment named "homework 5" where you will upload your completed Writeup.pdf (It would be good to confirm you know how to do this prior to 11pm of the due date).

And again, Writeup.pdf is a .pdf with fillable fields, make sure to save the .pdf once you have entered your answers!


