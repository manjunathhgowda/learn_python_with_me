# Write a Python Program to Check Armstrong Number?

'''It is a number that is equal to the sum of its own digits,
each raised to a power equal to the number of digits in the number.'''

# example : 153 , 9474

# num=input("Enter number to check armstrong:")
# l=len(num)
# sum=0
# for i in num:
#     i=int(i)
#     sum+=i**l
# if num==str(sum):
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number")


num = int(input("Enter a number: "))
num_digits = len(str(num))

sum = 0
temp_num = num
while temp_num > 0:
    digit = temp_num % 10
    sum += digit ** num_digits
    temp_num //= 10

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

