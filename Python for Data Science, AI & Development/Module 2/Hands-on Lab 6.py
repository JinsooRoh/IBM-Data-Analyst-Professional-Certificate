# 1. Tuples
# Create first tuple
tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created
type(tuple1)

# 2. Indexing
# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
tuple1[-1]

# Use negative index to get the value of the second last element
tuple1[-2]

# Use negative index to get the value of the third last element
tuple1[-3]

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2

# 3. Slicing
# Slice from index 0 to index 2
tuple2[0:3]

# Slice from index 3 to index 4
tuple2[3:5]

# Get the length of tuple
len(tuple2)

# 4. Sorting
# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted

# 5. Nested Tuple
# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples
NestedT[2][1][0]

# Print the second element in the second nested tuples
NestedT[2][1][1]

# Print the first element in the second nested tuples
NestedT[4][1][0]

# Print the second element in the second nested tuples
NestedT[4][1][1]

# 6. Quiz on Tuples
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

# Find the length of the tuple, genres_tuple
len(genres_tuple)

# Access the element, with respect to index 3
genres_tuple[3]

# Use slicing to obtain indexes 3, 4 and 5
genres_tuple[3:6]

# Find the first two elements of the tuple genres_tuple
genres_tuple[:2]

# Find the index of 's' in "disco"
"disco".find('s')

# Generate a sorted List from the Tuple C_tuple=(-5, 1, -3)
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
C_list