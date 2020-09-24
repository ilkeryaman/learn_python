# => Working with missing data (Pre-processing data)
import numpy as np
import pandas as pd
from introduction.modules.printer_module import pretty_print

arr = np.array([[10, 20, np.nan], [5, np.nan, np.nan], [21, np.nan, 10]])
pretty_print(arr)

df = pd.DataFrame(arr, index=["Index1", "Index2", "Index3"], columns=["Column1", "Column2", "Column3"])
pretty_print(df)

pretty_print(df.dropna())  # Since it is dropping according to axis and default value = 0 (x), it will drop all columns
pretty_print(df.dropna(axis=1))  # Since axis value = 1 (y), only Column2 and Column3 are dropped.
pretty_print(df.dropna(thresh=2))  # If there are at least 2 not a number value, do not remove this index

pretty_print(df.fillna(value=1))
pretty_print(df.sum())
pretty_print(df.sum().sum())
pretty_print(df.fillna(value=df.sum()))
pretty_print(df.fillna(value=df.sum().sum()))

pretty_print(df.size)                   # size of Dataframe
pretty_print(df.isnull())               # show as True/False
pretty_print(df.isnull().sum())         # column-based count of not a numbers
pretty_print(df.isnull().sum().sum())   # matrix-based count of not a numbers


"""
Calculates average of matrix
"""
def calculate_mean(df):
    total_sum = df.sum().sum()
    total_num = df.size - df.isnull().sum().sum()
    return total_sum / total_num


pretty_print(df.fillna(value=calculate_mean(df)))
