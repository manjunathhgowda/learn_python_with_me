# Write a Python Program to Find Factorial of Number Using Recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("ente thr number to find factorial:"))
print(f"factorial of {num} is : {fact(num)}")