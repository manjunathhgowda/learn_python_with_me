#  Write a Python Program to Find LCM.
#  LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
#  more numbers.

def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print(f"L.C.M of {a} and {b} is: {compute_lcm(a,b)}")

