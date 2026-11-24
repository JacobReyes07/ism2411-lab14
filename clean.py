def ex(num):
    print(f" --- Exercise {num} --- ")
ex(1)
import pandas as pd
df = pd.read_csv("data/messy_sales.csv")
df.info()
print(df.isnull().sum())
# Column 4 is a string but should be a float.
# Column 6 is missing about 7.5%.
# Column 3 is missing about 2.3%
ex(2)
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns)
ex(3)
print(df.shape)
df["quantity_sold"] = df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
# This is like the one it showed in the reading which works because quantity_sold is the only thing that isn't a string and I just added the df["quantity_sold"] = at the start so that it stays like that.
df = df.dropna(subset=["order_id", "order_date"]) 
# This one was also taught in the reading and does the same thing and drops them which it says is because an order cannot be placed without them.
print(df.shape)
ex(4)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print(df["order_date"].isna().sum())
df["unit_price"] = df["unit_price"].str.replace("$", "", regex=False)
df["unit_price"] = df["unit_price"].str.replace(",", "", regex=False)
df["unit_price"] = df["unit_price"].str.replace("(", "", regex=False)
df["unit_price"] = df["unit_price"].str.replace(")", "", regex=False)
df["unit_price"] = df["unit_price"].astype(float)
df["quantity_sold"] = df["quantity_sold"].astype(int)
df["revenue"] = (df["unit_price"] * df["quantity_sold"]).round(2)
print(df.dtypes)
ex(5)
df.duplicated().sum()
df = df.drop_duplicates()
print(df.shape)
ex(6)
print(df.describe())
df = df[df["quantity_sold"] != 9999]
# Max quantity sold 9999 looks like someone probably accidentally typed it.
# 59994 revenue is really high and probably an accident that is probably caused by the quantity sold of 9999 and 59994 is evenly divisible by 9999 which equals six so I think that is likely.
ex(7)
df.to_csv("data/clean_sales.csv", index = False)
csdf = pd.read_csv("data/clean_sales.csv")
csdf.info()
csdf = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])
csdf.info()