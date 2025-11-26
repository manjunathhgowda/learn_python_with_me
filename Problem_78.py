# move pos number to end of list and nagative to the left

arr=[-7,3,-3,-4,1,6]
j=0
for i in range(len(arr)):
    if arr[i]<0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)