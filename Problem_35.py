#  Write a Python Program to Split the array and add the first part to the end?

arr=[1,2,3,4,5,6,7]
d=int(input("Enter split point:"))
if d<0 or d>len(arr):
    print("Invalid split point")
else:
    print("Before split:",arr)
    print("After split:",arr[d:]+arr[:d])
