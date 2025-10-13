#  Write a Python Program to Find Armstrong Number in an Interval.

lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower,upper):
    num_digits = len(str(num))
    sum = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** num_digits
        temp_num //= 10        
    if sum == num:
        print(num)
