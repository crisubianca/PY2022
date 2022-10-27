
def p1(l1, l2):
    # p1: Write a function that receives as parameters two lists a and b and
    # returns a list of sets containing:
    # (a intersected with b, a reunited with b, a - b, b - a)
    l1_intersected_l2 = set(elem for elem in l1 if elem in l2)
    l1_reunited_l2 = set(l1 + l2)
    l1_minus_l2 = set(elem for elem in l1 if elem not in l2)
    l2_minus_l1 = set(elem for elem in l2 if elem not in l1)

    return l1_intersected_l2, l1_reunited_l2, l1_minus_l2, l2_minus_l1

def p2(string):
    # p2: Write a function that receives a string as a parameter and returns
    # a dictionary in which the keys are the characters in the character string
    # and the values are the number of occurrences of that character in the given text.
    # Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
    # {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
    return {i: string.count(i) for i in set(string)}
    # sau - mai ineficient
    # return {ch: string.count(ch) for ch in string}

def p3(dict1, dict2):
    # p3: Compare two dictionaries without using the operator "==" returning True or False.
    # (Attention, dictionaries must be recursively covered because they can contain other containers,
    # such as dictionaries, lists, sets, etc.)
    for item1, item2 in dict1, dict2:
        if type(item1) != type(item2):
            return False
        if type(item1) == type(item2) and item1 is dict or item1 is list or item1 is set:
            return p3(item1, item2)
        if item1 != item2:
            return False
    return True

def p4(tag, content, **parameters):
    # p4: The build_xml_element function receives the following parameters:
    # tag, content, and key-value elements given as name-parameters.
    # Build and return a string that represents the corresponding XML element.
    # Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
    # returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

    return "<" + tag + " " + r" ".join([p[0] + " = \"" + p[1] + "\"" if type(p[1]) == str else p[0] + " = " + str(p[1])
                                        for p in parameters.items()]) + ">" + content + "</" + tag + ">"

def p5(rules, dictionary):
    # p5: The validate_dict function that receives as a parameter a set of tuples
    # ( that represents validation rules for a dictionary that has strings as keys and values)
    # and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
    # A value is considered valid if it starts with "prefix", "middle" is inside the value
    # (not at the beginning or end) and ends with "suffix".
    # The function will return True if the given dictionary matches all the rules,
    # False otherwise.
    #
    # Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    # and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    # => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

    rules_dict = {rule[0]: [rule[1], rule[2], rule[3]] for rule in rules}
    return all([key in rules and value.startswith(rules_dict[key][1]) and
                rules_dict[key][2] in value and value.endswith(rules_dict[key][3])
                for key, value in dictionary.items()])

def p6(a_list: []):
    #p6: Write a function that receives as a parameter a list and returns
    # a tuple (a, b), representing the number of unique elements in the list,
    # and b representing the number of duplicate elements in the list
    # (use sets to achieve this objective).
    duplicates = set()
    uniques = set()

    set_from_list = set(a_list)
    for item in set_from_list:
        a_list.remove(item)
    duplicates = set(a_list)
    uniques = set(item for item in set_from_list if item not in duplicates)
    return len(uniques), len(duplicates)

def p7(*sets):
    #p7: Write a function that receives a variable number of sets
    # and returns a dictionary with the following operations from all sets two by two:
    # reunion, intersection, a-b, b-a.
    # The key will have the following form:
    # "a op b", where a and b are two sets,
    # and op is the applied operator: |, &, -.

    # Ex: {1,2}, {2, 3} =>
    #
    # {
    #
    #     "{1, 2} | {2, 3}":  {1, 2, 3},
    #
    #     "{1, 2} & {2, 3}":  { 2 },
    #
    #     "{1, 2} - {2, 3}":  { 1 },
    #
    #     ...
    #
    # }

    result = {}
    for idx1 in range(0, len(sets) - 1):
        for idx2 in range(idx1 + 1, len(sets)):
            result.update({(str(sets[idx1]) + " | " + str(sets[idx2])): (sets[idx1] | sets[idx2]),
                           (str(sets[idx1]) + " & " + str(sets[idx2])): (sets[idx1] & sets[idx2]),
                           (str(sets[idx1]) + " - " + str(sets[idx2])): (sets[idx1] - sets[idx2]),
                           (str(sets[idx2]) + " - " + str(sets[idx1])): (sets[idx2] - sets[idx1])})
    return result

def p8(mapping):
    #p8: Write a function that receives a single dict parameter named mapping.
    # This dictionary always contains a string key "start".
    # Starting with the value of this key you must obtain a list of objects
    # by iterating over mapping in the following way:
    # the value of the current key is the key for the next value, until you find a loop
    # (a key that was visited before).
    # The function must return the list of objects obtained as previously described.

    # Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    # will return ['a', '6', 'z', '2']
    to_return = list()
    value = mapping['start']
    while value not in to_return:
        to_return.append(value)
        value = mapping[value]
    return to_return

def p9(*arguments, **keywords):
    #p9: Write a function that receives a variable number of positional arguments
    # and a variable number of keyword arguments adn
    # will return the number of positional arguments
    # whose values can be found among keyword arguments values.

    # Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    # will return 3
    return len([el for el in arguments if el in keywords.values()])

def main():
    #p1:
    l1 = [1,2,3]
    l2 = [3,4,5]
    print("## RESULT P1 ##\n", p1(l1,l2))

    #p2:
    print("## RESULT P2 ##\n", p2("I love coffee!:)"))

    #p3:
    dict1 = {'Name': 'Ion', 'Age': {'check': [0,0]}}
    dict2 = {'Name': 'Ion', 'Age': {'check': [0,0]}}
    print("## RESULT P3 ##\n", p3(dict1, dict2))
    print("\nHEADS UP! Nu merge bine! :(\n")

    #p4:
    print("## RESULT P4 ##\n", p4("a", "Hello There", href=" http://python.org ", _class=" my-link ", id=" someid"))

    #p5:
    s = {("key1", "", "inside", "out"), ("key2", "start", "middle", "winter")}
    d = {
        "key1": "come,inside it's too cold out", "key3": "this is not valid"}
    print("## RESULT P5 ##\n", p5(s, d))

    #p6:
    a_list = [1, 2, 2, 3]
    print("## RESULT P6 ##\n", p6(a_list))

    #p7:
    print("## RESULT P7 ##\n", p7({1, 2}, {2, 3}))

    #p8:
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print("## RESULT P8 ##\n", p8(mapping))

    #p9:
    print("## RESULT P9 ##\n", p9(1, 2, 3, 4, x=1, y=2, z=3, w=5))

if __name__ == "__main__":
    main()
