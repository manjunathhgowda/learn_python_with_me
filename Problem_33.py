#  Write a Python Program to find largest element in an array.
arr=[4,2,44,1,56,32]
largest=arr[0]

for ele in arr:
    if ele>=largest:
        largest=ele
    
print("largest element in an array :",largest)

# using max() for maximum and min() for minimum
print("Max:",max(arr))
print("Min:",min(arr))
