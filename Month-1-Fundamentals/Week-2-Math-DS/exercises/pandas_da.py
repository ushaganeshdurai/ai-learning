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

'''
Using dataset from Exercise 2:
1. Filter rows where age > 30 (or equivalent column)
2. Filter rows where salary (or value) between 50000-70000
3. Filter multiple conditions (AND, OR)
4. Select specific columns
5. Get rows by label (iloc, loc)
'''
print("Filter rows where age > 30: ",titanic_df[titanic_df["Age"]>30])
print("Filter rows where salary (or value) between 50000-70000: ")

try:
    # Filter rows: salary not null AND between 50000-70000
    filtered = df[(df["salary"].notna()) & (df["salary"] >= 50000) & (df["salary"] <= 70000)]
    print(filtered)

except Exception as e:
    print(f"Error occurred: {e}")

#print(titanic_df["Survived"])

#Select passengers who are male AND older than 30
print(titanic_df[(titanic_df["Sex"] == "male" )&( titanic_df["Age"]>30)])
print(titanic_df[(titanic_df["Sex"]=="female" )|(titanic_df["Pclass"]==1)])
print(titanic_df[(titanic_df["Survived"]==1) & (titanic_df["Sex"]=="male")])
print(titanic_df[((titanic_df["Sex"] == "male" )&( titanic_df["Age"]>30)) &((titanic_df["Survived"]==1) & (titanic_df["Sex"]=="female")) ])