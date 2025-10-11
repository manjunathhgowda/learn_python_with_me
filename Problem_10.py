#  Write a Python program to swap two variables without temp variable

a=input("Enter variable 1:")
b=input("enter variable 2:")
print(f"Before swap: Value of variable 1 & 2 are : {a},{b} ")
a,b=b,a
print(f"After swap: Value of variable 1 & 2 are : {a},{b} ")