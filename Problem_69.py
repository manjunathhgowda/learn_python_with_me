#  Write a Python program to Merging two Dictionaries.

 # 1. Using the update() method:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("1.Merged Dictionary:",dict1)

# 2. Using dictionary unpacking
merged_dict = {**dict1, **dict2}
print("2.Merged Dictionary:", merged_dict)