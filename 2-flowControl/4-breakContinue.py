
# !break: exit current iteration
for i in range(4):
    if i == 2:
        break
    print(i)

# find first multiples of 6
i = 1

while i <= 10:
    print(f"6 * {i} = {6 * i}")

    if i >= 5:
        break
    i += 1

# !continue: skip current iteration
for i in range(4):
    if i == 2:
        continue
    print(i)


# print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
