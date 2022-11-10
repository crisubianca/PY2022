def function2(*args, **kwargs):
    #2) Create a function and an anonymous function that receive a variable number of arguments.
    # Both will return the sum of the values of the keyword arguments.
    # Example:
    #
    # For the call my_function(1, 2, c=3, d=4) the returned value will be 7.

    sum = 0

    for kw in kwargs.keys():
        sum += int(kwargs[kw])

    return sum

anom_function = lambda *args, **kwargs: sum([val for val in kwargs.values()])

def function3(string):
    #3) Using functions, anonymous functions, list comprehensions and filter,
    # implement three methods to generate a list with all the vowels in a given string.
    # For the string "Programming in Python is fun"
    # the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

    #first list
    def function3_with_f(string):

        return [ch for ch in string if ch.lower() in "aeiou"]
    #second list
    anon_function = lambda string: [ch for ch in string if ch.lower() in "aeiou"]

    first_list = function3_with_f(string)

    second_list = anon_function(string)

    #third list
    f_filter = lambda string: list(filter(lambda x: x.lower() in "aeiou", string))

    third_list = f_filter(string)

    return first_list, second_list, third_list

def function4(*args, **kwargs):
    #4) Write a function that receives a variable number of arguments and keyword arguments.
    # The function returns a list containing only the arguments which are dictionaries,
    # containing minimum 2 keys and at least one string key with minimum 3 characters.
    # Example:
    #
    # my_function(
    #
    #  {1: 2, 3: 4, 5: 6},
    #
    #  {'a': 5, 'b': 7, 'c': 'e'},
    #
    #  {2: 3},
    #
    #  [1, 2, 3],
    #
    #  {'abc': 4, 'def': 5},
    #
    #  3764,
    #
    #  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    #
    #  test={1: 1, 'test': True}
    #
    # ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]

    return_list = []

    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                             for key in arg.keys()]):
                return_list.append(arg)

    for kw in kwargs.keys():
        if type(kwargs[kw]) == dict:
            if len(kwargs[kw].keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                             for key in kwargs[kw].keys()]):
                return_list.append(kwargs[kw])

    return return_list

def function5(lst):
    #5) Write a function with one parameter which represents a list.
    # The function will return a new list containing all the numbers found in the given list.
    # Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])
    # will return [1, 5, 6, 3.0]

    new_lst = []
    for el in lst:
        if type(el) in [int, float, complex]:
            new_lst.append(el)
    return new_lst




if __name__ == '__main__':
    print("EX 2")
    print(function2(1, 2, c=3, d=4))
    print("\nEX 2 - anom_function")
    print(anom_function(1, 2, c=3, d=4))
    print("\nEX 3")
    print(function3("Programming in Python is fun"))
    print("\nEX 4")
    print(function4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5},
                    3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    print("\nEX 5")
    print(function5([1  , "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


