#  Write a Python program to find N largest elements from a list.
def nList(lst,N):
    if len(lst)<N:
        print("Not sufficient elements in the list")
    else:
        lst.sort(reverse=True)
        return lst[:N]

lst=[30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N=int(input("Enter value of N:"))
print(f"{N} largest elements from a list are : {nList(lst,N)}")
