import pandas as pd

"""s = pd.Series([10,20,30,40,50])
print(s)

data = {
    "Name":["Sidd", "Ibraheem", "Md"],
    "Age":[21,20,22]
}
df = pd.DataFrame(data)
print(df)"""

data = {
    "Subject":["OS","TAFL","DAA","OOT","DMS","PP"],
    "GradePt":[9,8,9,8,8,7]
}

df = pd.DataFrame(data)
print(df)

print(df["GradePt"].mean())
print(df["GradePt"].max())
print(df[df["GradePt"] == df["GradePt"].max()])

