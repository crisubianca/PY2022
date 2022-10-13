# 2.Write a script that calculates how many vowels are in a string.

mystring = str(input("Please type a sentence: "))
vowels = "aeiouAEIOU"
print("The number of vowels in your string is:")
print(len([letter for letter in mystring if letter in vowels]))
print([letter for letter in mystring if letter in vowels])