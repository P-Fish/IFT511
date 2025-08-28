import pandas as pd

column_names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
                "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country",
                "income"]
"""
Problem 1: File Handling (2 Points)
Write a python script that reads the adult.data file (US Census Dataset, link above) and prints each record (row). To do so:

Use the open() function to create a file handle.
Use a for loop to scan the file line by line, and use the print function to print each line.
"""
print(f"\n{"=" * 50}\nProblem 1: File Handling\n")
with open("adult-1.data", "r") as f:
    for line in f:
        print(line.rstrip())
"""
Problem 2: Pandas Data Frames (2 Points)
Write a python script that reads adult.data into a data frame. Then print the number of rows in the data frame. 

Notice that this file does not have column headers. You will need to specify the header=Noneoption inside the read_csv() function.
To find the number of rows, you can use the count() function. However, this will count the number of values within each column! To overcome that, select the first row: df[0] and then call the count()function for this single column as follows: df[0].count()
"""
print(f"\n{"=" * 50}\nProblem 2: Pandas Data Frames\n")
df = pd.read_csv("adult-1.data", header=None)
print(f"There are {df[0].count()} rows in the data frame")
"""
Problem 3:  Data Slicing and Computing Stats (6 Points)
Write a script that reads a US Census file into a data frame and

Finds the min, max, avg ages.
Finds the number of persons with Master's making more than 50K vs. the number of persons with Master's making less than 50K.
Finds the percentage of Master's making more than 50K vs. the percentage of Master's making less than 50K.
Finds the percentage of people making more than 50K vs those making less than 50K for each education level.
Repeat the same activity above (only number 4) for each type of occupation, that's column 1.
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
Write a python script that reads the sample google play store apps data file into a data frame. Notice that this file has the column headers. 

Print the first 10 records of the data frame using the print function.
Notice that the second column holds the category of the app. An app category can be Business, Education, etc. 

Find the total number of apps for each category. This can be done by extracting the 'Category' column and counting the number of occurrences of each category using the value_counts()function.
Which category has the highest number of apps? Write code that prints that category, and the number of apps associated with it. Look into these functions: max(), idxmax().
Write a piece of code that finds for each non numeric column, the distinct values that appear in this column, and the frequency of occurrence of each value. For example, for the category column, the code should print all the categories listed, and the number of times each category appears in this column.
"""
print(f"\n{"=" * 50}\nProblem 4: Simple Dataset File Processing\n")

"""
Problem 5: Simple Dataset File Processing (8 Points)
For the google play dataset, find the following:

The rating distribution of different apps. That is, how many apps have an average rating in the range [1,2), [2,3), [3,4) and [4,5]. Notice the inclusive/exclusive brackets. (2 points)
Repeat the exercise above to show the rating distributions within each year. (3 points)
Find the number of apps with android version 1&up, 2&up, 3&up, 4&up and the number of apps whose android version varies with the device. (3 points)
"""
print(f"\n{"=" * 50}\nProblem 5: Simple Dataset File Processing\n")
