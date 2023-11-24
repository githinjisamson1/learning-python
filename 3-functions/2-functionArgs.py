

# !args
def add(a, b):
    return a + b


print(add(1, 2))


# !with default args
def findProduct(item1=3, item2=5):
    return item1 * item2


print(findProduct())


# !with keyword/named arg
def displayInfo(firstname, lastname):
    print(f"First name: {firstname}")
    print(f"Last name: {lastname}")


displayInfo(lastname="Doe", firstname="John")


# !with arbitrary args/unknown number of args
def findSum(*numbers):
    result = 0

# numbers behaves as an array hence can iterate
    for item in numbers:
        result += item

    print(f"Sum is: {result}")


findSum(1, 2, 3, 4, 5)
