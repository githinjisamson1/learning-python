

'''
In Python, we can change the way operators work for user-defined types.

This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.

For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.
'''

# !special functions
'''
Class functions that begin with double underscore

The special functions are defined by the Python interpreter and used to implement certain features or behaviors.

They are called "double underscore" functions because they have a double underscore prefix and suffix, such as __init__() or __add__().

'''

# !Example: + Operator Overloading in Python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

# Output: (3,5)

# !Overloading Comparison Operators


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age


p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False


# TODO: check on operator overloading
# Improves code readability by allowing the use of familiar operators.

# Ensures that objects of a class behave consistently with built-in types and other user-defined types.
# Makes it simpler to write code, especially for complex data types.

# Allows for code reuse by implementing one operator method and using it for other operators.

# operator overloading: how python works under the hood: here above we are adding/comparing two classes
# __add__ and __lt__ are called under the hood
# same operator different meaning according to context == operator overloading
