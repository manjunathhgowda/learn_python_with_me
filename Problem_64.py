#  Write a Python program to find uncommon words from two Strings.
def uncommon_words(s1,s2):
    w1=set(s1.split())
    w2=set(s2.split())
    un_words=w1.symmetric_difference(w2)
    return list(un_words)

string1 = "This is the first string" 
string2 = "This is the second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words:", uncommon)
