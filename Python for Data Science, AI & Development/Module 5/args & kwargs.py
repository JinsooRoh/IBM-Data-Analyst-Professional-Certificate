# In Python, *args and **kwargs are used to handle a variable number of arguments in functions.

# === *args ===
# *args stands for "arguments" and is used to pass a variable number of positional arguments to a function.
# Inside the function, *args is treated as a tuple, allowing access to all positional arguments passed.
# This is useful when you don't know in advance how many arguments will be provided.

def sum_numbers(*args):
    # The *args parameter collects all positional arguments into a tuple.
    # The sum() function adds all elements in the tuple.
    return sum(args)

# Call the function with multiple arguments.
print(sum_numbers(1, 2, 3))  # Output: 6
# Here, *args becomes (1, 2, 3), and sum(args) computes 1 + 2 + 3 = 6.

# === **kwargs ===
# **kwargs stands for "keyword arguments" and is used to pass a variable number of keyword arguments to a function.
# Inside the function, **kwargs is treated as a dictionary, allowing access to all keyword arguments by their keys and values.
# This is helpful when you want to pass named arguments dynamically, especially when the arguments may vary.

def greet(**kwargs):
    # The **kwargs parameter collects all keyword arguments into a dictionary.
    # Loop through the dictionary to access each key-value pair.
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments.
greet(name="Alice", age=25)
# Output: 
# name: Alice
# age: 25
# Here, **kwargs becomes {'name': 'Alice', 'age': 25}, and the loop prints each key-value pair.

# === Combining *args and **kwargs ===
# *args and **kwargs can be used together in a function definition.
# *args handles positional arguments (as a tuple), while **kwargs handles keyword arguments (as a dictionary).
# When used together, *args must come before **kwargs in the parameter list due to Python's syntax rules.

def func(*args, **kwargs):
    # Print the tuple of positional arguments.
    print("args:", args)
    # Print the dictionary of keyword arguments.
    print("kwargs:", kwargs)

# Call the function with both positional and keyword arguments.
func(1, 2, name="Alice", age=25)
# Output:
# args: (1, 2)
# kwargs: {'name': 'Alice', 'age': 25}
# Here, positional arguments 1 and 2 are packed into *args as a tuple (1, 2),
# and keyword arguments name="Alice" and age=25 are packed into **kwargs as a dictionary.

# === Summary ===
# *args and **kwargs make Python functions flexible and adaptable to various situations.
# They are powerful tools for handling dynamic inputs, whether the number or type of arguments is unknown in advance.