
# !arithmentic operators
# + - * / // % **

# !assignment/augmented
# = += -= *= /= %= **=

# !comparison
# == != > < >= <=

# !logical
# and: both must be true
# or: atleast one is true
# not: reverse
# TODO: check truth table

# !bitwise
# & | ~ >> << ^
# TODO: practice bitwise operators

# !special operators: is/is not
# is: identical/refer to same object/check if located in same part of memory

x1 = 5
y1 = 5
print(x1 is y1)  # True

# equal/not identical/not located in same part in memory
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a is not b)  # True

# !membership operators: in/not in
str1 = "Hello World!"
dict1 = {"a": 1, "b": 2}
print("Hello" in str1)  # True
print("a" in dict1)  # True
print("WORLD" not in str1)  # False
