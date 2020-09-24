# => Lambda functions for small operations
multiply = lambda a, b: a * int(b)

print(multiply(2, 3))

try:
    print(multiply(3, "y"))
except ValueError:
    print("A ValueError is thrown.")
finally:
    print("Finally block is executed.")
