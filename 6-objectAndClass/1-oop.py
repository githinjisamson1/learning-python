
# !pillars of oop
# 1. inheritance: child class derives attributes/xtics from the parent class/child class can have its own attributes/can override
# 2. encapsulation: bundling of data/data hiding
# 3. abstraction: hiding away the difficult parts/implementing important details
# 4. polymorphism: an object having more than one form

# attributes: variables inside a class
# methods: functions inside a class

class Parrot:
    # attributes
    name = ""
    age = None


# instantiation
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

# !inheritance: child class deriving attributes from the parent class

# base/parent class
class Animal:
    def eat(self):
        print("I an eat!")

    def sleep(self):
        print("I can sleep!")


# derived/child class
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof! Woof!")


# derived/child class
class Cat(Animal):
    def meow(self):
        print("I can meow! Meow! Meow!")


# !instantiation/creating objects
dog1 = Dog()
dog1.eat()
dog1.sleep()
dog1.bark()


# !encapsulation: bundling of data
class Computer:

    def __init__(self):
        # private attribute/use underscore or double underscore
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

# change price using setter
    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price/cannot change since __maxprice is private
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# !polymorphism: object having more than one form
# render() is polymorphic
class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")


class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")


class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")


# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()


# TODO:
# Object-Oriented Programming makes the program easy to understand as well as efficient.
# Since the class is sharable, the code can be reused.
# Data is safe and secure with data abstraction.
# Polymorphism allows the same interface for different objects, so programmers can write efficient code.