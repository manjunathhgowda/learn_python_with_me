#  Write a Python program to print all happy numbers between 1 and 100.

def getNextNum(num):
    nxtNum = 0
    while num > 0:
        rem = num % 10
        nxtNum += rem ** 2
        num //= 10
    return nxtNum

def isHappy(num, seen=set()):
    if num == 1:
        return True
    if num in seen:  # cycle detected → not happy
        return False
    seen.add(num)
    nxt = getNextNum(num)
    return isHappy(nxt, seen)  # return the recursive result
print("Happy numbers between 1 and 100 are:")
for n in range(1,101):
    res = isHappy(n)
    if res:
        print(n,end="|")


