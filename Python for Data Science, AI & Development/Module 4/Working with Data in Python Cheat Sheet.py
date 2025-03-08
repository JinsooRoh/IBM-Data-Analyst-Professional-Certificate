# Reading and writing files
# File opening modes
# Syntax: r (reading) w (writing) a (appending) + (updating: read/write) b (binary, otherwise text)
# Examples:
# with open("data.txt", "r") as file: content = file.read() print(content) with open("output.txt", "w") as file: file.write("Hello, world!") with open("log.txt", "a") as file: file.write("Log entry: Something happened.") with open("data.txt", "r+") as file: content = file.read() file.write("Updated content: " + content)</td>

# File reading methods
# Syntax:
# file.readlines() # reads all lines as a list
# readline() # reads the next line as a string
# file.read() # reads the entire file content as a string
# Example:
with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()

# File writing methods
# Syntax:
# file.write(content) # writes a string to the file
# file.writelines(lines) # writes a list of strings to the file
# Example:
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Iterating over lines
# Syntax:
# for line in file: # Code to process each line
# Example:
with open("data.txt", "r") as file:
    for line in file: print(line)

# Open() and close()
# Syntax:
# file = open(filename, mode) # Code that uses the file
# file.close()
# Example
file = open("data.txt", "r")
content = file.read()
file.close()

# with open()
# Syntax:
# with open(filename, mode) as file: # Code that uses the file
# Example
with open("data.txt", "r") as file:
    content = file.read()

# Pandas
import pandas as pd

# .read_csv()
# Syntax: dataframe_name = pd.read_csv("filename.csv") Example: df = pd.read_csv("data.csv")

# .read_excel()
# Syntax:
# dataframe_name = pd.read_excel("filename.xlsx")
# Example:
df = pd.read_excel("data.xlsx")

# .to_csv()
# Syntax:
# dataframe_name.to_csv("output.csv", index=False)
# Example:
df.to_csv("output.csv", index=False)

# Access Columns
# Syntax:
# dataframe_name["column_name"] # Accesses single column
# dataframe_name[["column1", "column2"]] # Accesses multiple columns
# Example:
df["age"]
df[["name", "age"]]

# describe()
# Syntax:
# dataframe_name.describe()
# Example:
df.describe()

# drop()
# Syntax:
# dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
# dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)
# Example:
df.drop(["age", "salary"], axis=1, inplace=True) # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True) # Will drop rows

# dropna()
# Syntax:
# dataframe_name.dropna(axis=0, inplace=True)
# Example:
df.dropna(axis=0, inplace=True)

# duplicated
# Syntax:
# dataframe_name.duplicated()
# Example:
duplicate_rows = df[df.duplicated()]

# Filter Rows
# Syntax:
# filtered_df = dataframe_name[(Conditional_statements)]
# Example:
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]

# groupby()
# Syntax:
# grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True,
# sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)
# Example:
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})

# head()
# Syntax:
# dataframe_name.head(n)
# Example:
df.head(5)

# Import pandas
# Syntax:
# import pandas as pd
# Example:
import pandas as pd

# info()
# Syntax:
# dataframe_name.info()
# Example:
df.info()

# merge()
# Syntax:
# merged_df = pd.merge(df1, df2, on=["column1", "column2"])
# Example:
merged_df = pd.merge(sales, products, on=["product_id", "category_id"]) # type: ignore

# print DataFrame
# Syntax:
# print(df) # or just type df
# Example:
print(df)
df

# replace()
# Syntax:
# dataframe_name["column_name"].replace(old_value, new_value, inplace=True)
# Example:
df["status"].replace("In Progress", "Active", inplace=True)

# tail()
# Syntax:
# dataframe_name.tail(n)
# Example:
df.tail(5)

# NumPy
# Importing NumPy
# Syntax:
# import numpy as np
# Example:
import numpy as np

# np.array()
# Syntax:
# array_1d = np.array([list1 values]) # 1D Array
# array_2d = np.array([[list1 values], [list2 values]]) # 2D Array
# Example:
array_1d = np.array([1, 2, 3]) # 1D Array
array_2d = np.array([[1, 2], [3, 4]]) # 2D Array

# Numpy Array Attributes
# Example:
np.mean(array) # type: ignore
np.sum(array) # type: ignore
np.min(array) # type: ignore
np.max(array) # type: ignore
np.dot(array_1, array_2) # type: ignore

