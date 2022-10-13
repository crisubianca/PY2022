# 6. Write a function that validates if a number is a palindrome.

#121 -> Yes, it's a palindrome!:)
#211 ->No, it's not a palindrome!:(

num = input("Enter a number: ")
if num == num[::-1]:
    print("Yes, it's a palindrome!:)")
else:
    print("No, it's not a palindrome!:(")

