#  Write a Python Program to find sum of array.

arr=[1,2,3,4,5]

total=0
for i in arr:
    total+=i
print(f"Sum of array {arr} is: {total}")
# Using sum()
print(f"Sum of array {arr} is: {sum(arr)}")
