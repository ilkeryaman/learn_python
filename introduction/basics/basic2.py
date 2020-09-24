# => Data type conversion
a = 43
b = float(a)
print(b)

a = 5.14
b = int(a)
print(b)

a = 456
b = str(a)
print(b)
print(len(b))

val = '599012'
int_val = int(val)
print(int_val)

print(bool(12))
print(bool(-1))
print(bool(0))

# => print different types of values at one line
print("ilker", 37, 4.5, True)

# => print different types of values at one line with sep parameter (like concatenate)
print("ilker", 37, 4.5, True, sep='#')

# => print by separating every character of string variables (it does not separate other types)
print(*"ilker", 37, 4.5, True, sep='#')

# => print function special characters
print("hello ilker yaman,\n\t how are you?")

# => type function
print(type(34))
print(type(4.5))
print(type("Turkey"))
print(type(False))

# => String formatting (check pyformat.info web site)
print("{} {} {}".format(3.145, 2.2099, 7))
print("{2} {0} {1}".format(3.145, 2.2899, 7))
print("{:.2f} {:.2f} {}".format(3.145, 2.2899, 7))
print("Your username is {username} and password is {password}".format(password="qwerty", username="ilkery"))
print(f"This is {a}")   # Attention to f (f-string statement).
