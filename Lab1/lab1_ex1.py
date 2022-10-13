# 1.Find The greatest common divisor of multiple numbers read
# from the console.

print("How many numbers?")
how_many = int(input())
print("Give me %(numbers)d numbers:" % {"numbers": how_many})
n1 = int(input())
gcd = n1
for i in range(1, how_many):
    n2 = int(input())
    while n2 != gcd:
        if n2 > gcd:
            n2 = n2 - gcd
        else:
            gcd -= n2
print("Greatest common div for your numbers is:")
print(gcd)


