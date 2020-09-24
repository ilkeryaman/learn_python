import math

val = 6.80
print(math.floor(val))
print(math.ceil(val))

import time
print(time.time())
time.sleep(5)
print(time.time())

# => from - import usage
from random import *
print(randint(5, 20))


# => dangerous from - import usage
from time import sleep
def sleep(x):
    print("There is no sleep anymore.")


print(time.time())
sleep(10)
print(time.time())


# => sample own module and usage of import - as
from sample_month_module import month_module
from sample_month_module import months
try:
    print(months)
    month_module.get_month_by_order(4)
except ValueError as e:
    print("An error occurred while retrieving month name: {}".format(e))

help(month_module)
