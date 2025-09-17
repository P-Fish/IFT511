import pandas as pd

df = pd.read_csv('adult.data', header=None, na_values=' ?')
"""
Attribute types
Categorical: 1, 5, 6, 7, 8, 9, 13
Ordinal: 3, 14
Interval:
Ratio: 0, 2, 4, 10, 11, 12
"""

df_cleaned = df.dropna()

df = df_cleaned[ [0, 2, 4, 10, 11, 12] ]

for col in df_cleaned.columns:
    df = pd.concat([df, pd.get_dummies(df_cleaned[col])])

print(df.columns)

edu = {
    " Preschool"    :1,
    " 1st-4th"      :2,
    " 5th-6th"      :3,
    " 7th-8th"      :4,
    " 9th"          :5,
    " 10th"         :6,
    " 11th"         :7,
    " 12th"         :8,
    " HS-grad"      :9,
    " Some-college" :10,
    " Assoc-acdm"   :11,
    " Assoc-voc"    :11,
    " Bachelors"    :12,
    " Masters"      :13,
    " Prof-school"  :14,
    " Doctorate"    :15
}

df_cleaned[3].map(edu)