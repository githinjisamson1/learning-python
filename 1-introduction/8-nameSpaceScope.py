
# !namespace
# built-in namespace: upon start of python interpreter
# global namespace: module
# local namespace: function

# define global variable/global namespace
global_var = 10


def my_function():
    # define local variable/local namespace
    local_var = 20

    # !modify global variable value
    global global_var
    global_var = 30


# print global variable value
print(global_var)  # 10

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)  # 30

