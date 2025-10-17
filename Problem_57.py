# Write a Python program to Remove empty List from List.

lst= [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

new_lst=[]
for i in lst:
    if len(i)!=0:
        new_lst.append(i)
print(new_lst)

# or in short
lst1=[[1, 2, 3], [], [4, 5], [],[2], [],[1,4,2], [6, 7, 8], []]
print([i for i in lst1 if i])



