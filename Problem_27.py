#  Write a Python Program to Display Fibonacci Sequence Using Recursion.

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
terms=int(input("Enter the no.of term:"))
if terms<0:
    print("Enter valid term")
else:
    print("Fibonacci series are:")
    for i in range(terms):
         print(fibo(i))