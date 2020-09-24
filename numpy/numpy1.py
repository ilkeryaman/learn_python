import numpy as np
from introduction.modules.printer_module import pretty_print

data_list = [1, 2, 3]
data_list2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
data_list3 = []
arr = np.array(data_list)
arr2 = np.array(data_list2)

pretty_print(arr)
pretty_print(arr2)
pretty_print(arr2[2, 2])
pretty_print(np.arange(25))
pretty_print(np.arange(10, 20))
pretty_print(np.arange(0, 100, 5))
pretty_print(np.linspace(0, 100, 5))
pretty_print(np.linspace(1, 6, 6))
pretty_print(np.zeros(5))
pretty_print(np.zeros((2, 3)))
pretty_print(np.ones(6))
pretty_print(np.ones((2, 3)))
pretty_print(np.eye(4))
pretty_print(np.random.randint(0, 10))
pretty_print(np.random.randint(15))
pretty_print(np.random.randint(1, 10, 5))
pretty_print(np.random.randn(5))  # Gaussian distribution
pretty_print(np.random.rand(1, 10))  # rand function
pretty_print(np.arange(25).reshape(5, 5))

new_array = np.random.randint(1, 100, 10)
pretty_print(new_array)
pretty_print(new_array.max())
pretty_print(new_array.min())
pretty_print(new_array.sum())
pretty_print(new_array.mean())  # average
pretty_print(new_array.argmax())  # index of max value
pretty_print(new_array.argmin())  # index of min value
