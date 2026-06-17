import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/home/dell/Desktop/Python/Data/gotHouses.csv")

x = (df["House"])
y = (df["Army_Size"])

#plt.barh(x,y)
#plt.tight_layout()

plt.pie(y, labels=x, autopct="%1.1f%%", startangle=90)

plt.title("Army Size Distribution of GOT Houses")

plt.show()