def multiplication_table():
    for i in range(1, 11):
        print("""
======
 {}'s
======""".format(i))
        for j in range(1, 11):
            yield "{} x {} = {}".format(i, j, i*j)


iterator = iter(multiplication_table())
for x in iterator:
    print(x)
