import pandas as pd

# aggregate functions = Reduces a set of values into a single summary values
#                       Used to submerize and analyse data
#                       Often used with the groupby() function


df = pd.read_csv("/home/dell/Desktop/Python/Data/employee.csv")
df2 = pd.read_csv("/home/dell/Desktop/Python/Data/gotCharacter.csv")

# Whole DataFrame

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single Column

print(df["Salary"].mean())
print(df["Salary"].sum())
print(df["Salary"].min())
print(df["Salary"].max())
print(df["Salary"].count())

group = df.groupby("Age")

#print(group["Salary"].mean())
#print(group["Salary"].sum())
print(group["Salary"].min())
print(group["Salary"].max())
