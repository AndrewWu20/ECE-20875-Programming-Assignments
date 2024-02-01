import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: 'valid' or invalid
    """
    email_address = r'^([1-7]\d{2})\.[A-Za-z]{1,10}\d*@(avengers\.com|sheild\.gov)$'    #Make a variable of a valid email address given the constraints imposed by SHEILD
    if re.match(email_address, searchstring):                        #If the email matches, return valid, otherwise, return invalid
        return 'valid'
    else:
        return 'invalid'
    

def problem2(searchstring):
    """
    Extract Hero Name and vehicle.

    :param searchstring: string
    :return: tuple
    """
    hero_vehicle = re.compile(r'(([A-Z]\w+ )+)((rides)|(flies))( a) ((([A-Z]\w+\s*)+)|(\w+))')  #Create variable of correct constraints
    match = re.search(hero_vehicle, searchstring)       #Matches created variables with matching cases in search string based on constraints
    if match:       #If there is a match, print the hero name and the vehicle/vehicle name
        hero = match.group(1).rstrip()
        ship = match.group(7).rstrip()
        return (hero, ship)
    else:                                               #Else, return 'nohero' and 'noname'
        return('nohero', 'noname')
    


def problem3(searchstring):
    """
    Boy/Girl or boy/gir with Man/Woman.

    :param searchstring: string
    :return: string
    """
    hero_gender = re.compile("([A-Z][a-z]*) (Boy|boy|Girl|girl)")   #Checks for a hero name and if it is followed by boy or girl
    incorrect =  re.search(hero_gender, searchstring)                   #Find all of the ones matching the criteria above
    if incorrect:                                                   #If there are names that need to be changed, change them to 'woman' for girl and 'man' for boy
        if incorrect.group(2) == "Girl" or incorrect.group(2) == "girl":
            new_transcript = hero_gender.sub(incorrect.group(1) + " Woman", searchstring)
        else:
            new_transcript = hero_gender.sub(incorrect.group(1) + " Man", searchstring)
    else:                                                           #Else, return no match
        new_transcript = "nomatch"
    return new_transcript


if __name__ == '__main__':
    #Added nomatch test cases for Problem 2 and 3
    print("\nProblem 1:")
    testcase11 = '123.iamironman@avengers.com'
    print("Student answer: ",problem1(testcase11),"\tAnswer correct?", problem1(testcase11) == 'valid')

    testcase12 = '250.Srogers1776@avengers.com'
    print("Student answer: ",problem1(testcase12),"\tAnswer correct?", problem1(testcase12) == 'valid')

    testcase13 = '100.nickfury@sheild.gov'
    print("Student answer: ",problem1(testcase13),"\tAnswer correct?", problem1(testcase13) == 'valid')

    testcase14 = '144.venom@avengers.comasdf'
    print("Student answer: ",problem1(testcase14),"\tAnswer correct?", problem1(testcase14) == 'invalid')

    testcase15 = '942.hyperion@avengers.com'
    print("Student answer: ",problem1(testcase15),"\tAnswer correct?", problem1(testcase15) == 'invalid')

    testcase16 = '567.greengoblin@sheild.gov'
    print("Student answer: ",problem1(testcase16),"\tAnswer correct?", problem1(testcase16) == 'invalid')

    testcase17 = '324drdoom324@avengers.com'
    print("Student answer: ",problem1(testcase17),"\tAnswer correct?", problem1(testcase17) == 'invalid')

    testcase18 = '765.Hosborn*876@sheild.gov'
    print("Student answer: ",problem1(testcase18),"\tAnswer correct?", problem1(testcase18) == 'invalid')

    testcase19 = '234.vulture@sheild.com'
    print("Student answer: ",problem1(testcase19),"\tAnswer correct?", problem1(testcase19) == 'invalid')

    print("\nProblem 2:")
    testcase21 = "Captain America rides a Harley"
    print("Student answer: ",problem2(testcase21),"\tAnswer correct?", problem2(testcase21) == ("Captain America","Harley"))

    testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
    print("Student answer: ",problem2(testcase22),"\tAnswer correct?", problem2(testcase22) == ("Spider Man", "Harley"))

    testcase23 = "Groot rides a spaceship"
    print("Student answer: ", problem2(testcase23), "\tAnswer correct?", problem2(testcase23) == ("Groot", "spaceship"))

    testcase24 = "Starlord flies a Milano"
    print("Student answer: ",problem2(testcase24),"\tAnswer correct?", problem2(testcase24) == ("Starlord", "Milano"))

    testcase25 = "The Starlord flies many ships, but Rocket flies a Warbird Special much faster"
    print("Student answer: ",problem2(testcase25),"\tAnswer correct?", problem2(testcase25) == ("Rocket", "Warbird Special"))

    testcase26 = "Spider Man flies through the city"
    print("Student answer: ",problem2(testcase26),"\tAnswer correct?", problem2(testcase26) == ("nohero", "noname"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",problem3(testcase32),"\tAnswer correct?", problem3(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase31 = 'Spider Girl, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",problem3(testcase34),"\tAnswer correct?", problem3(testcase34) == "The Invisible Woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",problem3(testcase35),"\tAnswer correct?", problem3(testcase35) == "nomatch")