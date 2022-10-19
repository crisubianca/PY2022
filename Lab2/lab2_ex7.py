# Write a function that receives as parameter a list of numbers (integers)
# and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and
# the second element will be the greatest palindrome number.

def palindromelist(lst_of_numbers):

    list_of_palindroms = [el for el in lst_of_numbers if str(el) == str(el)[::-1]]
    return tuple((len(list_of_palindroms), max(list_of_palindroms)))

print(palindromelist([12321, 23432, 123, 4567654]))