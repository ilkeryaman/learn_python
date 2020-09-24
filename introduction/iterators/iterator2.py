"""
Generators (Generator functions):
Not consuming memory
"""


def get_square():
    for x in range(1, 5):
        yield x ** 2


iterator = iter(get_square())
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Iteration is stopped!")

# => for loop automatically catches StopIteration exception and breaks
iterator = iter(get_square())
print("Start of first iterator loop:")
for i in iterator:
    print(i)

print("Start of second iterator loop:")
for i in iterator:
    print(i)
