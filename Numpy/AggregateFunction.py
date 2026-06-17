import numpy as np 

"""
In NumPy, aggregate functions (also called reduction
functions) summarize the elements of an array and
return a single value or a reduced array.
"""

arr = np.array([[1,2,3,4],[5,6,7,8]])

print("Minimum:",np.min(arr))
print("Index of Minimum:",np.argmin(arr))
print("Maximum:",np.max(arr))
print("Index of Maximum:",np.argmax(arr))
print("Sum:",np.sum(arr))
print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Variance:",np.var(arr))
print("Standard Deviation:",np.std(arr))

# Sum of all columns
print("Sum of cols:",np.sum(arr, axis=0))

# Sum of all rows
print("Sum of rows:",np.sum(arr, axis=1))
