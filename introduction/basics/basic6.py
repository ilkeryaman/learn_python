# => None value (null)
a = None
print(a)
pretty = "{} = {}"


# => Equality check
print(pretty.format("\"ilker\" == '''ilker'''",     "ilker" == '''ilker'''))
print(pretty.format("[1, 2, 3] == [1, 2, 3]",       [1, 2, 3] == [1, 2, 3]))
print(pretty.format("[1, 2, 3] == [3, 2, 1]",       [1, 2, 3] == [3, 2, 1]))

# => and/or/not/in operators
print(pretty.format("True and False",               True and False))
print(pretty.format("True or False",                True or False))
print(pretty.format("not False",                    not False))
print(pretty.format("5 in [1, 2, 3, 4]",            5 in [1, 2, 3, 4]))
print(pretty.format("\"hel\" in \"hello\"",         "hel" in "hello"))
print(pretty.format("5 < 6 < 7",                    5 < 6 < 7))
print(pretty.format("7 > 6 > 5",                    7 > 6 > 5))  # not as javascript, it returns True

# => if, else if, else
a = 8
if a > 10:
    print("Value is %d" % a)
    print("It is bigger than 10")
elif (a > 8):
    print("%d is entered" % a)
    print("It is bigger than 8")
else:
    print("Value entered is %d" % a)
    print("It is lower than 9")

# => if else in one line
is_true = True if 2 > 1 else False
print("is_true: {}".format(is_true))

# => print more than one line
print("""
Value entered is %d
It is a great value
Yaaayyyy !!!
""" % a)
