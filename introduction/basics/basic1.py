# => Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print("a + b = %d" % (a+b))

# => This will not work!
"""
# one, two, hello = 1, 2, "hwllo"
# print(one + two + hello)
"""

# => Python swap
a, b = b, a
print("a = %d" % a)
print("b = %d" % b)

# => * Using two multiplication symbols makes a power relationship.
squared = 7 ** 2
cubed = 2 ** 3
square_root = 9 ** 0.5
print("squared = %d" % squared)
print("cubed = %d" % cubed)
print("square root = %d" % square_root)

# => To use two or more argument specifiers, use a tuple (parentheses):
print("%s is %d years old" % ("Ilker", 33))

# => In Python, a string can be created by three quote
print('''This is a three quoted string!''')

# => Python has an integer division operator: //
print(5 / 2)
print(5 // 2)

""" => Here are some basic argument specifiers you should know:
    %s - String (or any object with a string representation, like numbers)
    %d - Integers
    %f - Floating point numbers
    %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    %x/%X - Integers in hex representation (lowercase/uppercase)
"""
# => Interesting addition
print("2.4 + 4.3 = %f" % (2.4 + 4.3))
print(2.4 + 4.3)

# => Changing sign operator
a = 9
a = -a
print("Change sign result = %d" % a)

# => The 'is' operator (Unlike the double equals operator "==", the "is" operator does not match
# the values of the variables, but the instances themselves.)
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# => reverse indexing
print("Last element of x is %d" % x[-1])

# => Python substring
a = "ilker yaman"
print(a[2:4])       # start from second index, go till 4th index
print(a[2:8:2])     # start from second index, go till 8th index, by skipping 2
print(a[:8])        # first 8 character
print(a[2:])        # start from second index, go till end
print(a[:-1])       # go till last character
print(a[::-1])      # reverse a string
