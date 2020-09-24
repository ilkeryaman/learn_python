"""
Best practise is to put 2 blank lines, before function definition and after it
Function names should be lowercase
"""


def greeting(name):
    print("Hello", name)


def greeting2(name="ilker"):
    greeting(name)


greeting("ilker")
myName = None
greeting(myName)
greeting2(myName)
greeting2()
emptyString = ""
greeting2(emptyString)


# => Function with default values
def details(name="ilker", surname="yaman", phone="5321112233"):
    print("name: {}, surname: {}, phone: {}".format(name, surname, phone))


details()
details(surname="yemen")


# => Function with any number of arguments
def total(*a):
    ttl = 0
    for i in a:
        ttl += i
    return ttl


print(total(5, 4, 3))


# => Global and local variables
def print_local_glb():
    glb = 2
    print(glb)


def print_glb():
    global glb  # use global glb
    print(glb)


glb = "10"
print_local_glb()
print(glb)
print_glb()
