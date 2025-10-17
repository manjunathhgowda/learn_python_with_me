# Write an python program to Check if a Number is a Palindrome

num = int(input("Enter a number: "))
rev = int(str(num)[::-1])
if num == rev:
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is NOT a Palindrome Number")