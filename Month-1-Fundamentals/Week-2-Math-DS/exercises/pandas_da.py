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

print(f"Shape of dataframe: {df.shape} {df.dtypes} ")
print(df.head(2))
print(df["age"])

'''
Load and Explore Data

1. Load Titanic or iris dataset (use pandas/seaborn)
2. Print shape
3. Print first 5 rows
4. Print info() and describe()
5. Check data types
6. Count missing values
'''
titanic_df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(titanic_df.shape)
print("First 5 rows: ",titanic_df.head(5))
print(titanic_df.info(),titanic_df.describe())
print()
