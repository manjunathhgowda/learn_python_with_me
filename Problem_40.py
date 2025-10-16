#  Write a Python Program to Sort Words in Alphabetic Order.

text=input("Enter a string:")
words=text.split()
# If you want the sorting to ignore case (treat “Apple” and “apple” the same), use: key=str.lower
words.sort(key=str.lower)  
for word in words:
    print(word,end=" ") 