
'''
An exception is an unexpected event that occurs during program execution.
Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.

For instance, they occur when we:

try to open a file(for reading) that does not exist (FileNotFoundError)
try to divide a number by zero (ZeroDivisionError)
try to import a module that does not exist (ImportError) and so on.

Whenever these types of runtime errors occur, Python creates an exception object.

Errors represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.

Errors are usually beyond the control of the programmer and we should not try to handle errors.

Exceptions can be caught and handled by the program.

Types of exceptions:
1. built-in exceptions
2. user-defined exceptions
'''

# !system ZeroDivisionError
divide_numbers = 7/0
print(divide_numbers)

# !view all built-in exceptions using locals()
# invoke locals then access using bracket notation
print(dir(locals()['__builtins__']))
