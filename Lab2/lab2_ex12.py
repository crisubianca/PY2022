# Write a function that will receive a list of words  as parameter and
# will return a list of lists of words, grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.

# Example:
# group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
# will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
from itertools import groupby

def groupbyrhyme(list_rhyme):
    list_rhyme.sort(key=lambda i: i[len(i) - 2] + i[len(i) - 1], reverse=True)

    to_be_returned = []
    for key, value in groupby(list_rhyme, key= lambda i: i[len(i) - 2] + i[len(i) - 1]):
        to_be_returned.append(list(value))
    return to_be_returned

print(groupbyrhyme((['ana', 'banana', 'carte', 'arme', 'parte'])))