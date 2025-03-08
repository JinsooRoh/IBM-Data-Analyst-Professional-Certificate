# 2D Numpy in Python
# Create a 2D Numpy Array

# Import the libraries
import numpy as np

# Consider the list a, which contains three nested lists each of equal size.
# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# We can cast the list to a Numpy Array as follows:
# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A

# We can use the attribute ndim to obtain the number of axes or dimensions, referred to as the rank.
# Show the numpy array dimensions
A.ndim

# Attribute shape returns a tuple corresponding to the size or number of each dimension.Attribute shape returns a tuple corresponding to the size or number of each dimension.
# Show the numpy array shape
A.shape

# The total number of elements in the array is given by the attribute size.
# Show the numpy array size
A.size

# Basic Operations
# The process is identical to matrix addition. Matrix addition of X and Y is shown in the following figure:
# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y
Z = X + Y
Z

# Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler.
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2
Z = 2 * Y
Z

# Multiplication of two arrays corresponds to an element-wise product or Hadamard product.
# We can perform element-wise product of the array X and Y as follows:
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Multiply X with Y
Z = X * Y
Z

# We can also perform matrix multiplication with the numpy arrays A and B as follow:
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B

# We use the numpy function dot to multiply the arrays together.
# Calculate the dot product
Z = np.dot(A,B)
Z

# Calculate the sine of Z
np.sin(Z)

# We use the numpy attribute T to calculate the transposed matrix
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C
C.T

# Quiz on 2D Numpy Array
# Write your code below and press Shift+Enter to execute
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A

# Calculate the numpy array size.
A.size

# Access the element on the first row and first and second columns.
A[0][0:2]

# Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
X = np.dot(A, B)
X
