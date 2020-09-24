from functools import reduce

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]

print(list(map(lambda a: a * 2, list1)))
print(list(filter(lambda a: a % 2 == 0, list1)))
print(reduce(lambda a, b: a + b, list1))
print(list(zip(list1, list2)))
print(list(enumerate(list2)))

for x in enumerate(list2):
    if x[0] % 2 == 0:
        continue
    print(x[1])

print(any(x > 2 for x in list1))
print(all(x > 2 for x in list1))
