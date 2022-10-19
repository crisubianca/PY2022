# Write a function that receives a number x, default value equal to 1, a list of strings,
# and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x
# if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.

#  Example:
#  x = 2, ["test", "hello", "lab002"], flag = False
#  will return (["e", "s"], ["e" .
#  Note: The function must return list of lists.

def asciidivisiblebyx(x, list_of_strings, flag):
    to_be_returned = []
    for item in list_of_strings:
        to_be_returned_insance = []
        for letter in item:
            if (ord(letter) % x == 0) is flag:
                to_be_returned_insance.append(letter)
        to_be_returned.append(to_be_returned_insance)

    return to_be_returned

print(asciidivisiblebyx(2, ["test", "hello", "lab002"], False))