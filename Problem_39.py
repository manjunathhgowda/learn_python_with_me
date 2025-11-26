#  Write a Python Program to Transpose a Matrix.
def transpseMatrix(m):
    rows=len(m)
    cols=len(m[0])
    tm=[[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            tm[j][i]=m[i][j]
    return tm
matrix=[ 
    [1,2,6],
    [3,4,4]
]
print("Original Matrix:")
for row in matrix:
    print(row)
print("Transpose Matrix:")
transpose=transpseMatrix(matrix)
for row in transpose:
    print(row)

