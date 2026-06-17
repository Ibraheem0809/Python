import pandas as pd

#pd.set_option('display.max_columns', None)

df_csv = pd.read_csv("/home/dell/Desktop/Python/Data/employee.csv")
print(df_csv.to_string())

df_json = pd.read_json("/home/dell/Desktop/Python/Data/employee.json")
print(df_json)

