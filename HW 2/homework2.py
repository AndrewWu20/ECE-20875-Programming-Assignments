def histogram(data, n, min_val, max_val):
    # data is a list
    # n is an integer
    # min_val and max_val are floats

    # Write your code here
    if n <= 0:                      #If the number of bins is zero, there is no histogram and return an empty list
        return []
    if min_val == max_val:          #If the values are all the same, return an empty list
        print("Error: min_val and max_val are the same value")
        return []
    if min_val > max_val:           #If the min and max values are backwards, switch them
        temp_val = max_val
        max_val = min_val
        min_val = temp_val
    hist = n * [0]                  #Create hist as a list of n zeros
    w = (max_val - min_val)/n       #Calculation for bin width
    for value in data:              #Iterate through all values of data, if those values are within the range, do the calculation and add them to hist
        if value > min_val and value < max_val:
            i = int((value - min_val) / w)
            hist[i] += 1
    return hist
    # return the variable storing the histogram
    # Output should be a list
    

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day, person_to_month, person_to_year):
    #person_to_day, person_to_month, person_to_year are dictionaries

    # Write your code here
    month_to_person_data = {}                       #Set an empty dictionary
    current_year = 2022                             #Set the current year to 2022
    for person in person_to_month:                  #Iterate through the dictionary person to month and set variable to specific entries
        month = person_to_month[person]     
        day = person_to_day[person]
        year = person_to_year[person]
        age = current_year - year                   #Find age of person
        if month in month_to_person_data.keys():    #If two people have the same birth month, only include the older one in the dictionary
            if age > month_to_person_data[month][1][2]:
                print(month)
                month_to_person_data[month] = ((person, (day, year, age)))
        else:                                       #Else, go on as usual
            month_to_person_data[month] = ((person, (day, year, age)))        
    return month_to_person_data
    # return the variable storing output
    # Output should be a dictionary

# We first define the current year as 2022, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_person_data that will store the final data in the format specified in the problem statement.
# We iterate over the keys and values of the person_to_month dictionary using a for loop and the items() method.
# For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year dictionaries using the current name as the key.
# We then use the current month as the key and a tuple of (name, (day, year, age)) as the value to update the month_to_person_data dictionary.
# Finally, we return the month_to_person_data dictionary as the output of the function.