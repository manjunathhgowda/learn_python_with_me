#  Write a Python program to find all duplicate characters in string.

def charCount(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    duplicates=[key for key,value in dict.items() if value>1]
    return duplicates

str1="Good Morning Everyone"
dup=charCount(str1)
print(dup)
