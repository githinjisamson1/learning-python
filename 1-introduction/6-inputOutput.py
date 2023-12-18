
# !actual syntax
# print(object= separator= end= file= flush=)
# object: values to be printed
# sep: separator/.
# end: add specific values/ \n
# file: where to be printed
# flush: output is flushed/buffered?


# with object param: adds newline character automatically
print("Hello World!")

# with end param: does not add newline character automatically
print("Hello", end="! ")
print("World")

# with sep param
print("Hello", "John", sep=".")

# !also
# We can also use the print() function to print Python variables
# We can also join two strings together inside the print() statement/+

# !output formatting
x = 5
y = 10
print("Numbers are {} and {}".format(x, y))

# !input
num1 = int(input("Enter number: "))  # type casting
print(f"Number entered is: {num1}")
# print("Number entered is: {}".format(num1))
