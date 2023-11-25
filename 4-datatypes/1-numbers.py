
import random
import math

# !numeric data type
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

# !number systems
# decimal: base 10
# binary: base 2/0b
# octal: base 8/0o
# hexadecimal: 0x

# !type conversion
# implicit: done autumatically
print(1 + 2.0)  # prints 3.0

# explicit: done manually
num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3)  # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

# !random module
# get random item from range
print(random.randrange(10, 20, 2))

# get random item from fruits 
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# shuffle fruits list
random.shuffle(fruits)
print(fruits)

# print random element
print(random.random())

# !math module
print(math.pi)
print(math.factorial(5))
print(math.log2(4))
print(math.exp(10))
