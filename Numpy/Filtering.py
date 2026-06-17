import numpy as np

"""
Filtering - In NumPy, filtering means selecting elements from an array that satisfy a condition.
This is usually done with Boolean indexing.
"""

ages = np.array([[21,17,19,20,16,30,18,65],
                [39,22,15,99,18,19,20,21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]

even = ages[ages % 2 == 0]
odd = ages[ages % 2 != 0]

print(len(teenagers), teenagers)
print(len(adults) ,adults)
print(len(seniors) ,seniors)

print(even)
print(odd) 


# while filtering if we want to have a same shape then 
# there is a different function

teen = np.where(ages < 18, ages, 0)

print(teen)