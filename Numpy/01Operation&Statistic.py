"""
1 -> Sum - Adds all elements:
ex - np.sum(arr)
10 + 20 + 30 + 40 + 50 = 150

2 -> Mean (Average)
ex - np.mean(arr)

Formula:
Mean = Number of Values / Sum of Values

3 -> Max (largest value)
ex - np.max(arr)

4 -> Min (smallest value)
ex - np.min(arr)

"""

import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))