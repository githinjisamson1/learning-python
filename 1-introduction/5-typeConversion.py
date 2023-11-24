
# !implicit conversion: automatically done by python interpreter/small to large/avoids data loss
value1 = 5
value2 = 5.5
print(type(value1 + value2))  # float
print(value1 + value2)

# !explicit conversion: manual conversion/type casting/large to small/data may be lost
# int()/float()/str()
num1 = "5"
num2 = 4
castedNum1 = int(num1)
print(type(castedNum1))  # int
print(castedNum1 + 4)
