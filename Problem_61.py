# Write a Python program for removing ith character from a string.

def remove_char(s,i):
    if i < 0 or i >= len(s):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    return s[:i]+s[i+1:]

input_str = "Hello, wWorld!"
i =int(input("Enter index:")) 
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")