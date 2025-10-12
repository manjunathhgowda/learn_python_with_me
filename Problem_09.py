#  Write a Python program to solve quadratic equation.

# The standard form of a quadratic equation is: 
#               ax^2+bx+c
#  where
#  a, b and c are real numbers and 𝑎 ≠ 0
#  The solutions of this quadratic equation is given by:
# -b (+ or -) sqrt(b^2-4ac)/2a

import math

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

discriminant=b**2-4*a*c

if discriminant>0:
    #two real and distinct roots
    root1=(-b+ math.sqrt(discriminant)/2*a)
    root2=(-b- math.sqrt(discriminant)/2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root1}")
elif discriminant==0:
    #one real root
    root= -b/(2*a)
    print(f"Root: {root}")
else:
    #two complex roots
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(abs(discriminant))/(2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
