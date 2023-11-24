

'''
# !package
A package is a container that contains various functions to perform specific tasks. For example, the math package includes the sqrt() function to perform the square root of a number.

We can separate our code into multiple files by keeping the related code together in packages.
This way we can also reuse our code

# !Importing module from a package
import Game.Level.start
Game.Level.start.select_difficulty(2)

# !Import Without Package Prefix
from Game.Level import start
start.select_difficulty(2)

#!Import Required Functionality Only: NOT RECOMMENDED
from Game.Level.start import select_difficulty
select_difficulty(2)

# !module vs package
TODO: A module in Python is a single file containing Python code.
t could be a script or a collection of functions, classes, and variables.
Suppose you have a file named math_operations.py, which contains functions for basic mathematical operations like addition, subtraction, multiplication, etc. 
This file is a module.

TODO: A package in Python is a way of organizing related modules into a directory hierarchy.
It contains an __init__.py file, which can be empty, to indicate that the directory should be treated as a package.
e.g., 
math_package/
├── __init__.py
├── math_operations.py


'''
