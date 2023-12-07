

# !local variable: inside function
def greet():

    # local variable
    message = 'Hello'

    print('Local', message)


greet()

# try to access message variable
# outside greet() function
# print(message/)


# !global variable: inside module/file we are currently in 
# declare global variable
message = 'Hello'


def greet():
    # !declare local variable
    print('Local', message)


greet()
print('Global', message)

# !non-local variable: in nested function/neither local nor global
# outside function


def outer():
    message = 'local'

    # nested function
    def inner():

        # !declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)


outer()
