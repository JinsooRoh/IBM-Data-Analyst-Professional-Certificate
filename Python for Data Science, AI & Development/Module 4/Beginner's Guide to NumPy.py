# Creating NumPy arrays
# Creating 1D array
import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.

# Creating 2D array
import numpy as np

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Array attributes
# Array attributes
print(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# output : 2
print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# Output : (3, 3)
print(arr_2d.size) # size: Provides the total number of elements in the array.
# Output : 9

# Indexing and slicing
print(arr_1d[2])          # Accessing an element (3rd element)
print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)
print(arr_2d[1])          # Accessing a row (2nd row)
print(arr_2d[:, 1])       # Accessing a column (2nd column)

# Basic operations
# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9]

# Scalar multiplication
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]

# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]

"""
# Operation with NumPy
# Array Creation
arr = np.array([1, 2, 3, 4, 5])

# Element-Wise Arithmetic
result = arr1 + arr2

# Scalar Arithmetic
result = arr * 2

# Element-Wise Functions
result = np.sqrt(arr)

# Sum and Mean
total = np.sum(arr)<br>average = np.mean(arr)

# Maximum and Minimum Values
max_val = np.max(arr)<br>min_val = np.min(arr)

# Reshaping	
reshaped_arr = arr.reshape(2, 3)

# Transposition
transposed_arr = arr.T

# Matrix Multiplication
result = np.dot(matrix1, matrix2)

"""