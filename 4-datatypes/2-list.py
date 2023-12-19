

# !list:
# collection of related/unrelated items
# ordered/indexed/mutable

# !create
fruits = ["apple", "banana", "cherry"]
ages = list((20, 21, 22, 23, 24))
print(type(fruits))
print(type(ages))

# !access
print(fruits[0])

# negative index: -1 rep last item/element
print(ages[-1])

# IndexError: does not exist
# print(fruits[20])

# !slicing of a list: ":" operator
# start index is inclusive
# end index is exclusive

vowels = ["a", "e", "i", "o", "u"]
print(vowels[1:4])
print(vowels[2:])
print(vowels[:4])
print(vowels[0:4:2])
print(vowels[:])

# !add elements to a list
# append(): add item at end of list
numbers = [21, 34, 54, 12]
numbers.append("One")
print(numbers)

# extend(): add all items of an iterable/extend a list/array
numbers = [2, 4, 6]
oddNumbers = [1, 3, 5]
numbers.extend(oddNumbers)
print(numbers)

# insert: insert item at specified index
numbers = [10, 30, 40]
numbers.insert(0, 5)
print(numbers)


# !change list items: mutable
languages = ['Python', 'Swift', 'C++']

# changing the third item to 'JavaScript'
languages[2] = 'JavaScript'

print(languages)  # ['Python', 'Swift', 'JavaScript']

# !remove an item from a list
# del
fruits = ["apple", "banana", "cherry", "mango", "orange"]
# del fruits[3]
# del fruits[-1]
# del fruits[1:4]
# print(fruits)


# remove
fruits.remove("mango")
# print(fruits)

# TODO: check on list methods
'''
append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy
'''

# !iterating through a list
fruits = ["apple", "banana", "cherry"]

for item in fruits:
    print(item)

# !check if element exists in list
print("apple" in fruits)


# !size/length
print(len(fruits))

# !list comprehension
# List comprehension is a concise and elegant way to create lists
# shortens for loop to a single line
# e.g.,

numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)


numbers2 = [item for item in range(10)]
print(numbers2)


# e.g 2 .,
numbers = []

for n in range(1, 6):
    numbers.append(n**2)

numbers = [n**2 for n in range(1, 6)]

print(numbers)
