# Working with different file formats
# Data Engineering
# Data engineering is one of the most critical and foundational skills in any data scientist’s toolkit.

# Data Engineering Process
# 1. Extract - Data extraction is getting data from multiple sources. Ex. Data extraction from a website using Web scraping or gathering information from the data that are stored in different formats(JSON, CSV, XLSX etc.).
# 2. Transform - Transforming the data means removing the data that we don't need for further analysis and converting the data in the format that all the data from the multiple sources is in the same format.
# 3. Load - Loading the data inside a data warehouse. Data warehouse essentially contains large volumes of data that are accessed to gather insights.

# Comma-separated values (CSV) file format
# In a spreadsheet file format, data is stored in cells. Each cell is organized in rows and columns.
# A column in the spreadsheet file can have different types.
# For example, a column can be of string type, a date type, or an integer type.

# Reading data from CSV in Python
# The Pandas Library is a useful tool that enables us to read various datasets into a Pandas data frame.
# We use pandas.read_csv() function to read the csv file. In the parentheses, we put the file path along with a quotation mark as an argument, so that pandas will read the file into a data frame from that address.
# The file path can be either a URL or your local file address.
import pandas as pd
import requests
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Define the URL of the CSV file to download
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Download the file synchronously using requests and save it in the target directory
response = requests.get(filename)
if response.status_code == 200:
    # Write the downloaded content to the target directory
    with open(os.path.join(target_dir, "addresses.csv"), "wb") as f:
        f.write(response.content)

# Read the CSV file from the target directory into a pandas DataFrame, assuming no header row
df = pd.read_csv(os.path.join(target_dir, "addresses.csv"), header=None)

# Print the DataFrame to the console
print("Original DataFrame:")
print(df)

# Adding column names to the DataFrame
# We can add columns to an existing DataFrame using its columns attribute.
df.columns = ['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']
print("\nDataFrame with Column Names:")
print(df)

# Selecting a single column
# To select the first column 'First Name', you can pass the column name as a string to the indexing operator.
print("\nFirst Name Column:")
print(df["First Name"])

# Selecting multiple columns
# To select multiple columns, you can pass a list of column names to the indexing operator.
df = df[['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']]
print("\nDataFrame with Selected Columns:")
print(df)

# Selecting rows using .loc and .iloc

# loc() : loc() is label-based data selecting method which means that we have to pass the name of the row or column which we want to select.
# To select the first row
print("\nFirst Row using loc():")
print(df.loc[0])

# To select the 0th, 1st, and 2nd row of the 'First Name' column only
print("\nFirst Three Rows of 'First Name' Column using loc():")
print(df.loc[[0, 1, 2], "First Name"])

# iloc() : iloc() is an index-based selecting method which means that we have to pass integer index in the method to select specific row/column.
# To select the 0th, 1st, and 2nd row of the 'First Name' column only
print("\nFirst Three Rows of 'First Name' Column using iloc():")
print(df.iloc[[0, 1, 2], 0])

# Transform Function in Pandas
# Python's Transform function returns a self-produced dataframe with transformed values after applying the function specified in its parameter.

#import library
import pandas as pd
import numpy as np

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# Let’s say we want to add 10 to each element in a dataframe:
# applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
print(result)

