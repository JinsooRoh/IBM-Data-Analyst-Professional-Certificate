# Importing Pandas
import pandas as pd

# Data Loading
import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# What is a Series?
import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

print(s)

# Accessing Elements in a Series
# Accessing by label
print(s[2])     # Access the element with label 2 (value 30)

# Accessing by position
print(s.iloc[3]) # Access the element at position 3 (value 40)

# Accessing multiple elements
print(s[1:4])   # Access a range of elements by label

# Series Attributes and Methods
# values: Returns the Series data as a NumPy array.
# index: Returns the index (labels) of the Series.
# shape: Returns a tuple representing the dimensions of the Series.
# size: Returns the number of elements in the Series.
# mean(), sum(), min(), max(): Calculate summary statistics of the data.
# unique(), nunique(): Get unique values or the number of unique values.
# sort_values(), sort_index(): Sort the Series by values or index labels.
# isnull(), notnull(): Check for missing (NaN) or non-missing values.
# apply(): Apply a custom function to each element of the Series.

# Creating DataFrames from Dictionaries:
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)

# Column Selection:
print(df['Name'])  # Access the 'Name' column

# Accessing Rows:
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

# Slicing:
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# Finding Unique Elements:
unique_dates = df['Age'].unique()

# Conditional Filtering:
high_above_102 = df[df['Age'] > 25]

# Saving DataFrames:
df.to_csv('trading_data.csv', index=False)

# DataFrame Attributes and Methods
# shape: Returns the dimensions (number of rows and columns) of the DataFrame.
# info(): Provides a summary of the DataFrame, including data types and non-null counts.
# describe(): Generates summary statistics for numerical columns.
# head(), tail(): Displays the first or last n rows of the DataFrame.
# mean(), sum(), min(), max(): Calculate summary statistics for columns.
# sort_values(): Sort the DataFrame by one or more columns.
# groupby(): Group data based on specific columns for aggregation.
# fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
# apply(): Apply a function to each element, row, or column of the DataFrame.