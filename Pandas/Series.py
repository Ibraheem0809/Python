import pandas as pd

"""
Series - In Pandas, a Series is a 1-dimensional labeled array.
         It is like a single column in a table.

         A Series can hold a numbers, strings, floats and any data type
         It has data values index (labels)
"""

data = [100, 102, 104, 200, 202]

# series = pd.Series(data)
# print(series)

"""
series = pd.Series(data, index=['a','b','c'])
series.loc['c'] = 200 # loc -> locating values 
print(series.loc['c'])

# iloc -> index of location
print(series.iloc[2])
"""

series = pd.Series(data, index=['a','b','c','d','e'])
print(series)

print(series[series < 200])

# if we use dictionary instead of list we don't need to
# use index as dict already have a key value pair

calories = {"Day 1":1750, "Day 2":2100, "Day 3":1600, "Day 4":1800, "Day 5":2050}

srs = pd.Series(calories)

print(srs)
srs.loc["Day 3"] += 100
print(srs[srs <= 2000])


 