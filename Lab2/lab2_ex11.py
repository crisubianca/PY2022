# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element
# in the tuple.

# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def orderbythird(list):
    try:
        list.sort(key=lambda i: i[1][2])
    except:
        return "A tuple does not have a 2nd element or an element doesn't have 3 characters"

    return list

print(orderbythird([('abc', 'bcd'), ('abc', 'zza')]))