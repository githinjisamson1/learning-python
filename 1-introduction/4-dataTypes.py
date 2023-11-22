
# !DataTypes/Classes
# Numeric/int, float, complex
# String/str
# Sequence/list, tuple, range
# Mapping/dict
# Set/set, frozeenset
# Boolean/bool

# !everything in python is an object
# hence data types are actually classes &
# variables are instances of these classes
# hence can use constructor or literal to create them

# Numbers
num1 = 1
num2 = 2.5
num3 = 2+3j
print(type(num1), type(num2), type(num3))

# list: ordered/similar or different items/[]
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
print(fruits[0])

# tuple: ordered/immutable/cannot be modified/()
product = ("Microsoft", "X-box", 500)
print(product[0])
print(type(product))

# str: ""
name = "John Doe"
print(name)
print(type(name))

# set: unordered/unique/{}
studentIds = {1, 2, 3, 4, 5}
print(studentIds)
print(type(studentIds))

# dict: ordered/key-value pairs
student = {"name": "John Doe", "age": 21, "gender": "male"}
print(student["name"])
print(student.get("name"))
# print(student.get("score")) # None
print(type(student))
