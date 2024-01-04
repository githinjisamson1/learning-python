
# !namespace
# built-in namespace: upon start of interpreter
# global namespace: in module
# local namespace: in function

# define global variable/global namespace/in module
global_var = 10


def my_function():
    # define local variable/local namespace/in function
    local_var = 20

    # !modify global variable value/will rarely do so
    global global_var
    global_var = 30


# print global variable value
print(global_var)  # 10

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)  # 30
