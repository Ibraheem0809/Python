import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print(arr)

# slicing -> array[start:end:step]

# Rows
print(arr[0])
print(arr[:3])
print(arr[::2])
print(arr[::-1]) # reverse

# Cols 
print(arr[:,2])
print(arr[:, 0:3])
print(arr[:, 1:4])
print(arr[0:2, 1:3])