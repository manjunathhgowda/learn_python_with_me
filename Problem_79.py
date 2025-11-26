# majority of element in list (> n/2 times)
arr=[2,3,2]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
    if freq[i]> len(arr)//2:
        print(i)