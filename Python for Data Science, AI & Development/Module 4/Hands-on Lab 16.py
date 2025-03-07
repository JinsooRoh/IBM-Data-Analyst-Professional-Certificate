import urllib.request
import pandas as pd

# URL for the XLSX file
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
xlsx_filename = "Product-sales.xlsx"

# Download the XLSX file using urllib.request
urllib.request.urlretrieve(xlsx_path, xlsx_filename)
print("XLSX Download completed. File saved as", xlsx_filename)

# Read the downloaded XLSX file into a DataFrame
df_xlsx = pd.read_excel(xlsx_filename)

# Display the first few rows of the DataFrame
print("XLSX File head:")
print(df_xlsx.head())

# Access to the column Length
x = df_xlsx[['Quantity']]
x

# Get the column as a series
x = df_xlsx['Product']
x

# Get the column as a dataframe
x = df_xlsx[['Quantity']]
type(x)

# Access to multiple columns
y = df_xlsx[['Product','Category', 'Quantity']]
y

# Access the value on the first row and the first column
df_xlsx.iloc[0, 0]

# Access the value on the second row and the first column
df_xlsx.iloc[1,0]

# Access the value on the first row and the third column
df_xlsx.iloc[0,2]

# Access the value on the second row and the third column
df_xlsx.iloc[2,2]

# Access the column using the name
df_xlsx.loc[0, 'Product']

# Access the column using the name
df_xlsx.loc[1, 'Product']

# Access the column using the name
df_xlsx.loc[1, 'CustomerCity']

# Access the column using the name
df_xlsx.loc[1, 'Total']

# Slicing the dataframe
df_xlsx.iloc[0:2, 0:3]

# Slicing the dataframe using name
df_xlsx.loc[0:2, 'OrderID':'Category']

# Quiz on DataFrame
# 1. Use a variable q to store the column Price as a dataframe
q = df_xlsx[['Price']]
q

# 2. Assign the variable q to the dataframe that is made up of the column Product and Category:
q = df_xlsx[['Product', 'Category']]
q

# 3. Access the 2nd row and the 3rd column of df:
df_xlsx.iloc[1,2]

# 4. Use the following list to convert the dataframe index df to characters and assign it to df_new;
# find the element corresponding to the row index a and column 'CustomerCity'.
# Then select the rows a through d for the column 'CustomerCity'
new_index = ['a','b','c','d','e']

df_new = df_xlsx
df_new.index = new_index
df_new.loc['a', 'CustomerCity']
df_new.loc['a':'d', 'CustomerCity']
