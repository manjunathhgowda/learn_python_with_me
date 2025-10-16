#  Write a Python program to print all disarium numbers between 1 to 100.

def is_disarium(num):
    num_str=str(num)
    result=0
    power=1
    for char in num_str:
        result+=int(char)**power
        power+=1
    return result==num

for n in range(1,101):
    if is_disarium(n):
        print(n,end=" | ")