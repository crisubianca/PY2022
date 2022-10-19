# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

# Example:
# For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2
# lists [1,2,3 ]
# 1 is in list 1 and 4,
# 2 is in list 1 and 2,
# 3 is in lists 1 and 2.

from collections import defaultdict

def exactlyxtimes(lists, x):
    dict = defaultdict(int)
    for list in lists:
        for item in list:
            dict[item] += 1
    return set(goodItem for goodItem in dict if dict[goodItem] == 2)

print(exactlyxtimes( [ [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"] ] , [2] ) )