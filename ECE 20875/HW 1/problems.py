def problem0(num):
    """
        This is a sample problem and solution that are not part of the grade. Its purpose is just to familiarize
        yourself with functions and the format for this homework

        The objective of this sample problem is to determine if the num is divisible by 3, if it is the function will
        return the string "divisible" otherwise it will return "not divisiable

        I will use the modulo operator "%"  (might come in handy in other homework problems - worth a google search!)


    """
    
    #******Insert your code here ****
    if num % 3: #Use modulo operator to get remaineder. If it not 0 (which would be interpretted like a 'False' in the if statement, then we know it is not divisiable
        return "not divisible"
    else:
        return "divisible"
    # *******************************



def problem1(year):
    """
    When given a year, determine if the year is even or odd, but if it is an election year (divisible by 4) return

    To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

    Odd year: Return a string "odd"
    Even year: Return "even" unless it is leap year, then return a string "leap"
    leap year: Return a string "leap"
    
    Remember to comment your code!
    """
     #******Insert your code here ****
    if year % 2:                        #If the year is not divisible by two, it is an odd year
        return "odd"
    else:
        if year % 4:                    #If the year is not divisible by four, it is an even non leap year
            return "even"
        else:
            if year % 100:              #If the year is not divisible by one hundred, its an even leap year
                return "leap"
            else:
                if year % 400:          #If the year is not divisible by four hundred, its an end-of-century year that is not a leap year
                    return "even"
                else:
                    return "leap"       #If the year is divisible by four hundred, its an end-of-century leap year
    # *******************************

def problem2(given_number):
    """
    When given a return a list of all values that are trianglular numbers that are less than or equal to the given_number
    triangle number: https://en.wikipedia.org/wiki/Triangular_number

    Remember you are returning a list of numbers!
    
    And remember to comment your code!
    """
     #******Insert your code here ****
    triangular_nums_list = []                               #Create an empty list
    for i in range(1, given_number+1):                      #Repeat loop for given num + 1 times using range operator
        triangular_nums = i*(i+1)/2
        if triangular_nums <= given_number:                 #If the triangle num is less than given num, append to list, otherwise, return list
            triangular_nums_list.append(triangular_nums)
    return triangular_nums_list
    # *******************************
#When you run this python file you should be able to check your work with these test cases

if __name__ == '__main__' :
    #Below are the Test Cases!
    print("\nProblem 0:")
    print("Student answer was:", problem0(1), "    Problem 0 answer correct?",problem0(1)=='not divisible', )
    print("Student answer was:", problem0(2), "    Problem 0 answer correct?",problem0(2)=='not divisible', )
    print("Student answer was:", problem0(3), "    Problem 0 answer correct?",problem0(3)=='divisible', )
    print("Student answer was:", problem0(4), "    Problem 0 answer correct?",problem0(4)=='not divisible', )

    print("\nProblem 1:")
    print("Problem 1 answer correct?",problem1(2023)=='odd', "    Student answer was:", problem1(2023))
    print("Problem 1 answer correct?",problem1(2022)=='even', "    Student answer was:", problem1(2022))
    print("Problem 1 answer correct?",problem1(2020)=='leap', "    Student answer was:", problem1(2020))
    print("Problem 1 answer correct?",problem1(2000)=='leap', "    Student answer was:", problem1(2000))
    print("Problem 1 answer correct?",problem1(1900)=='even', "    Student answer was:", problem1(1900))

    print("\nProblem 2:")
    print("Problem 2 answer correct?",problem2(8)==[1, 3, 6], "      Student answer was:", problem2(8))
    print("Problem 2 answer correct?",problem2(10)==[1, 3, 6, 10], "      Student answer was:", problem2(10))
    print("Problem 2 answer correct?",problem2(16)==[1, 3, 6, 10, 15], "      Student answer was:", problem2(16))
    print("Problem 2 answer correct?",problem2(21)==[1, 3, 6, 10, 15, 21], "      Student answer was:", problem2(21))
