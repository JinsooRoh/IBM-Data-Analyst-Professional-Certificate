# 1. Consider a function named calculate_total that takes two numbers as input (parameters), adds them together, and then produces the sum as the output.
def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12

# 2. Python's built-in functions
# len(): Calculates the length of a sequence or collection
string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])   # Output: 5

# sum(): Adds up the elements in an iterable (list, tuple, and so on)
total = sum([10, 20, 30, 40, 50])  # Output: 150

# max(): Returns the maximum value in an iterable
highest = max([5, 12, 8, 23, 16])  # Output: 23

# min(): Returns the minimum value in an iterable
lowest = min([5, 12, 8, 23, 16])  # Output: 5

# 3. Defining your functions
def function_name():
    pass
"""
A "pass" statement in a programming function is a placeholder or a no-op (no operation) statement.
Use it when you want to define a function or a code block syntactically but do not want to specify any functionality or implementation at that moment.

1. Placeholder: "pass" acts as a temporary placeholder for future code that you intend to write within a function or a code block.
2. Syntax Requirement: In many programming languages like Python, using "pass" is necessary when you define a function or a conditional block.
It ensures that the code remains syntactically correct, even if it doesn't do anything yet.
3. No Operation: "pass" itself doesn't perform any meaningful action.
When the interpreter encounters “pass”, it simply moves on to the next statement without executing any code.

"""

# Function Parameters
def greet(name):
    print("Hello, " + name)

result = greet("Alice")
print(result)  # Output: Hello, Alice
"""
1. Parameters are like inputs for functions
2. They go inside parentheses when defining the function
3. Functions can have multiple parameters

"""

# Docstrings (Documentation Strings)
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)
"""
1. Docstrings explain what a function does
2. Placed inside triple quotes under the function definition
3. Helps other developers understand your function

"""

# Return statement
def add(a, b):
    return a + b

sum_result = add(3, 5)  # sum_result gets the value 8
"""
1. Return gives back a value from a function
2. Ends the function's execution and sends the result
3. A function can return various types of data

"""

# 4. Understanding scopes and variables
# Global Scope: Variables defined outside functions; accessible everywhere
# Local Scope: Variables inside functions; only usable within that function

# Part 1: Global variable declaration
global_variable = "I'm global"

# Part 2: Function definition
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

# Part 3: Function call
example_function()

# Part 4: Accessing global variable outside the function
print(global_variable)  # Accessible outside the function

# Part 5: Attempting to access local variable outside the function
# print(local_variable)  # Error, local variable not visible here

# 5. Using functions with loops
# Functions and loops together
"""
1. Functions can contain code with loops
2. This makes complex tasks more organized
3. The loop code becomes a repeatable function

"""
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)

print_numbers(5)  # Output: 1 2 3 4 5

# Enhancing code organization and reusability
"""
1. Functions group similar actions for easy understanding
2. Looping within functions keeps code clean
3. You can reuse a function to repeat actions

"""
def greet(name):
    return "Hello, " + name

for _ in range(3):
    print(greet("Alice"))

# 6. Modifying data structure using functions
# Part 1: Initialize an empty list
# Define an empty list as the initial data structure
my_list = []

# Part 2: Define a function to add elements
# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

# Part 3: Define a function to remove elements
# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

# Part 4: Add elements to the lis
my_list = []

def add_element(data_structure, element):
    data_structure.append(element)

# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

# Part 5: Print the current list
# Print the current list
print("Current list:", my_list)

# Part 6: Remove elements from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list

# Part 7: Print the updated list
# Print the updated list
print("Updated list:", my_list)