# 4.Write a script that converts a string of characters written
# in UpperCamelCase into lowercase_with_underscores.

mystring = str(input("Please type your sentence in UpperCamelCase: "))
def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')
print("Your converted sentence is: ")
print(camel_to_snake(mystring))