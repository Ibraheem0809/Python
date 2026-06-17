import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,38,5])
y3 = np.array([13,15,20,30])

plt.grid(axis="both",color="lightgray")


plt.title("Class Size", fontsize=25,
                        family="Arial",
                        fontweight="bold",
                        color="#2d4cfc")

plt.xlabel("Years", fontsize=20,
                    family="Arial",
                    fontweight="bold",
                    color="#2dbefc")
plt.ylabel("Students", fontsize=20,
                       family="Arial",
                       fontweight="bold",
                       color="#2dbefc")

plt.tick_params(axis="both",
                color="#2dbefc")

plt.plot(x,y1,label="A")
plt.plot(x,y2,label="B")
plt.plot(x,y3,label="C")

plt.legend()
plt.xticks(x)

plt.show()
