#  Write a Python program to determine whether the given number is a Harshad Number
'''A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
 In other words, 
 a number is considered a Harshad number if it can be evenly divided 
 by the sum of its own digits.
 For example:
 18 is a Harshad number because 1 + 8 = 9 and 18 is divisible by 9
 44 is not a Harshad number because 4 + 4 = 8 and 44 is not divisible by 8.'''

def checkHarshad(num):
    temp_num=num
    sum=0
    while 0<temp_num:
        digit=temp_num%10
        sum+=digit
        temp_num//=10
    return num%sum==0

    # digit_sum = sum(int(i) for i in str(num))
    # return num % digit_sum == 0
    
n=int(input("Enter an number:"))
if checkHarshad(n):
    print(f"Yes..! {n} is Harshad Number")
else:
    print(f"No..! {n} is Not a Harshad Number")