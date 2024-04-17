import array as ar
import numpy as np



#write a python program to compute the matrix addition and transpose using iterative struture using numpy array
matrix1 = np.array([[1,3,5],[5,2,6]])
matrix2 = np.array([[4,1,5],[78,3,6]])
result = np.zeros(matrix1.shape)

print(result)

def matrix_trans(matrix1):
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i][j]=matrix1[j][i]

    return matrix1
print(matrix1)
print(matrix_trans(matrix1))
