# 1. What are Strings?
# Use quotation marks for defining string
"The BodyGuard"

# Use single quotation marks for defining string
'The BodyGuard'

# Digitals and spaces in string
print('1 2 3 4 5 6 ')

# Special characters in string
print('@#2_#]&*^%$')

# Print the string
print("hello!")

# Assign string to variable
name = "The BodyGuard"
print(name)

# 2. Indexing
# Print the first element in the string
print(name[0])

# Print the element on index 6 in the string
print(name[6])

# Print the element on the 10th index in the string
print(name[10])

# Print the last element in the string
print(name[-1])

# Print the first element in the string
print(name[-13])

# Find the length of string
print(len("The BodyGuard"))

# 3. Slicing
# Take the slice on variable name with only index 0 to index 3
name[0:4]

# Take the slice on variable name with only index 8 to index 11
name[8:12]

# 3. Stride
# Get every second element. The elments on index 1, 3, 5 ...
name[::2]

# Get every second element in the range from index 0 to index 4
name[0:5:2]

# 4. Concatenate Strings
# Concatenate two strings
name = "The BodyGuard"

statement = name + " is the best album"
print(statement)

# Print the string for 3 times
3 * "The BodyGuard"

# Concatenate strings

name = "The BodyGuard"
name = name + " is the best album"
print(name)

# 5. Escape Sequences
# New line escape sequence
print(" The BodyGuard\n is the best album" )

# Tab escape sequence
print(" The BodyGuard \t is the best album" )

# Include back slash in string
print(" The BodyGuard \\ is the best album" )

# r will tell python that string will be display as raw string
print(r" The BodyGuard \ is the best album" )

# 6. String Manipulation Operations
# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "The BodyGuard is the best album"
b = a.replace('BodyGuard', 'Janet')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "The BodyGuard"
name.find('he')

# Find the substring in the string.
name.find('Guard')

# If cannot find the substring in the string
name.find('Jasdfasdasdf')

#Split the substring into list
name = "The BodyGuard"
split_string = (name.split())
print(split_string)

text = "apple,banana,grape,orange"
result = text.split(",")
print(result)

text = "apple banana grape orange"
result = text.split(" ", 2)  # Maximum twice split
print(result)

text = "Hello\nWorld\nPython"
result = text.split("\n")
print(result)

# 7. RegEx
import re

s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


# Check if consecutive digits were found
import re

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# Regular Expression Special Characters (Sequences) in Python

# \d  - Matches any digit (0-9)
# Example: r"\d\d\d" matches "123"
import re
print(re.findall(r"\d\d\d", "My code is 123."))  # Output: ['123']

# \D  - Matches any non-digit character
# Example: r"\D\D\D" matches "abc"
print(re.findall(r"\D\D\D", "abc123"))  # Output: ['abc']

# \w  - Matches any word character (a-z, A-Z, 0-9, and _)
# Example: r"\w\w\w" matches "cat"
print(re.findall(r"\w\w\w", "cat_123"))  # Output: ['cat', '_12']

# \W  - Matches any non-word character
# Example: r"\W\W\W" matches "@#%"
print(re.findall(r"\W\W\W", "@#%abc"))  # Output: ['@#%']

# \s  - Matches any whitespace character (space, tab, newline, etc.)
# Example: r"\s" matches " " in "hello world"
print(re.findall(r"\s", "hello world"))  # Output: [' ']

# \S  - Matches any non-whitespace character
# Example: r"\S\S\S" matches "hey"
print(re.findall(r"\S\S\S", "hey there!"))  # Output: ['hey', 'the']

# \b  - Matches the boundary between a word character and a non-word character
# Example: r"\bcat\b" matches "cat" in "The cat sat"
print(re.findall(r"\bcat\b", "The cat sat on the mat."))  # Output: ['cat']

# \B  - Matches any position that is not a word boundary
# Example: r"\Bcat\B" matches "cat" in "category" but not in "The cat sat"
print(re.findall(r"\Bcat\B", "category and The cat sat"))  # Output: ['cat']

# Check if special sequences were found

# Find all occurrences of non-word characters in the text
import re

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches:", matches)

# Find all occurrences of a specified pattern within a string
import re

s2 = "The BodyGuard is the best album of 'Whitney Houston'."

result = re.findall("st", s2) # Use the findall() function to find all occurrences of the "st" in the string
print(result)

# The split_array contains all the substrings, split by whitespace characters
import re

s2 = "The BodyGuard is the best album of 'Whitney Houston'."

# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)


# Define the regular expression pattern to search for
pattern = r"Whitney Houston"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

# 8. Quiz on Strings
# Consider the variable g, and find the first index of the sub-string snow
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

g.find("snow")

# In the variable g, replace the sub-string Mary with Bob
print(g.replace("Mart", "Bob"))

# In the variable g, replace the sub-string , with .
print(g.replace(",", "."))

# In the variable g, split the substring to list
g.split()

# In the string s3, find whether the digit is present or not using the \d and search() function
s3 = "House number- 1105"

result = re.search(r"\d", s3)

if result:
    print("Digit Found.")
else:
    print("Digit not found.")

# In the string str1, replace the sub-string fox with bear using sub() function
str1= "The quick brown fox jumps over the lazy dog."

# The new_string contains the original string with the pattern replaced by the replacement string
pattern = r"fox"

replacement = "bear"

new_string = re.sub(pattern, replacement, str1, flags = re.IGNORECASE)
print(new_string)

# Use re.sub() to replace "fox" with "bear"
new_str1 = re.sub(r"fox", "bear", str1)
print(new_str1)

# In the string str2 find all the occurrences of woo using findall() function
# Use re.findall() to find all occurrences of "woo"
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

new_str2 = re.findall(r"woo", str2)
print(new_str2)

matches = re.findall(r"woo", str2)
print(matches)