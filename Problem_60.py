#  Write a Python program to find words which are greater than given length k.

def find_words(w,k):
    l_w=[]
    for word in w:
        if len(word)>k:
            l_w.append(word)
    return l_w

word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon fruit"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
