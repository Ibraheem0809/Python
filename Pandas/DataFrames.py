import pandas as pd

"""
DataFrames :-  A tabular data structure with rows and columns.
               (2D) Similar to an Excel SpreadSheet.
"""

data = {
    "Name":["Sidd","Ibraheem","Md"], 
    "Age":[21,20,19]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

print(df.loc["Employee 1"])

# Add new Column
df["Job"] = ["AI Intern", "Web Designer", "N/A"]

# Add new Row
new_row = pd.DataFrame([{"Name":"Santosh","Age":22,"Job":"AI Trainer"},
                        {"Name":"Zaqwan","Age":20,"Job":"App Developer"}],
                       index=["Employee 4","Employee 5"])
df = pd.concat([df,new_row])

print(df)