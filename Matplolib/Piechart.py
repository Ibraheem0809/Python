import matplotlib.pyplot as plt
import numpy as np 

"""
Pie chart- A pie chart is a circular chart divided into slices.
           Each slice shows a part of the whole, and its size depends on the value it represents.
           It helps us easily compare different parts of a total amount.
"""

categories= ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values= [300,250,275,225]
clrs= ["red","blue","yellow","green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=clrs,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90)
plt.show()