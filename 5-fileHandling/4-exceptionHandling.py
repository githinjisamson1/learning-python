
# exception handling
try:
    numerator = 1
    denominator = 0
    print(numerator/denominator)
    
except ZeroDivisionError:
    print("Attempt to divide number by zero!")
    
finally:
    print("Finally will always execute!")


# catching specific exceptions
try:
    even_numbers = [2, 4, 6]
    print(even_numbers[5])
    
except ZeroDivisionError:
    print("Attempt to divide number by zero!")
    
except IndexError:
    print("Index out of bound!")

# try with else clause
# program to find reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    # True/False: False raises an AssertionError
    assert num % 2 == 0
    
except:
    print("Not an even number!")
    
else:
    # run code if try runs without any errors.
    reciprocal = 1/num
    print(reciprocal)
