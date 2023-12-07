
# !dictionary
# collection of related items stored as key-value pairs
# Dictionary keys must be immutable, such as tuples, strings, integers, etc
# We cannot use mutable (changeable) objects such as lists as keys.

student = {
    "name": "John",
    "age": 21,
    "gender": "male"
}

print(type(student))

# !Valid dictionary
my_dict = {
    1: "Hello",
    (1, 2): "Hello Hi",
    3: [1, 2, 3]
}

# !Invalid dictionary: unhashable
# Error: using a list as a key is not allowed
# my_dict = {
#     1: "Hello",
#     [1, 2]: "Hello Hi",
# }


# !dict() constructor to create dictionary
countryCapitals = dict({"Kenya": "Nairobi", "Uganda": "Kampala"})

print(countryCapitals)
print(type(countryCapitals))

# !size/length
print(len(countryCapitals))

# !access
print(countryCapitals["Kenya"])
print(countryCapitals.get("Uganda"))
print(countryCapitals.get("Tanzania"))  # None

# !change dictionary items/mutable
student = {
    "name": "John",
    "age": 21,
    "gender": "male"
}

student["name"] = "John Doe"
print(student)


# !add items to a dictionary
student["school"] = "Jkuat"
print(student)

student.update({"position": "class rep"})
print(student)


# !remove dictionary items
del student["position"]
print(student)

student.pop("age")
print(student)

student.clear()
print(student)

# TODO: check dictionary methods
'''
pop/update/clear/keys/values/get/popitem/copy
'''


# !membership test
countryCapitals = {"Kenya": "Nairobi",
                   "Uganda": "Kampala", "Tanzania": "Dar er Salaam"}

print("Kenya" in countryCapitals)
print("Sudan" not in countryCapitals)

# !iterate over a dictionary
for item in countryCapitals:
    print(item)
