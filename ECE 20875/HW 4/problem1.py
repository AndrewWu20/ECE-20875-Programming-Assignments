def add_map(fun, L):
    """
    Returns a new list R where each element in R is fun(i) + 1 for the
    corresponding element i in L
    :param fun: function
    :param L: list
    :return R: list
    """
    # Fill in
    return(list(map(lambda x: fun(x) + 1, L)))  #Values are mapped into fun and adds one, then returns values

def compose_map(fun1, fun2, L):
    """
    Returns a new list R where each element in R is fun2(fun1(i)) for the
    corresponding element i in L
    :param fun1: function
    :param fun2: function
    :param L: list
    :return R: list
    """
    # Fill in
    return(list(map(lambda x: fun2(fun1(x)), L)))   #Returns a Mapped list that goes through fun1 and fun2

def compose(fun1, fun2):
    # Fill in
    """
    Returns a new function ret_fun. ret_fun should take a single input i, and return
    fun1(fun2(i))
    :param fun1: function
    :param fun2: function
    :return ret_fun: function
    """
    def ret_fun(i):
        # Fill in
        return(fun1(fun2(i)))   #Returns i of fun2 in fun1

    return ret_fun

def repeater(fun, num_repeats):
    """
    Returns a new function ret_fun. ret_fun should take a single input i, and return
    fun applied to i num_repeats times. In other words, if num_repeats is 1, ret_fun
    should return fun(i). If num_repeats is 2, ret_fun should return fun(fun(i)). If
    num_repeats is 0, ret_fun should return i.
    :param fun: function
    :param num_repeats: int
    :return ret_fun: function
    """
    def ret_fun(x):
        # Fill in
        if num_repeats == 0:    #If num_repeats is zero, don't repeat and return
            return x
        else:                   #Loop through fun until num_repeats is zero
            for i in range(num_repeats):
                x = fun(x)
            return x

    return ret_fun

if __name__ == '__main__':

    def test1(x):
        return x * 2

    def test2(x):
        return x - 3

    data = [1, 3, 5, 7, -9, -9, 11, 13, 15, 17, 19]

    # Testing the add_map function
    print(add_map(test1, data)) # Calling the add_map function with function test1 and the list data as the argument

    # Testing the compose_map function
    print(compose_map(test1, test2, data)) # Calling the compose_map function with functions test1, test2 and the list data as the argument

    print(compose_map(test2, test1, data)) # Calling the compose_map function with functions test2, test1 and the list data as the argument (order of function input changed)

    # Using the compose function with functions test1 and test2 as arguments and returning its value to f1
    f1 = compose(test1, test2)

    # Running f1 with i=4
    print(f1(4))

    # Applying f1 on to each value in the list data
    print(list(map(f1, data)))

    # Using the compose function with functions test2 and test1 as arguments and returning its value to f2
    f2 = compose(test2, test1)

    # Running f2 with i=4
    print(f2(4))

    # Applying f2 on to each value in the list data
    print(list(map(f2, data)))

    # Testing the repeater function that with the function test1 with different num_repeats argument.
    z = repeater(test1, 0)
    once = repeater(test1, 1)
    twice = repeater(test1, 2)
    thrice = repeater(test1, 3)

    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))
