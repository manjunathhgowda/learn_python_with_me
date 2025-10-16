#  Write a Python Program for cube sum of first n natural numbers?

def cubeSum(num):
    return sum([i**3 for i in range(1, num + 1)])

    # total=0
    # for i in range(1,num+1):
    #     total+=i**3
    # return total
    
n=int(input("Enter value of n:"))
print(f"cube sum of first {n} natural number is: {cubeSum(n)}")

