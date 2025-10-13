# Write a Python Program to Print the Fibonacci sequence.

terms=int(input("Enter a terms to find the fibonacci sequence:"))

n1,n2=0,1
count=0
if terms<=0:
    print("Enter valid term")
elif terms==1:
    print(f"Fibonacci sequence upto {terms} is : {n1}")
else:
    print("Fibonacci sequence are:")
    while count<terms:
        print(n1,end=" ")
        last=n1+n2
        n1=n2
        n2=last
        count+=1
    



    
