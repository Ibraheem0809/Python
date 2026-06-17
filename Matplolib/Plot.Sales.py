import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Mon","Tue","Wed","Thu","Fri"])

y1 = np.array([15, 25, 10, 14, 19])  # Week 1
y2 = np.array([20, 18, 22, 17, 15])  # Week 2
y3 = np.array([12, 14, 16, 20, 18])  # Week 3
y4 = np.array([25, 22, 19, 23, 21])  # Week 4

plt.plot(x, y1, label="Week 1", marker="o")
plt.plot(x, y2, label="Week 2", marker="o")
plt.plot(x, y3, label="Week 3", marker="o")
plt.plot(x, y4, label="Week 4", marker="o")

plt.title("Monthly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.show()