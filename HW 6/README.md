# Homework 6: Regular Expressions
## Due: Monday 06 March 2023 at 11:59 pm ET

The length of this homework is inversely proportional to your knowledge in writing regular expressions, both for finding matches and for doing substitutions.

A good resource to use is https://regex101.com/ for checking your expressions

## Background

Please refresh your memory of regular expressions using the class notes. You may also find the Python [documentation on regular expressions](https://docs.python.org/3.6/library/re.html) useful.

A few helpful reminders: 

### Testing for Patterns

When you use `re.search` to find a regular expression match, it returns a `Match` object if the pattern exists in the string (we will see more about objects later in the semester). If *there is no match*, then `re.search` (and `re.match` and `re.findall`) will return `None`,  which you can test for:

```
p = re.compile('pattern')
if (p.search(s)) :
   # This branch will execute if the pattern is found
else :
   # this branch will execute if the pattern is *not* found
```

### Substituting with functions

A common use of `re.sub` is to substitute one string for another (remember that you can use the *groups* that you match in a pattern as part of your string substitution):

```
s = "loooool"
p = re.compile('(l)o+(l)')
p.sub(r'\1o\2', s) #replace "loooool" with "lol"
```

You can also call a method instead of providing a replacement string. This method will be called with the `Match` object corresponding to the matched string, and should return a string:

```
def replFun(m) :
   return m.group(2).upper()
s = "loooool"   
p = re.compile('(l)(o+)(l)')
m = p.search(s)
p.sub(r'\1'+replFun(m) +r'\3', s) #replace "loooool" with "lOOOOOl"
```
Remember that `(`, `)`, `-` and `.` are special characters for regular expressions. To search for those characters, you need to precede them with a backslash: `\(` `\)`, `\-`, `\.`. 

# Instructions

## 0) Set up your repository

Click the link on Piazza to set up your repository for HW 6, then clone it.

The repository should contain two files:

1. `problems.py`, the file in which you will fill in the functions for the problems. This also contains test code you can use to test your solutions.
2. This README.

## Problem 1: Regular expression matches

Congratulations! You have been hired as a new agent of SHEILD (security organization that defends Earth). The world is getting more and more superheroes and your first task is to work on the database of superhero emails (even those with telepathic powers need a traditional way to communicate). However, it appears that the evil forces are at work, the nefarious Doctor Octavious has hacked SHEILDs database and has entered in false emails. You must create a function that can correctly identify which emails are valid.

A valid email at SHEILD has the following structure:

Fill in the function `problem1`. This function should return the string `valid` if the input string *is a valid email address* and `invalid` if not. We define a valid email as follows:

1. The email **must** begin with the ID number of the hero, from 100 up to 799 (This is dictated by SHEILD's numbering rules) followed by a "."(period)
2. After the "." the email **must** have a name composed of upper or lower case letters, containing at least 1, but no more than 10 letters.
3. The email **may** have any amount of numbers following the letters of the name, but anything else between the name and the @ symbol is invalid
4. The email **must** have the “@” symbol followed by either "sheild.gov" or "avengers.com"
5. There **must** be nothing following the .gov or .com

Correct Examples:
```
123.iamironman@avengers.com
250.Srogers1776@avengers.com
100.nickfury@sheild.gov
```

Incorrect Examples:
```
144.venom@avengers.comasdf (broke rule 5)
942.hyperion@avengers.com (breaks rule 1, incorrect number in front)
567.greengoblin@sheild.gov (breaks rule 2, too many letters)
324drdoom324@avengers.com (breaks format established in 1 (does not have ".")
765.Hosborn*876@sheild.gov (breaks rule 3, has something other than numbers after name and between "@" symbol)
234.vulture@sheild.com (breaks rule 4, not correct ending)
```

*ANY other format should not count as a valid email. Spaces before or after an otherwise valid email is considered invalid.*

Because we are looking for the entire string to be an email, you can either use `^` and `$` to force a match to be at the beginning and end of a string, or you can use `fullmatch` instead of `match` or `search`.

## Problem 2: Groups

Wow, there are a lot of problems on your first day, the list of Heros and their vehicles have been lost. Luckily you have some transcripts that have the students and their ships. Fill in function problem 2 to return a tuple of the student's name and the spaceship that the student drives. 

A transcript would have the format *Super Hero rides/flies a vehicle* and will have the following conditions:

1. A Super Hero's name can be one word, or two words. The word or words in a name must start with a captial letter. 
2. The verb can be either "rides" or "flies"
3. If the vehicle has a Name (first letter is capitalized), it can be two words. If the vehicle does not have a name, it will be one word and contain all lowercase letters. 
4. If the above conditions are both not met, there is no match. You will then return a tuple of strings (“nohero”, “noname”)

Example: 

`The Wasp rides the wind, but Iron Man rides a Quinjet`

Although there is the phrase “Wasp rides” it does not have "a" following the word "rides". Therefore, your program needs to keep looking for the correct pattern. 

This pattern is found in “Iron Man rides a Quinjet”. The correct output of the problem2 would be ("Iron Man", Quinjet)


Fill in the function `problem2`. This function should search an input string for the student and ship then return a tuple of them.

`Captain America rides a Harley`

you should return:

`('Captain America','Harley')`

If you pass in:

`No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise`

you should return:

`('Spider Man', 'Harley')`

*This is because No one did not have a capitalized first letter in the word preceding "rides"*


If you pass in: 

`Starlord flies many ships, but Rocket flies a Warbird Special much faster`

you should return:

`('Rocket', 'Warbird Special')`

_vehicle has a 2 word name - both Warbird and Special are capitalized_

If you pass in: 

`Groot rides a spaceship`

you should return:

`('Groot', 'spaceship')`

_vehicle does not have a name - returned value is just one word and lowercase_




**Be careful not to return extra spaces in the return value. You may need to do a little bit of extra processing of the string captured by your group to ensure this. You will receive partial credit for having spaces. Please remove extra spaces for full credit.**

## Problem 3: Substitution
Oh no! Someone has changed these audio transcripts from mission reports. You must correct the super hero name!  

Replace the word Boy/Girl or boy/girl with Man/Woman. Fill in the function `problem3` to returns a string with the correct word restored. 

Here are the rules for replacement
1. Boy/Girl or boy/girl should be replaced with Man/Woman if the word prior to it is a name (starts with a captial letter)
2. If no match is found, return "nomatch"

Here are some examples: 

`Spider Girl, I need help!`

*Should return*

`Spider Woman, I need help!`


`There is a boy trapped in a burning building Iron Boy`

*Should return*

`There is a boy trapped in a burning building Iron Man`

_This is because the first boy is not proceeded by a word that has a Capital letter_





**Be careful not to return extra spaces in the final output. You may need to do a little bit of extra processing of the string captured by your group to ensure this. You will receive partial credit for having unwanted spaces. Please remove extra spaces for full credit.**

# Testing Your Code

To test your code, run the `problems.py` file. These tests are not exhaustive, passing them does not guarantee full credit on the homework.

# What to Submit

Please submit `problems.py` with all the functions filled in. 

# Submitting your code

Please add, commit and push the latest version of your code, as you did in the previous HW.
Do not make any modifications to this post submission and prevent the late penalty.
