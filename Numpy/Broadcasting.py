import numpy as np

"""
Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array's shape.

The dimensions have the same size.
OR
One of the dimensions has a size of 1.
"""


"""
arr1 = np.array([[1,2,3,4],[5,6,7,8])
arr2 = np.array([[1],[2],[3],[4]])

These two arrays are not goind to broadcast together bcoz 
of its dimensions.
"""
arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1],[2],[3],[4]])

print(arr1.shape)
print(arr2.shape)

print(np.dot(arr1,arr2))

print(arr1)
print(arr2)

print(arr1 * arr2)


# multiplication table
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1*array2)