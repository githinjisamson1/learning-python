
# TODO: !Execute as long as a condition is true/number of iterations is not known

# !display numbers from 1 to 5
i = 1
n = 5

while i <= n:
    print(i)
    i += 1

# !calculate sum of numbers until user enters 0
sum = 0
number = int(input("Enter number: "))

while number != 0:
    sum += number
    number = int(input("Enter number: "))

print(f"Sum is: {sum}")

# !!!infinite loop
# age = 20

# while age > 18:
#     print("You van vote")

# !with optional else block
# The else block will not execute if the while loop is terminated by a break statement.
counter = 0

while counter < 3:
    print('Inside loop')
    counter += 1
    
    # uncommenting will result in else block not executing
    # if counter == 2:
    #     break
else:
    print('Inside else/Runs when condition evaluates to false')
