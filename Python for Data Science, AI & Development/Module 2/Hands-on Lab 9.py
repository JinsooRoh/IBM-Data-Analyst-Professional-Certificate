# Condition Statements
# 1. Comparison Operators
# Condition Equal
a = 5
a == 6 # The result is False, as 5 does not equal to 6.

# Greater than Sign
i = 6
i > 5 # i is equal to 6, because 6 is larger than 5, the output is True.

# Greater than Sign
i = 2
i > 5 # The statement is False as 2 is not greater than 5

# Inequality Sign
i = 2
i != 6 # Following condition will produce True as long as the value of i is not equal to 6

# Inequality Sign
i = 6
i != 6 # i equals 6 the inequality expression produces False

# Use Equality sign to compare the strings
"ACDC" == "The Bodyguard" # As the strings are not equal, we get a False.

# Use Inequality sign to compare the strings
"ACDC" != "The Bodyguard" # The output is going to be True as the strings are not equal.

"""
ASCII Table
    'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74,
    'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
    'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106,
    'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116,
    'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122

"""

# Compare characters
'B' > 'A'

# Compare characters
'BA' > 'AB' # When there are multiple letters, the first letter takes precedence in ordering

# 2. Branching
# If statement example
age = 19
# age = 18

# expression that can be true or false
if age > 18:
    
    # within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

# The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example
age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# Elif statment example
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example
album_year = 1983
# album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')

# Condition statement example
album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# 3. Logical operators
# Condition statement example
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example
album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# The not statement checks if the statement is false
# Condition statement example
album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")

# 4. Quiz on Conditions
# Write a Python program to check if a player Lionel Messi has more than 10 achievements.
player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} plays {sport} and has {achievements} achievements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")

# Write a Python program to check if a player belongs to the sport Tennis or has exactly 20 achievements.
player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if  sport == "tennis" or achievements == 20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achivements.")
else:
    print(f"{player_name} does not meet the criteria.")

# Write a Python program to check if a player has less than 10 achievements and does not play Soccer.
player_name = "Usain Bolt"
sport = "Athletics"
achievements = 8

if sport != "Soccer" and achievements < 10:
    print(f"{player_name} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")

