import numpy as np
import pandas as pd
from introduction.modules.printer_module import pretty_print

labels_list = ["Ilker", "Hakan", "Murat", "Serdar", "Erhan"]
data_list = [10, 20, 30, 40, 50]

series = pd.Series(data=data_list, index=labels_list)
pretty_print(series)

pretty_print(pd.Series(data_list))
np_array = np.array(data_list)
pretty_print(pd.Series(np_array))
pretty_print(pd.Series(np_array, labels_list))
pretty_print(pd.Series(np_array, index=["A", "B", "C", "D", "E"]))

data_dict = {"Ilker": 30, "Kemal": 80, "Mehmet": 60}
pretty_print(pd.Series(data_dict))
ser2019 = pd.Series([3, 14, 22, 20], ["Apple", "Banana", "Mango", "Strawberry"])
ser2020 = pd.Series([5, 10, 20, 40], ["Apple", "Banana", "Grapes", "Mango"])
pretty_print(ser2019)
total = ser2019 + ser2020
pretty_print(total)
pretty_print(total["Mango"])
pretty_print(total["Grapes"])
try:
    pretty_print(total["Peach"])
except KeyError as e:
    print("A key error is thrown: {}".format(e))
