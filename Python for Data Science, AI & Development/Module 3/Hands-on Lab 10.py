# Loops
# 1. Range
# Use the range
range(3)
range(0,3)

# 2. What is for loop?
# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     

# Example of for loop
for i in range(0, 8):
    print(i)

# Exmaple of for loop, loop through list
dates = [1982,1980,1973]

for year in dates:  
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# 3. What is while loop?
# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    
print("It took ", i ,"repetitions to get out of loop.")

# 4. Quiz on Loops
# Write a for loop that prints out all the elements between -5 and 5 using the range function.
for i in range(-4, 5):
    print(i)

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'].
Genres= [ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares= ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]

while(i < len(PlayListRatings) and Rating >= 6):
    print(f"Index: {i}, Rating: {Rating}")
    print(Rating) 
    Rating = PlayListRatings[i]
    i = i + 1

"""
# Case 1: With 'i < len(PlayListRatings)'
while (i < len(PlayListRatings) and Rating >= 6):
    # Ensures that 'i' does not exceed the valid index range of PlayListRatings  
    # Prevents 'IndexError' (list index out of range)  
    # Safely stops the loop when reaching the end of the list  

# Case 2: Without 'i < len(PlayListRatings)'
while (Rating >= 6):  
    # Does NOT check if 'i' is within the valid index range  
    # If 'i' exceeds the length of PlayListRatings, an 'IndexError' will occur  
    # May cause the program to crash when trying to access an invalid index  

"""

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange'
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while (i < len(squares) and squares[i] == "orange"):
    print(f"Index: {i}, Square: {squares[i]}") 
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)
