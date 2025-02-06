# 1. Types of objects in Python
# Integer
type(11)

# Float
type(2.14)

# String
type("Hello, Python 101!")

# 2. Integers
type(-1)
type(4)
type(0)

# 3. Floats
type(1.0)
type(0.5)
type(0.56)

#System settings about float type
import sys
sys.float_info

# 4. Converting from one object type to a different object type
float(2)
print(type(float(2)))
int(1.1)

# Convert a string into an integer with error
int('1 or 2 people')

# Convert the string "1.2" into a float
float('1.2')

# Convert an integer to a string
str(1)

# Convert a float to a string
str(1.2)

# 5. Boolean data type
type(True)
type(False)
int(True)
bool(1)
bool(0)
float(True)

# Exercise: Types
type(6/2)
type(6//2)
type("Hello, World!")
type("hello" == "world") 

int("1001")
float("1234.56")
str("123-456-7890")

print(6%2)
