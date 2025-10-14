#  Write a Python Program to Find HCF.
#  Highest Common Factor(HCF):
#  HCF, or Highest Common Factor, is the largest positive integer that divides two or more
#  numbers without leaving a remainder.

def compute_hcf(x,y):
    if x>y:
        upper=x
    else:
        upper=y
    for i in range(1,upper+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print(f"L.C.M of {a} and {b} is: {compute_hcf(a,b)}")