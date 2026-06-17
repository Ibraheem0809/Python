import pandas as pd

df = pd.read_csv("gotCharacter.csv")
df.to_csv("clean.csv", index=False)