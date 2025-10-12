# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

print("Prime number s between 1 and 10 are:")
for i in range(1,11):
    if i==1 or i==2:
        print(i)
    else:
        for j in range(2,i):
            if (i%j==0):
                break
            else:
                print(i)
                break