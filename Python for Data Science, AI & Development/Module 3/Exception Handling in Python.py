# Common Exceptions in Python
# 1. ZeroDivisionError
# This error arises when an attempt is made to divide a number by zero.
result = 10 /0
print(result)
# Raises ZeroDivisionError

# 2. ValueError
# This error occurs when an inappropriate value is used within the code.
num = int("abc")
# Raises ValueError

# 3. FileNotFoundError
# This exception is encountered when an attempt is made to access a file that does not exist.
with open("nonexistent_file.txt", "r") as file:
        content = file.read()
# Raises FileNotFoundError

# 4. Index Error
# An IndexError occurs when an index is used to access an element in a list that is outside the valid index range.
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError

# 5. KeyError
# The KeyError arises when an attempt is made to access a non-existent key in a dictionary.
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError

# 6. TypeError
# The TypeError occurs when an object is used in an incompatible manner.
result = "hello" + 5   
# Raises TypeError

# 7. AttributeEror
# An AttributeError occurs when an attribute or method is accessed on an object that doesn't possess that specific attribute or method.
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError

# 8. ImportError
# This error is encountered when an attempt is made to import a module that is unavailable.

# Handling Exceptions
# Try and Except: Use the try and except blocks to prevent your program from crashing due to exceptions.
# using Try-except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")
