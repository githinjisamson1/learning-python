

# !recursion
# function calling itself multiple times until a base condition is met

# !program to find the factorial of a number
numberToFindFactorial = int(input("Enter number: "))


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


print(f"{numberToFindFactorial}! = {factorial(numberToFindFactorial)}")


# !RecursionError: maximum depth of recursion is 1000
def recursor():
    recursor()


recursor()


# TODO:
# !advantages of recursion
# 1. Recursive functions make the code look clean and elegant.
# 2. A complex task can be broken down into simpler sub-problems using recursion.
# 3. Sequence generation is easier with recursion than using some nested iteration.

# !disadvantages of recursion
# 1. Sometimes the logic behind recursion is hard to follow through.
# 2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# 3. Recursive functions are hard to debug.
