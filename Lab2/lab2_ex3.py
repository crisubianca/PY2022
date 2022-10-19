# Write a function that receives as parameters two lists a and b and returns:
# a intersected with b, a reunited with b, a - b, b - a

def Intersection(lst1, lst2):
    final_lst = [value for value in lst1 if value in lst2]
    print("The intersection of your lists is: ")
    return final_lst

def Union(lst1, lst2):
    final_lst = lst1+lst2 #if the two lists have the same number, it appears twice in the result
    print("The union of your lists is: ")
    return final_lst

def Difference(lst1, lst2):
    list = []
    for element in lst1:
        if element not in lst2:
            list.append(element)
    print("The difference between your lists is: ")
    return list


lst1 = []
a1 = int(input("Enter number of elements: "))
for i in range(0, a1):
    ele = int(input())
    lst1.append(ele)  # adding the element
print("Your list is: ")
print(lst1)

lst2 = []
a2 = int(input("Enter number of elements: "))
for i in range(0, a2):
    ele = int(input())
    lst2.append(ele)  # adding the element
print("Your list is: ")
print(lst2)

print(Intersection(lst1, lst2))
print(Union(lst1, lst2))
print(Difference(lst1, lst2))
print(Difference(lst2, lst1))