#Write a function that counts how many bits with value 1 a number has. For example for number 24,
# the binary format is 00011000, meaning 2 bits with value "1"

# loop through all bits in an integer, check if a bit is set and if it is then increment the set bit count
print("Enter a number: ")
number = int(input())
def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

#i = 24
print("The number of bits with value 1 for your number are: ")
print(countSetBits(number))