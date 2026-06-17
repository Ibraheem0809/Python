import matplotlib.pyplot as plt
import numpy as np

"""
Scatter Plot- A scatter plot is a graph that displays data as dots to show the relationship between two variables.
"""

x1 = np.array([1, 2, 3, 4, 5, 6])      # Study Hours
y1 = np.array([40, 50, 55, 65, 75, 85]) # Exam Scores

x2 = np.array([4, 3, 5, 6, 1, 2])      # Study Hours
y2 = np.array([55, 75, 40, 85, 50, 65]) # Exam Scores

plt.scatter(x1, y1, label="Class-A", color="red")
plt.scatter(x2, y2, label="Class-B", color="blue")

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.legend()

plt.show()