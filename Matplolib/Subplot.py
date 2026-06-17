import matplotlib.pyplot as plt
import numpy as np

"""
Subplot- A subplot is one of several smaller plots contained within a single Matplotlib figure, used to compare or present multiple datasets side by side.

For example, a figure can contain:

2 subplots arranged vertically (2 rows, 1 column)
4 subplots arranged in a 2×2 grid
Any other grid arrangement


Figure - The entire Canva
Ax - A single plot(subplot)
"""

# instead of plot we can use diggerent graph (pie, bar etc)

x = np.array([1,2,3,4,5])
figure, axes = plt.subplots(2,2)

axes[0,0].plot(x,x*2,color="red")
axes[0,0].set_title("x*2")

axes[0,1].plot(x,x**2,color="blue")
axes[0,1].set_title("x**2")


axes[1,0].plot(x,x**3,color="green")
axes[1,0].set_title("x**3")


axes[1,1].plot(x,x**4,color="purple")
axes[1,1].set_title("x**4")

# to avoid overlapping we use
plt.tight_layout()
plt.show()
