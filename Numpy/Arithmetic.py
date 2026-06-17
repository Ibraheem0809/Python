import numpy as np

# Scalar Arithmetic
arr = np.array([1,2,3])

print(arr+1)
print(arr-2)
print(arr*3)
print(arr/4)
print(arr ** 5)

# Vectorized Math func

array = np.array([1.21,2.56,3.43])

print("Square Root: ",np.sqrt(array))
print("Round off: ", np.round(array))


# it also contains some constant value
print("pi: ",np.pi)


# Exercise
radii = np.array([1,2,3])
# pi*r*r
print(np.pi * radii ** 2)


# Element wise arithmetic
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("Sum:",arr1+arr2)
print("Diff:",arr2-arr1)
print("Pro:",arr1*arr2)
print("Div:",arr1/arr2)
print("Floor div:",arr1//arr2)
print("Exp:",arr1**arr2)
print("Rem:",arr1%arr2)


# Comparision Operator

scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores >= 75)
print(scores <= 75)

scores[scores < 60] = 0
print(scores)


