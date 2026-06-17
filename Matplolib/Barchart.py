import matplotlib.pyplot as plt
import numpy as np 

"""
BarCharts - Compare categories of data by representing each category with a bar
"""

categories= ["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"]
values= np.array([4,3,2,5,3,1])

plt.title("Daily Consumption", fontsize="25", fontweight="semibold")
plt.xlabel("Food", fontsize="15", fontweight="semibold")
plt.ylabel("Quantity", fontsize="15", fontweight="semibold")

# Vertical
plt.bar(categories,values, color="skyblue")

# Horizontal
#plt.barh(categories,values, color="skyblue")

plt.show() 