#maximum sub array -kadane's algorithm

def max_subarray_sum(n):
    c=m=n[0]
    for i in n:
        c=max(i,c+i)
        m=max(m,c)
    return m
x=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(x))