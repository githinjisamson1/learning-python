
# !pass: we are telling the interpreter
# !that we will implement some code block later
# !interpreter ignores comment but not pass

number1 = 10

if number1 < 20:
    pass


def exampleFunction():
    pass


class ExampleClass:
    pass

# !Indentation error
# if number1 < 20:
#     # will execute later
