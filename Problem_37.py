#  Write a Python Program to Add Two Matrices.

def add_matrices(m1,m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        print("Matrices must have the same dimensions for addition")
    else:
        result=[]
        for i in range(len(m1)):
            row=[]
            for j in range(len(m1[0])):
                row.append(m1[i][j]+m2[i][j])
            result.append(row)
        return result
  
matrix1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2=[
    [11,12,13],
    [14,15,14],
    [17,18,19]
]
result_matrix = add_matrices(matrix1, matrix2)
print("Matrix 1 is:")
for row in matrix1:
    print(row)
print("Matrix 2 is:")
for row in matrix2:
    print(row)
print("Resultant Matrix is:")
for row in result_matrix:
    print(row)
