#  Write a Python Program to Check Prime Number

num=int(input("enter number to check prime or not:"))
if num==1:
    print(f"{num} is not prime number")
elif num>1:
    for i in range(2,num+1):
        if num%i==0:
            print(f"{num} is not prime number")
            break
        else:
            print(f"{num} is prime number")
            break