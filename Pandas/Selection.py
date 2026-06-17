import pandas as pd 

df = pd.read_csv("/home/dell/Desktop/Python/Data/gotCharacter.csv")

# SELECTION by COLUMN/s(.to_string() method is used to display full data of large file)
"""
print(df["Name"])
print(df["House"])
print(df["Status"])
"""
#print(df[["Name","Title"]].to_string())

# SELECTION by ROW/s

"""
print(df.loc[0,["Name","Title","Region"]])
# print(df.loc[0:5]) # rows
print(df.iloc[0:11:2, 0:3])
#print(df[df["House"] == "Stark"].to_string())
print(df[df["Name"] == "Lancel Lannister"])
"""

ch = input("Enter a GOT character: ")

result = df[df["Name"].str.lower() == ch.lower()]

if result.empty:
    print(f"{ch} NOT Found")
else:
    print(result.to_string(index=False))