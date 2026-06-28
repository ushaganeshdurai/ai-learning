'''
Creating Dataframe
1.Create DataFrame from dict:
   {"name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]}
2. Print shape, columns, dtypes
3. Access first 2 rows
4. Access single column
'''
import pandas as pd 
df = pd.DataFrame( {"name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]}
)

print(f"Shape of dataframe: {df.shape()} {df.dtypes()} ")
print(df.head(2))
print(df["age"])
