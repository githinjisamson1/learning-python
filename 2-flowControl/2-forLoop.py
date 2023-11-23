
# TODO: !Execute a specified numbers of times/number of iterations is known

# !with list
fruits = ['apple', "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# !with string
name = "John"

for item in name:
    print(item)


# !with range: counting starts from 0
# define a range containing 0, 1, 2, 3
values = range(4)

for i in values:
    print(i)

# !not using items in sequence in loopy body
# _ denotes will not be used in loopy body
for _ in fruits:
    print("Hello")
    print("Hi")


# !with optional else block
digits = [1, 2, 3, 4, 5]

for i in digits:
    print(i)
else:
    print("No items left")
