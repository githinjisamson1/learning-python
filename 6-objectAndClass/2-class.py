
# !class: blueprint/template of an object

# !Access Class Attributes Using Objects
# define a class
class Bike:
    # class attributes
    name = ""
    gear = 0


# create object of class/instantiation
bike1 = Bike()

# access attributes and assign new values/dot notation
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


# !Create Multiple Objects of Python Class
# define a class
class Employee:
    # define a class attribute
    employee_id = 0


# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


# !Python Methods
# create a class
class Room:
    # class attributes
    length = 0.0
    breadth = 0.0

    # method to calculate area/instance method
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()


# !Python Constructors: __init__() constructor
# !always called upon creating each instance of a class
class Bike:

    # constructor function
    def __init__(self, name=""):
        self.name = name


bike1 = Bike("Mountain bike")
