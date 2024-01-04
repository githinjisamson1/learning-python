
'''
Note:

When we are developing a large Python program, it is a good practice to place all the user-defined exceptions that our program raises in a separate file.

Many standard modules define their exceptions separately as exceptions.py or errors.py (generally but not always).

in customizing exception classes...
The inherited __str__ method of the Exception class is then used to display the corresponding message when SalaryNotInRangeError is raised.
'''

# !custom exceptions syntax
class CustomException(Exception):
    pass

try:
    pass
except CustomException:
    pass



# !example1
# inherit from Exception class
class InvalidAgeException(Exception):
    pass


number = 18

try:
    age = int(input("Enter age: "))

    if age < number:
        raise InvalidAgeException
    else:
        print("Eligible to vote!")

except InvalidAgeException:
    print("Invalid age!")

class SalaryNotInRangeException(Exception):
    pass

# !example 2
try:
    salary = int(input("Enter salary: "))
    
    if 5000 < salary <  15000:
        print(f"Salary {salary} is within range")
    else:
        raise SalaryNotInRangeException
except SalaryNotInRangeException:
    print(f"Salary {salary} is not within range!")


# !customizing exception classes
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary not in (5000, 15000) range"):
        self.salary=salary
        self.message=message
        super().__init__(self.message)
        
salary=int(input("Enter input salary: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
        
