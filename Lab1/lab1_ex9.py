#Write a functions that determine the most common letter in a string. For example if the string is
# "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

# "an apple is not a tomato" -> the most common is: "a"(4 times)
from collections import Counter

string = input("Write your string: ")

def commonLetter(text):
    max = 0
    letter = ""
    text = text.lower()
    for i in text:
        if "a" <= i <= "z":
                count = text.count(i)
                if count > max:
                    max = count
                    letter = i
    print("Common letter is '", letter, "'", "and appears of ", max ,'times!')

commonLetter(string)