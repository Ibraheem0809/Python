"""
1. Creates a NumPy array:
   [10, 20, 30, 40, 50]

2. Prints:
   - First element
   - Last element
   - First 3 elements
   - Array multiplied by 2
   - Shape of the array

3. Create a 2D array:

   [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
   ]

4. Print:
   - First row
   - Second column
   - Shape
"""

import numpy as np

arr = np.array([10,20,30,40,50])

print("First Element: ",arr[0])
print("Last Element: ",arr[-1])
print("First 3 Elements: ",arr[0:3])
print("Array * 2 : ",arr*2)
print("Shape:",arr.shape)

arr2D = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("First Row: ",arr2D[0])
print("Secont Col: ",arr2D[:,1])
print("Shape: ",arr2D.shape)