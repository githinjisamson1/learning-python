
# !tuple
# collection of related items/can contain any data type
# ordered/indexed/immutable

# !create
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# !with one element: must have trailing comma
var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses is optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>

# !access
# indexing
studentIds = (1, 2, 3, 4, 5)
print(studentIds[0])

# negative indexing: -1 rep last item/element
# start index is inclusive
# end index is exclusive
print(studentIds[-1])

# !slicing
print(studentIds[1:4])


# !tuple methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

# !iterating through a tuple
studentIds = (20, 21, 22, 23, 24)

for item in studentIds:
    print(item)

# !check if item exists in tuple
languages = ["JavaScript", "Python", "Kotlin"]
print("JavaScript" in languages)

# TODO:  advantages of a tuple over a list
# 1. We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.

# 2. Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.

# 3. Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.

# 4. If you have data that doesn't change, implementing it as a tuple will guarantee that it remains write-protected.
