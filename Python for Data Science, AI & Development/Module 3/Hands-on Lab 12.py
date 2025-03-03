# Exception Handling
# What is na Exception?
# An exception is an error that occurs during the execution of code.
# This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.

1/0
# ZeroDivisionError occurs when you try to divide by zero.
"""
y = a + 5
# NameError -- in this case, it means that you tried to use the variable a when it was not defined.
"""

a = [1, 2, 3]
a[10]
# IndexError -- in this case, it occured because you tried to access data from a list using an index that does not exist for this list.
"""
# potential code before try catch
try:
    # code to try to execute
except:
    # code to execute if there is an exception
# code that will still execute if there is an exception

# For example if we divide by zero. Try running the following block of code with b as a0 number.
# An exception will only be raised if b is zero.
"""

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")

"""
# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception   
# code that will execute if there is no exception or a one that we are handling

"""

# Except Specific Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
        
"""
# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception 
# code that will execute if there is no exception or a one that we are handling

"""

# Try Except Else Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

"""
# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
# code that will execute if there is no exception or a one that we are handling

"""


# Try Except Else and Finally Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

# Practice Exerccies
# Excercise 1: Handling ZeroDivisionError
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("The number you provided can\'t divide 1 because it is 0.")
        return None
try:
    numerator = int(input("Please enter a number you want to divide: "))
    denominator = int(input("Please enter a number you want to divide by: "))
    print(safe_divide(numerator, denominator))
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Excercise 2: Handling ValueError
import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        return "Error: Invalid input! Please enter a positive integer or a float value."

try:
    number1 = float(input("Plase enter a number you want to calculate: "))
    print(perform_calculation(number1))
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Excercise 3: Handling Gerneric Exceptions
def complex_calculation(num):
    try:
        result = num / (num - 5)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except Exception as e:
        return f"An unexpected error occured: {e}"

try:
    num = int(input("Plase enter a number you want to calculate: "))
    print(complex_calculation(num))
except ValueError:
    print("Invalid input! Please enter a valid integer.")