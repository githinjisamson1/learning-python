
# !global keyword
# we can only access the global variable but cannot modify it from inside the function.
# the solution for this is to use the global keyword.
c = 1


def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2

    print(c)


add()

# Output: 3


# !global in nested function
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)


outer_function()
print("Outside both function: ", num)

# !!!OUTPUT: all take effect after calling the outer function
# Before calling inner_function():  20
# After calling inner_function():  20
# Outside both function:  25
