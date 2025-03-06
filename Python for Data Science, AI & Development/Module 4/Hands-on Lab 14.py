# Reading Files Python
# Download Data

# Uncomment these if working locally, else let the following code cell run.
# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)
# Download Example file
# !wget Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

"""
from pyodide.http import pyfetch
import pandas as pd
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
await download(filename, "example1.txt")
print("done")

"""


import urllib.request

# Specify the URL from which the file will be downloaded and the filename to save it as.
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'example1.txt'

# Download the file from the URL and save it to the current working directory.
urllib.request.urlretrieve(url, filename)
print("Download completed. File saved as", filename)


# Example of reading the file:
with open(filename, "r", encoding="utf-8-sig") as file1:
    FileContent = file1.read()

    print("File content:\n", FileContent, sep="")


# Reading Text Files
# One way to read or write a file in Python is to use the built-in open function.
# The open function provides a File object that contains the methods and attributes you need in order to read, save, and manipulate the file.
# In this notebook, we will only cover .txt files.
# The first parameter you need is the file path and the file name.

# The mode argument is optional and the default value is r.
# In this notebook we only cover two modes:
# **r**: Read mode for reading files
# **w**: Write mode for writing files

# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()

# A Better Way to Open a File
# Using the 'with' statement is better practice, it automatically closes the file even if the code encounters an exception.
# The code will run everything in the indent block then close the file object.
# Open file using with
with open(filename, "r") as file1:
    FileContent = file1.read()
    print("File content: \n", FileContent, sep="")

# Check if the file is closed (outside the with block)
print("Is file closed?", file1.closed)

# Print the path and mode of file
print("File name:", filename)
print("File mode:", "r")

# See the content of file
print(FileContent)

# Using the 'with' statement is better practice, it automatically closes the file even if the code encounters an exception.
with open(filename, "r") as file1:
    print("Reading first four characters:")
    print(file1.read(4))  # Read first four characters

# Check if the file is closed after 'with' block
print("Is file closed after 'with' block?", file1.closed)

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
print(FileasList[0])

# Print the second line
print(FileasList[1])

# Print the third line
print(FileasList[2])