#  Write a Python program to Count occurrences of an element in a list.

lst=[30, 10, 45, 5, 10, 20, 10, 100, 30,10]
dict={}
for key in lst:
    dict[key]=dict.get(key,0)+1 
for key,value in dict.items():
    print(f"{key} found {value} times in list")



