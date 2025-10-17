#  Write a Python program to Cloning or Copying a list.

lst=[30, 10, 45, 5, 20, 98, 100, 34]
copied_lst=lst.copy()
print(copied_lst)

#or
copied_lst1=lst[:]
print(copied_lst1)

#or
copied_lst2=list(lst)
print(copied_lst1)

#or
copied_lst3=[i for i in lst]
print(copied_lst1)

