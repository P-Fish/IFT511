import pandas as pd

column_names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
                "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country",
                "income"]
"""
Problem 1: File Handling (2 Points)
"""
#Limited to 20 lines for readability
print(f"\n{"=" * 50}\nProblem 1: File Handling\n")
with open("adult-1.data", "r") as f:
    for i in range(20):
        print(f.readline().rstrip())

"""
Problem 2: Pandas Data Frames (2 Points)
"""
print(f"\n{"=" * 50}\nProblem 2: Pandas Data Frames\n")
df = pd.read_csv("adult-1.data", header=None)
print(f"There are {df[0].count()} rows in the data frame")

"""
Problem 3:  Data Slicing and Computing Stats (6 Points)
"""
print(f"\n{"=" * 50}\nProblem 3:  Data Slicing and Computing Stats\n")
df = pd.read_csv("adult-1.data", header=None)
df.columns = column_names

print(f"Age-min: {df['age'].min()}, Age-max: {df['age'].max()}, Age-avg: {df['age'].mean():.2f}\n")

filtered_df = df[df["education"] == " Masters"]

high_earner_count = len(filtered_df[filtered_df["income"] == " >50K"])
low_earner_count = len(filtered_df[filtered_df["income"] == " <=50K"])

print(f" Masters >50k: {high_earner_count:0d}, Masters <=50k: {low_earner_count:0d}")
print(f" Percent of Masters >50k: {high_earner_count / len(filtered_df):.1%}")
print(f" Percent of Masters <=50k: {low_earner_count / len(filtered_df):.1%}\n")

for val in df["education"].unique():
    filtered_df = df[df["education"] == val]
    high_earner_count = len(filtered_df[filtered_df["income"] == " >50K"])
    low_earner_count = len(filtered_df[filtered_df["income"] == " <=50K"])

    print(f"{val} >50k: {high_earner_count:0d}, {val} <=50k: {low_earner_count:0d}")
    print(f" Percent of{val} >50k: {high_earner_count / len(filtered_df):.1%}")
    print(f" Percent of{val} <=50k: {low_earner_count / len(filtered_df):.1%}\n")

for val in df["occupation"].unique():
    filtered_df = df[df["occupation"] == val]
    high_earner_count = len(filtered_df[filtered_df["income"] == " >50K"])
    low_earner_count = len(filtered_df[filtered_df["income"] == " <=50K"])

    print(f"{val} >50k: {high_earner_count:0d}, {val} <=50k: {low_earner_count:0d}")
    print(f" Percent of{val} >50k: {high_earner_count / len(filtered_df):.1%}")
    print(f" Percent of{val} <=50k: {low_earner_count / len(filtered_df):.1%}\n")

"""
Problem 4: Simple Dataset File Processing (2 Points)
"""
print(f"\n{"=" * 50}\nProblem 4: Simple Dataset File Processing\n")

df = pd.read_csv("sample_googleplaystore-1.csv")
print(df.head(10))
print()

counts = df["Category"].value_counts()

print(f"App count by {counts}\n")

#The axes are already sorted descending from the value_counts() function so you only need the first element
print(f"Category with the highest number of apps: {counts.axes[0][0]}")

for column in df.columns:
    if df[column].dtypes not in ["int64", "float64"]:
        print(f'\nDistinct values in the "{column}" column')
        counts = df[column].value_counts()
        for val in counts.axes[0]:
            l = counts[val]
            print(f'\t"{val}" has {l} occurrence{'s' if l > 1 else ''}')

"""
Problem 5: Simple Dataset File Processing (8 Points)
"""
print(f"\n{"=" * 50}\nProblem 5: Simple Dataset File Processing\n")

bins = [1, 2, 3, 4, 5]
labels = ['[1,2)', '[2,3)', '[3,4)', '[4,5]']
print(pd.cut(df['Rating'], bins=bins, labels=labels, right=False).value_counts())

# Extract year from 'Last Updated' column
df['Year'] = pd.to_datetime(df['Last Updated'], format='%d-%b-%y', errors='coerce').dt.year

# Group by year and apply rating binning
yearly_rating_dist = df.groupby('Year')['Rating'].apply(
    lambda x: pd.cut(x, bins=bins, labels=labels, right=False).value_counts()
).unstack(fill_value=0)

print("\nRating distribution within each year:")
print(yearly_rating_dist)

# Function to categorize Android version requirements
def categorize_version(version_str):
    if pd.isna(version_str) or version_str == 'NaN':
        return 'Unknown'

    version_str = str(version_str).strip()

    if 'Varies with device' in version_str:
        return 'Varies with device'

    # Extract the major version number
    if ' and up' in version_str:
        # Extract the number before ' and up'
        version_part = version_str.split(' and up')[0]
        try:
            # Handle versions like "4.0.3", "2.3.3", etc.
            major_version = int(float(version_part.split('.')[0]))
            return f'{major_version} & up'
        except:
            return 'Unknown'

    return 'Unknown'


# Apply categorization
df['Android_Category'] = df['Android Ver'].apply(categorize_version)

# Count apps by Android version category
android_counts = df['Android_Category'].value_counts()

print("\nAndroid Version Requirements:")
print(android_counts)