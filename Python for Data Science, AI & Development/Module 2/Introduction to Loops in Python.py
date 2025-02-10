# Main Types of Loops
# 1. For Loops
# for val in sequence:
      # statement(s) to be executed in sequence as a part of the loop.

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)

# Range Function
for number in range(1, 11):
    print(number)

for number in range(11):
    print(number)

# The Enumerated For Loop
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

# Without Enumerated For Loop
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):  
    print(f"At position {i}, I found a {fruits[i]}")

# While Loops
# while condition:
    # Code to be executed while the condition is true
    # Indentation is crucial to indicate the scope of the loop
count = 1
while count <= 10:
    print(count)
    count += 1

