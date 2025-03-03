# Classes and Objects in Python
# Creating a Class
# Import the library to draw the objects
import matplotlib.pyplot as plt

# Creating a class Circle
class Circle:

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

# Creating an instance of a class Circle
# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Can use the dir command to get a list of the object's methods.
dir(RedCircle)

# Can look at the data attribute radius 
# Print the object attribute radius
RedCircle.radius

# Print the object attribute color
RedCircle.color

# Can change the object's data attribute
# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

# Can draw the object by using the method drawCircle()
# Call the method drawCircle
RedCircle.drawCircle()

# Can increase the radius of the circle by applying the method add_radius().
# Use method to change the object attribute radius
print("Radius of object: ", RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attribute radius
BlueCircle.radius

# Print the object attribute color
BlueCircle.color

# Call the method drawCircle
BlueCircle.drawCircle()

# The Rectangle Class
# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attribute height
SkinnyBlueRectangle.height

# Print the object attribute width
SkinnyBlueRectangle.width

# Print the object attribute color
SkinnyBlueRectangle.color

# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Print the object attribute height
FatYellowRectangle.height

# Print the object attribute width
FatYellowRectangle.width

# Print the object attribute color
FatYellowRectangle.color

# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()

# Scenario: Car dealership's inventory management system
# Task-1. You are tasked with creating a Python program to represent vehicles using a class.
# Each car should have attributes for maximum speed and mileage.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Task-2. Update the class with the default color for all vehicles," white".
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

# Task-4. Create a method to display all the properties of an object of the class.
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_property(self):
        print("Properties of the Vehicles: ")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_property(self):
        print("Properties of the Vehicles: ")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

vehicle1 = Vehicle(200, 20)
vehicle1.seating_capacity(5)
vehicle1.display_property()

vehicle2 = Vehicle(180, 25)
vehicle2.seating_capacity(4)
vehicle2.display_property()