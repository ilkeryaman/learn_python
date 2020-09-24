# => Dataframes
import pandas as pd
from numpy.random import randn
from introduction.modules.printer_module import pretty_print

pretty_print(randn(3, 3))
df = pd.DataFrame(data=randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])
pretty_print(df)
pretty_print(df["Column2"])
pretty_print(type(df["Column2"]))
pretty_print(df.loc["A"])
pretty_print(df[["Column1", "Column3"]])

df["Column4"] = pd.Series(randn(3),index=["A", "B", "C"])
pretty_print(df)

df["Column5"] = df["Column1"] + df["Column2"] + df["Column3"]
pretty_print(df)

"""
There is a rule to drop column, row from DataFrame.
Axis information as (x = 0, y = 1) should be provided. Otherwise x is default.
Since inplace parameter's value is false as default, we won't see the result after drop.
"""
df.drop("Column5", axis=1)
pretty_print(df)

df.drop("Column5", axis=1, inplace=True)
pretty_print(df)

pretty_print(df.iloc[0])  # index A
pretty_print(df.iloc[1])  # index B
pretty_print(df.iloc[2])  # index C

pretty_print(df.loc["A", "Column2"])
pretty_print(df.loc[["A", "B"], ["Column1", "Column2"]])
