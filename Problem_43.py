#  Write a Python program to check if the given number is a Disarium Number.

#  A Disarium number is a number that is equal to the sum of its digits each raised to the
#  power of its respective position. For example, 89 is a Disarium number because 89=8^1+9^2

def is_disarium(num):
    num_str=str(num)
    result=0
    power=1
    for char in num_str:
        result+=int(char)**power
        power+=1
    return result==num
try:
    num = int(input("Enter a number: "))
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")