# => Other Dataframe operations
import pandas as pd
from introduction.modules.printer_module import pretty_print

df = pd.DataFrame({
    "Column1": [1, 2, 3, 4, 5, 6],
    "Column2": [100, 100, 200, 300, 300, 100],
    "Column3": ["Ahmet", "Mehmet", "Ilker", "Hakan", "Mustafa", "Ali"]
})

pretty_print(df)

pretty_print(df.head())  # returns first n rows (default = 5)
pretty_print(df.head(3))

pretty_print(df["Column2"].unique())
pretty_print(df["Column2"].nunique())   # number of unique values
pretty_print(df["Column2"].value_counts())

pretty_print(df[(df["Column1"] >= 4) & (df["Column2"] == 300)])


def multiply_with(value, factor=3):
    return value * factor


pretty_print(df["Column2"].apply(multiply_with, 5))
pretty_print(df["Column2"].apply(lambda x: x*2))
pretty_print(df["Column3"].apply(len))

pretty_print(df.drop("Column3", axis=1))

pretty_print(df.columns)
pretty_print(df.index)
pretty_print(len(df.index))
pretty_print(df.index.names)
pretty_print(df.sort_values("Column2"))
pretty_print(df.sort_values("Column2", ascending=False))

df = pd.DataFrame({
    "Month": ["Mar", "Apr", "May", "Mar", "Apr", "May", "Mar", "Apr", "May"],
    "City": ["Ankara", "Ankara", "Ankara", "Istanbul", "Istanbul", "Istanbul", "Izmir", "Izmir", "Izmir"],
    "Moisture": [10, 25, 50, 21, 67, 80, 30, 70, 75]
})

pretty_print(df)

pretty_print(df.pivot_table(index="Month", columns="City", values="Moisture"))
pretty_print(df.pivot_table(index="City", columns="Month", values="Moisture"))

