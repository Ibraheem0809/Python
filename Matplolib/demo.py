import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

plt.plot(x, y, marker='o', linestyle='-', color='blue')

plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()