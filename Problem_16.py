# Write a Python Program to Find the Factorial of a Number
num=int(input("enter the number find Factorial :"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"Factorial of number {num} is :{fact}")