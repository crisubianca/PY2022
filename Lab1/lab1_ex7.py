#Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.

# "An apple is 123 USD" -> 123
# "abc123abc" -> 123

text = input("Write your text: ")
print("Numbers from your text are: ")
for i in text:
    if(i.isdigit()):
        print(i,end="")

# ANOTHER METHOD COULD BE USING re : The regular expressions can also be used to perform this particular task.
# We can define the digit type requirement, using “\D”, and only digits are extracted from the string. -> see geeks for geeks