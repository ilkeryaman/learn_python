import numpy as np
from introduction.modules.printer_module import pretty_print

arr = np.arange(1, 10)
pretty_print(arr)
arr[:3] = 25
pretty_print(arr)

arr = np.arange(1, 10)
arr2 = arr
arr2[:3] = 100
pretty_print(arr)
pretty_print(arr2)

arr = np.arange(1, 10)
arr2 = arr.copy()
arr2[:3] = 100
pretty_print(arr)
pretty_print(arr2)

new_array = np.arange(1, 21).reshape(5, 4)
pretty_print(new_array)
pretty_print(new_array[:, 0:2])
pretty_print(new_array[:3, :3])
pretty_print(new_array[0:2, :])
pretty_print(new_array[:2])

pretty_print(arr > 3)

# => Filtering an array
bool_array = arr > 3
pretty_print(arr[bool_array])


