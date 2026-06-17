import matplotlib.pyplot as plt
import numpy as np 

"""
Histogram- A visual representation of the distribution of quantitative data.
           They group values into bins (intervals)
           and counts how many fall in each range.
"""

scores = np.random.normal(loc=80, scale=50, size=100)
scores = np.clip(scores, 0, 100)
"""
loc=80 → mean (average) score is 80.
scale=10 → standard deviation is 10.
size=100 → generate 100 scores.
"""
plt.hist(scores, bins=10, edgecolor='black')

plt.title("Distribution of Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()