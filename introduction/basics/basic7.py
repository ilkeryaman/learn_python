list1 = [1, 2, 3]
tuple1 = ((1, 2), (3, 4), (7, 7))
dict1 = {"name": "ilker", "age": 33}

for x in list1:
    print("Current item is", x)

for x, y in tuple1:
    print("x is {}, y is {}".format(x, y))

for x in dict1:
    print(x)

for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)

print(dict1)

for x in range(0, 5):
    print("x is " + str(x))

for x in range(0, 5, 2):
    print("x is " + str(x))

rng = range(0, 25, 5)
print(rng)
print(*rng)

for x in range(10):
    print("* " * x)

# => while loop
i = 4
while i > 0:
    print(i)
    i -= 1
else:
    print("End of while loop")
