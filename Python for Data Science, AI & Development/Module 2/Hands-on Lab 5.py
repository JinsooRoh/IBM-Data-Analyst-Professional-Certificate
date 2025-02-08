# Lists
# 1. Indexing
# Create a list
L = ["The Bodyguard", 7.0, 1992]

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3])
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2])
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1])

# 2. List Content
# Sample List
["The Bodyguard", 7.0, 1992, [1, 2], ("A", 1)]

# 3. List Operations
# Sample List
L = ["The Bodyguard", 7.0,1992,"BG",1]

# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
L

# Use append to add elements to list
L = [ "The Bodyguard", 7.0]
L.append(['pop', 10])
L

# Use extend to add elements to list
L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
L

# Use append to add elements to list
L.append(['a','b'])
L

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
'hard rock'.split()

# Split the string by comma(delimiter)
'A,B,C,D'.split(',')

# 3. Copy and Clone List
# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
B
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# 4. Scenario:Shopping List
# create a empty list for storing the items to buy in Shopping list
Shopping_list = []

# Store the number of items to the shopping_list
Shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
print(Shopping_list)

# Add a new item to the shopping_list
Shopping_list.append("Football")
print(Shopping_list)

Shopping_list.extend(["Football"])
print(Shopping_list)

"""
# Caution!
Shopping_list.extend("Football")  # Passing a String
print(Shopping_list)

Output = ['Watch', 'Laptop', 'Shoes', 'Pen', 'Clothes', 'F', 'o', 'o', 't', 'b', 'a', 'l', 'l']

"""

# Print First item from the shopping_list
print(Shopping_list[0])


# Print Last item from the shopping_list
print(Shopping_list[-1])

#Print the entire Shopping List
print(Shopping_list)

# Print the item that are important to buy from the Shopping List
print(Shopping_list[1:3])

# Change the item from the shopping_list
Shopping_list[3] = "Notebook"
print(Shopping_list)

# Delete the item from the shopping_list that is not required
del (Shopping_list[-2])
print(Shopping_list)

# Print the shopping list
print(Shopping_list)