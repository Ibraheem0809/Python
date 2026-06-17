import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [2,0],
    [1,5]
])
print("A:")
print(A)
print("B:")
print(B)

# Matrix Addition
print("Matrix Addition:")
print(A+B)

# Matrix Subtraction
print("Matrix Subtraction:")
print(B-A)

# Matrix Multiplication (Element-wise)
print("Matrix Multiplication (Element-wise):")
print(A*B)

# Dot Product Of Matrix
print("Dot Product:")
print(np.dot(A,B))