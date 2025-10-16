#  Write a Python Program to Remove Punctuation From a String.

punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
mystr=input("enter your string:")
no_punct = ""
for char in mystr:
    if char not in punctuations:
        no_punct+=char
print("Refined str:",no_punct)

