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
