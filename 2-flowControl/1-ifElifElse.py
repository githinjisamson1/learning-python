
# TODO:
# !match...case for python 3.10
# !dictionary mapping in place of if...elif...else

# !if
number = 10

# check if number is greater than 0/can be on one line/only when having single if
if number > 0:
    print('Number is positive.')

print('The if statement is easy')

# !if...else
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

# !if...elif...else
score = int(input("Enter student score: "))


def examineScore(score):
    if (score > 50):
        print("Above average")
    elif (score == 50):
        print("Average")
    elif (score < 50):
        print("Below average")
    else:
        print("Invalid")


examineScore(score)

# !nested if statements
number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive
