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