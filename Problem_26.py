#  Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("-----Options-----")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
print("-----------------")
a=int(input("Enter the first operand:"))
b=int(input("Enter the second operand:"))
while(True):
    choice=int(input("Enter your Choice (1,2,3,4):"))
    if choice==1:
      print(f"{a} + {b} = {add(a,b)}")
    elif choice==2:
      print(f"{a} - {b} = {subtract(a,b)}")
    elif choice==3:
        print(f"{a} * {b} = {multiply(a,b)}")
    elif choice==4:
        if b==0:
            print(f"{a} can't be devisible by zero...")
        else:
            print(f"{a} / {b} = {divide(a,b)}")
    elif choice==5:
        print("Exiting.............")
        break
    else:
        print("Invalid choice..Try again")


       