
# !inheritance syntax
# define a superclass
class super_class:
    # attributes and method definition
    pass

# inheritance
class sub_class(super_class):
    # attributes and method of super_class
    # attributes and method of sub_class
    pass


# !inheritance e.g.,
class Animal:

    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()

# !is-a relationship
# we use inheritance only if there exists an is-a relationship between two classes e.g., 
# Car is a Vehicle
# Apple is a Fruit
# Cat is an Animal

# !e.g., 2


class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : "))
                      for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()

# !method overriding: method in the subclass overrides the method in the superclass


class Animal:

    # attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")

# inherit from Animal


class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

# !super()
# Both the overridden and the superclass version of the eat() method is executed.


class Animal:

    name = ""

    def eat(self):
        print("I can eat")

# inherit from Animal


class Dog(Animal):

    # override eat() method
    def eat(self):

        # call the eat() method of the superclass using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()


# TODO: uses of inheritance
# Since a child class can inherit all the functionalities of the parent's class, this allows code reusability.

# Once a functionality is developed, you can simply inherit it. No need to reinvent the wheel. This allows for cleaner code and easier to maintain.

# Since you can also add your own functionalities in the child class, you can inherit only the useful functionalities and define other required features.
