#  Write a Python program to check if the given number is Happy Number.

'''
 Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
 the number by the sum of the squares of its digits and continue the process, eventually
 reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
 is not a Happy Number.
  For example:
 19 is a Happy Number because:
 1^2 + 9^2 = 82
 8^2 + 2^2 = 68
 6^2 + 8^2 = 100
 1^2 + 0^2 + 0^2 =1
 The process reaches 1, so 19 is a Happy Number.
'''

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

n = int(input("Enter a number: "))
res = isHappy(n)
if res:
    print(f"Yes!.. {n} is a Happy Number")
else:
    print(f"No!.. {n} is Not a Happy Number")

