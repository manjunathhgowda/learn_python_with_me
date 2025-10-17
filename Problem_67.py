#  Write a Python program to Extract Unique dictionary values.

my_dict = {'a': 10,'b': 20,'c': 10,'d': 30,'e': 20}
unique_values_list=list(set(my_dict.values()))
print("Unique values in the dictionary:", unique_values_list)