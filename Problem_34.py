#  Write a Python Program for array rotation.

def rotated_array(arr,d):
    l=len(arr)
    if d<0 or d>=l:
        print("Invalid rotation value")
    else:
        rotated_array=[0]*l
        for i in range(l):
            rotated_array[i]=arr[(i+d)%l]
        return rotated_array
    
arr=[1,2,3,4,5,6]
rotation_value=int(input("Enter rotation value:"))
print("Original array:",arr)
print("Rotated array:",rotated_array(arr,rotation_value))

