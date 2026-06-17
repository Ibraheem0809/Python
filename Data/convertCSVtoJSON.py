import pandas as pd

df = pd.read_csv("employee.csv")

df.to_json("employee.json", orient="records", indent=4)
print("Data Converted Successfully!!")