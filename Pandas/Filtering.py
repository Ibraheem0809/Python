import pandas as pd

# Filtering - Keeping the rows that match a condition
df = pd.read_csv("/home/dell/Desktop/Python/Data/gotCharacter.csv")

stark = df[df["House"] == "Stark"]
northern_stark = df[(df["House"] == "Stark") & 
                    (df["Region"] == "The North")]

alive_lannister = df[(df["House"] == "Lannister") & 
                    (df["Status"] == "Alive")]
print(alive_lannister)