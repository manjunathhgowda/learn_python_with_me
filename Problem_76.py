# Frequency of charecter in string
from collections import Counter
word="acharyatech"
print(Counter(word))
#or
freq={}
for ch in word:
    freq[ch]=freq.get(ch,0)+1

for key,value in freq.items():
    print(key,":",value)


