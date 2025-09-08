import pandas as pd

def print_problem(num):
    print("\n")
    print("=" * 40)
    print(f"Problem {num:d}")
    print("=" * 40)

#Problem 1
print_problem(1)
df = pd.read_csv("sample_googleplaystore.csv")
ratings_mean = df["Rating"].mean()
print(f"The mean rating for apps is {ratings_mean:.2f}")

#Problem 2
print_problem(2)
categories = df["Category"].unique().tolist()
for category in categories:
    x = df[df["Category"] == category]
    avg = x["Rating"].mean()
    print(category, "=", "%.2f" % avg)

#Problem 3
print_problem(3)
print("Non-numeric columns")
for column in df.columns:
    if df[column].dtypes not in ["int64", "float64"] and column != "App":
        num_unique = df[column].nunique()
        print(f'\nThere are {num_unique} unique labels in "{column}"')
        print(df[column].value_counts())

print("\n\nNumeric columns")
for column in df.columns:
    if df[column].dtypes in ["int64", "float64"]:
        print(f"\n{column} stats:")
        print(f"\tmin:{df[column].min():.2f}")
        print(f"\tmax:{df[column].max():.2f}")
        print(f"\tavg:{df[column].mean():.2f}")