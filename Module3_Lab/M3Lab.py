import pandas as pd

def print_problem(num):
    print("\n")
    print("=" * 40)
    print(f"Problem {num:d}")
    print("=" * 40)


df = pd.read_csv("sales.csv")
print_problem(1)
vc = df["product_type"].value_counts()
print(f"{vc.axes[0][0]} has the highest purchase count")
print()
print(vc)

print_problem(2)
purchase_date = df["purchase_date"]
df["month"] = pd.DatetimeIndex(purchase_date).month
df["month_name"] = pd.DatetimeIndex(purchase_date).month_name()
ppm = df["month"].value_counts()
ppmn = df["month_name"].value_counts()
print(ppm)
print()
print(ppmn)