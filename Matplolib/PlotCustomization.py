import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Mon","Tue","Wed","Thu","Fri"])
y1 = np.array([15, 25, 10, 14, 19])  # Week 1
y2 = np.array([20, 18, 22, 17, 15])  # Week 2

line_style = dict(marker=".",
                  markersize=30,
                  markerfacecolor="#1cd3fc",
                  mec="#1cd3fc",
                  ls="solid",
                  linewidth=3,
                  color="#1c5bfc")

"""
markersize can be written as ms
markerfacecolor can be written as mfc
markeredgecolor can be written as mec
linestyle can be written as ls(none,solid,dashed,dotted,dashdot)
"""
plt.plot(x,y1, **line_style) # instead of copying used line_style as dictionary
plt.plot(x,y2, **line_style)



# Title
plt.title("Monthly Sale")

# X & Y - Label
plt.xlabel("Days")
plt.ylabel("Sales")

plt.show()
