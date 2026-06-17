import pandas as pd

#Data Cleaning - The process of fixing/removing
#                incomplete, irrelevant, incorrect data
#                ~75% of work done with pandas is data cleaning

df = pd.read_csv("/home/dell/Desktop/Python/Data/gotCharacter.csv")

# 1. Drop Irrelevant Data

df = df.drop(columns=["CharacterID"])


# 2. Handle Missing Data [dropna() == drop not available]

# df = df.dropna(subset=["House"])
df = df.fillna({"House":"None"})


# 3. Fix Inconsistent Value
df["House"] = df["House"].replace({"None":"N/A","Stark":"STARK"})


# 4. Standardize Text
df["Name"] = df["Name"].str.upper()


# 5. Fix Data Types
df["Status"] = df["Status"].astype(bool)


# 6. Remove Duplicate Values
df = df.drop_duplicates()

print(df)