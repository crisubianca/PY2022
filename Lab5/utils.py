#a) Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x.
# When run, the module will request an input from the user,
# convert it to a number and it will display the output of the process_item function.

def process_item(x):
    x += 1
    while any([x % el == 0 for el in range(2, int(x**(1/2)) + 1)]):
        x += 1
    return x


def main():

    x = int(input("Enter a number:"))
    print(process_item(x))

if __name__ == '__main__':
    main()
