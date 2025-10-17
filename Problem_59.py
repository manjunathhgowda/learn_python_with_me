#  Write a Python program to Count occurrences of an element in a list.

lst=[30, 10, 45, 5, 10, 20, 10, 100, 30,10]
dict={}
value=1
for key in lst:
    if key not in dict:
        dict[key]=value
    else:
        count=dict.get(key)
        dict[key]=count+1
        
print(dict)
for key in dict:
    print(f"{key} found {dict.get(key)} times in list")



