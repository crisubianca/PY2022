# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

import math
from math import sqrt

lst = []
a = int(input("Enter number of elements: "))
for i in range(0, a):
    ele = int(input())
    lst.append(ele)  # adding the element
print("Your list is: ")
print(lst)

flag_primes = False
primes = []


def isPrime(n):
    # Corner case
    if (n <= 1):
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True

for num in lst:
    if isPrime(num):
        flag_primes = True
        primes.append(num)

if flag_primes:
    print("The list contains the following primes:", primes)
else:
    print("No primes found in list!")