
import math

# TODO: function
# a routine that takes in one or more args and returns a single value
# performs a specific task
# types: library(built-in), user-defined

# !program to addTwoNumbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def addTwoNumbers(a, b):
    return a + b


print(f"Sum of {num1} and {num2} is: {addTwoNumbers(num1, num2)}")

# !program to convert celsius to fahrenheit
celsius = float(input("Enter celsius temperature: "))


def fahEquivalent(celsius):
    return 1.8 * celsius + 32


print(f"{celsius} C: {fahEquivalent(celsius)} F")

# !recursion
# !program to find the factorial of a number

numberToFindFactorial = int(input("Enter number: "))


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(f"{numberToFindFactorial}! = {factorial(numberToFindFactorial)}")

# !keyword/named arguments
addTwoNumbers(a=1, b=2)

# !library functions: built-in
print(f"Square root of 4: {math.sqrt(4)}")
print(f"2 to the power of 3: {pow(2, 3)}")

# TODO: benefits of using functions
# code reusable
# We can use the same function multiple times in our program which makes our code reusable

# code readability
# Functions help us break our code into chunks to make our program readable and easy to understand
