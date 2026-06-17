"""

Variance and standard deviation measure that spread.

Variance measures how far values are from the mean on average.
Standard deviation is the square root of variance and is easier to interpret.


Why do AI engineers often calculate:
Mean & Standard Deviation before training a model?

AI engineers calculate mean and standard deviation to understand the distribution of data and to standardize/normalize features before training. Many machine learning algorithms perform better when features are on similar scales.

Example:

Age:      18 - 60
Salary:   20,000 - 2,000,000

Without scaling, Salary can dominate the model because its values are much larger.

"""


import numpy as np

data = np.array([10,20,30,40,50])

mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

data1 = np.array([10, 10, 10, 10, 10])
data2 = np.array([1, 5, 10, 15, 19])
print(np.var(data1))
print(np.std(data2))