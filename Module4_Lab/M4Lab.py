import pandas as pd

df = pd.read_csv("agaricus-lepiota.data", header=None)
print(df.isna().value_counts())
