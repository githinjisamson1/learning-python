

# TODO: modules
'''
keep code CLEAN!REUSABLE!MODULAR!
Instead of putting everything in a single file, 
we can use modules to separate codes in separate files as per their functionality. 
This makes our code organized and easier to maintain.
'''


# !import module
import example
# import math

# !import with renaming
import math as m

# !from...import
# from math import sqrt

# !import all names: bad practice/can lead to duplicate definitions/hampers readability
# imports all definitions from math module
# except those starting with underscore/private definitions
from math import *



# !module usage
print(example.add(1, 2))
# print(math.pi)
print(m.pi)
print(sqrt(36))
print(example.__name__)

# declare
number1 = 1

# !dir(): list all definitions
print(dir())
