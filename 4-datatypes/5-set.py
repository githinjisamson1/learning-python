
# !set
# collection of unique data
# unordered/unindexed/unique
# set can have any number of items and they may be of different types
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# !create
studentIds = {1, 2, 3, 4, 5}
print(type(studentIds))

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# !create empty set
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

# !a set cannot contain duplicates
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}

# !add/updated set items
# !add: add an item to set
numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers)

# !update: update set items with other collection types(lists, tuples, sets)
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# !remove an element from set: discard()
languages = {'Swift', 'Java', 'Python'}

print('Initial Set:', languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)


# !built-in fucntions with set
'''
all/any/enumerate/len/max/min/sorted/sum
'''

# !iterate over a set
studentIds = {1, 2, 3, 4, 5}

for item in studentIds:
    print(item)

print(len(studentIds))

# TODO: python set operations
# !union of two sets: A | B / A.union(B)
# The union of two sets A and B include all the elements of set A and B.

# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B))

# !set intersection: A & B / A.intersection(B) / A ⋂ B
# The intersection of two sets A and B include the common elements between set A and B.

# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# !difference between two sets: A - B / A.difference(B)
# The difference between two sets A and B include elements of set A that are not present on set B.

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# !set symmetric difference: A ^ B / A.symmetric_difference()
# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# !check if two sets are equal: have the same elements
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')


# TODO: !other set methods

# add/clear/copydifference/difference_update/discard
# intersection/intersection_update/isdisjoint/
# issubset/issuperset/pop/remove/symmetric_difference/union/update
