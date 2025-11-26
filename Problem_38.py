#  Write a Python Program to Multiply Two Matrices.

def multiply_matrices(m1,m2):
    rows_m1=len(m1)
    cols_m1=len(m1[0])
    rows_m2=len(m2)
    cols_m2=len(m2[0])

    if cols_m1 != rows_m2:
        print("multiplication not posible")
    else:
        result=[[0 for _ in range(cols_m2)] for _ in range(rows_m1)]
        
        for i in range(rows_m1):
            for j in range(cols_m2):
                for k in range(cols_m1):
                    result[i][j]+=m1[i][k]*m2[k][j]
        return result
  
matrix1=[
    [11,12],
    [14,15],
    [8,9]
]

matrix2=[
    [1,2,3],
    [4,5,6]
]
result_matrix = multiply_matrices(matrix1, matrix2)
print("Matrix 1 is:")
for row in matrix1:
    print(row)
print("Matrix 2 is:")
for row in matrix2:
    print(row)
print("Resultant Matrix is:")
for row in result_matrix:
    print(row)
