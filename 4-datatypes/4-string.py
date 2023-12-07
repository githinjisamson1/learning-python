
# !string
# sequence of characters enclosed in double quotes

# create a string using double quotes
string1 = "Python programming"

# create a string using single quotes
string1 = 'Python programming'

# !access
greet = 'hello'

# access 1st index element
print(greet[1])  # "e"

# negative indexing
greet = 'hello'

# access 1st index element
print(greet[1])  # "e"

# !slicing
greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

# !strings are immutable: TypeError
# However, we can assign the variable name to a new string.
# message = 'Hola Amigos'
# message[0] = 'H'
# print(message)

# !multiline string: docstring
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)


# !compare two strings
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

# !join two or more strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# Output: Hello, Jack

# !iterate through a string
greet = "Hello"

for item in greet:
    print(item)

print(len(greet))


# !string membership test
print("H" in greet)
print("z" not in greet)

# TODO: check string methods
'''

upper/lower/partition/replace/find/rstrip/split/startswith/isnumeric/index

'''

# !escape sequences
# \\	Backslash
# \'	Single quote
# \"	Double quote
# \a	ASCII Bell
# \b	ASCII Backspace
# \f	ASCII Formfeed
# \n	ASCII Linefeed
# \r	ASCII Carriage Return
# \t	ASCII Horizontal Tab
# \v	ASCII Vertical Tab
# \ooo	Character with octal value ooo
# \xHH	Character with hexadecimal value HH

# !string formatting
# f-strings
name = 'Cathy'
country = 'UK'

print(f'{name} is from {country}')

# using format()
print('{} is from {}'.format(name, country))
