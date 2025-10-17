#  Write a Python program to find second largest number in a list.

#using remove() and max()
lst1=[23,63,73,22,63,66,13,645]
lst1.remove(max(lst1))
print("The Second largest number in the list is:",max(lst1))

#using sort() and 2nd index
lst2 = [23,63,73,22,63,66,13,645]
lst2.sort(reverse=True)
if len(lst2) >= 2:
    second_largest = lst2[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")