# JSON file Format
# JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.
# Writing JSON to a File
import json
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Define the dictionary to be converted to JSON
person = {
    'first_name': 'Mark',
    'last_name': 'abc',
    'age': 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Serialization using dump() function
# json.dump() method can be used for writing to JSON file.
# Syntax: json.dump(dict, file_pointer)
# Parameters:
# dictionary – name of the dictionary which should be converted to JSON object.
# file pointer – pointer of the file opened in write or append mode.

# Define the full path for saving the file in the target directory
output_path = os.path.join(target_dir, 'person.json')

# Write the dictionary as a JSON object to the specified path
with open(output_path, 'w') as f:
    json.dump(person, f)

# serialization using dumps() function
# json.dumps() that helps in converting a dictionary to a JSON object.
# Parameters:
# dictionary – name of the dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation
# Serializing json  
import json
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Define the dictionary to be converted to JSON
person = {
    'first_name': 'Mark',
    'last_name': 'abc',
    'age': 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Serialization using dumps() function
# json.dumps() method converts a Python object into a JSON string.
json_object = json.dumps(person, indent=4)

# Writing to sample.json in the target directory
output_path = os.path.join(target_dir, "sample.json")
with open(output_path, "w") as outfile:
    outfile.write(json_object)

# Print the JSON string
print("JSON String:")
print(json_object)

# Reading JSON to a File
# Using json.load()
# The JSON package has json.load() function that loads the JSON content from a JSON file into a dictionary.
import json  # Already imported, kept for clarity

# Opening JSON file from the target directory
with open(output_path, 'r') as openfile:
    # Reading from JSON file
    json_object = json.load(openfile)

# Print the loaded JSON object and its type
print("\nLoaded JSON Object:")
print(json_object)
print("Type of Loaded Object:", type(json_object))

# XML file format
# XML is also known as Extensible Markup Language.
# As the name suggests, it is a markup language. It has certain rules for encoding data. XML file format is a human-readable and machine-readable file format.

# Writing with xml.etree.ElementTree
# The xml.etree.ElementTree module comes built-in with Python. It provides functionality for parsing and creating XML documents.
# ElementTree represents the XML document as a tree. We can move across the document using nodes which are elements and sub-elements of the XML file.
import xml.etree.ElementTree as ET
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# Create a new XML file with the results
mydata1 = ET.ElementTree(employee)

# Define the full path for saving the file in the target directory
output_path = os.path.join(target_dir, "new_sample.xml")

# Write the XML file to the specified path
with open(output_path, "wb") as files:
    mydata1.write(files)
# Reading with xml.etree.ElementTree
# Not needed unless running locally
# !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml

import xml.etree.ElementTree as etree
import requests
import pandas as pd  # Added to fix the missing import
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Define the URL of the XML file to download
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Download the file synchronously using requests and save it in the target directory
response = requests.get(filename)
if response.status_code == 200:
    # Write the downloaded content to the target directory
    with open(os.path.join(target_dir, "Sample-employee-XML-file.xml"), "wb") as f:
        f.write(response.content)

# You would need to firstly parse an XML file and create a list of columns for DataFrame, then extract useful information from the XML file and add to a pandas DataFrame.
# Parse the XML file from the target directory
tree = etree.parse(os.path.join(target_dir, "Sample-employee-XML-file.xml"))

# Get the root of the XML tree
root = tree.getroot()

# Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]

# Initialize an empty DataFrame
dataframe = pd.DataFrame(columns=columns)  # Corrected typo from 'datatframe' to 'dataframe'

# Iterate through each node in the XML root
for node in root:
    # Extract text from each element
    firstname = node.find("firstname").text if node.find("firstname") is not None else None
    lastname = node.find("lastname").text if node.find("lastname") is not None else None
    title = node.find("title").text if node.find("title") is not None else None
    division = node.find("division").text if node.find("division") is not None else None
    building = node.find("building").text if node.find("building") is not None else None
    room = node.find("room").text if node.find("room") is not None else None
    
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    
    # Concatenate with the existing DataFrame
    dataframe = pd.concat([dataframe, row_df], ignore_index=True)

# Print the DataFrame to the console
print(dataframe)

# Save Data
# Pandas enables us to save the dataset to CSV by using the dataframe.to_csv() method, you can add the file path and name along with quotation marks in the parentheses.
# Save the DataFrame as employee.csv to the target directory
dataframe.to_csv(os.path.join(target_dir, "employee.csv"), index=False)
# We can also read and save other file formats, we can use similar functions to pd.read_csv() and df.to_csv() for other data formats. The functions are listed in the following table:csv	pd.read_csv()	df.to_csv()
"""
csv - Read: pd.read_csv(), Save: df.to_csv()
json - Read: pd.read_json(), Save: df.to_json()
excel - Read: pd.read_excel(), Save: df.to_excel()
hdf - Read: pd.read_hdf(), Save: df.to_hdf()
sql - Read: pd.read_sql(), Save: df.to_sql()

"""

# Binary File Format
# "Binary" files are any files where the format isn't made up of readable characters. It contain formatting information that only certain applications or processors can understand.
# While humans can read text files, binary files must be run on the appropriate software or processor before humans can read them.
# Binary files can range from image files like JPEGs or GIFs, audio files like MP3s or binary document formats like Word or PDF.
# Let's see how to read an Image file.

# Reading the Image file
# Python supports very powerful tools when it comes to image processing. Let's see how to process the images using the PIL library.
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
# importing PIL 
from PIL import Image 
import requests
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Define the URL of the image to download
filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Download the file synchronously using requests and save it in the target directory
response = requests.get(filename)
if response.status_code == 200:
    # Write the downloaded content to the target directory
    with open(os.path.join(target_dir, "dog.jpg"), "wb") as f:
        f.write(response.content)

# Read the image from the target directory
img = Image.open(os.path.join(target_dir, "dog.jpg"))

# Output the image (display it)
img.show()

# Data Analysis
# We have 768 rows and 9 columns. The first 8 columns represent the features and the last column represent the target/label.

# Import pandas library
import pandas as pd
import requests
import os

# Define the target directory
target_dir = r"C:\Users\js090\Desktop\IBM Data Analyst Professional Certificate\Python for Data Science, AI & Development\Module 5"

# Define the URL of the CSV file to download
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# Ensure the target directory exists or create it
os.makedirs(target_dir, exist_ok=True)

# Download the file synchronously using requests and save it in the target directory
response = requests.get(filename)
if response.status_code == 200:
    # Write the downloaded content to the target directory
    with open(os.path.join(target_dir, "diabetes.csv"), "wb") as f:
        f.write(response.content)

# Read the CSV file from the target directory into a pandas DataFrame
df = pd.read_csv(os.path.join(target_dir, "diabetes.csv"))

# Print the first few rows of the DataFrame to verify
print(df.head())

# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe, where n is an integer.
# Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
print(df.head(5))

# To view the dimensions of the dataframe, we use the .shape parameter.
df.shape

# Statistical Overview of dataset
# This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
df.info()

# Pandas describe() is used to view some basic statistical details like percentile, mean, standard deviation, etc. of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a different output
df.describe()

# Identify and handle missing values
# We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:
# .isnull()
# .notnull()
# The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.
missing_data = df.isnull()
missing_data.head(5)
# "True" stands for missing value, while "False" stands for not missing value.

# Count missing values in each column
# Using a for loop in Python, we can quickly figure out the number of missing values in each column.
# As mentioned above, "True" represents a missing value, "False" means the value is present in the dataset. In the body of the for loop the method ".value_counts()" counts the number of "True" values.
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

# Correct data format
# Check all data is in the correct format (int, float, text or other).
# In Pandas, we use
# .dtype() to check the data type
# .astype() to change the data type
# Numerical variables should have type 'float' or 'int'.
df.dtypes

# Visualization
# Visualization is one of the best way to get insights from the dataset. Seaborn and Matplotlib are two of Python's most powerful visualization libraries.
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()