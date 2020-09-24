import pandas as pd
from numpy.random import randn
from introduction.modules.printer_module import pretty_print

# => Dataframe filtering
df = pd.DataFrame(randn(4, 3), ["A", "B", "C", "D"], ["Column1", "Column2", "Column3"])
pretty_print(df)
boolean_df = df > 0
pretty_print(boolean_df)
pretty_print(df[boolean_df])
pretty_print(df[df > 0])
pretty_print(df["Column1"] > 0)
pretty_print(df[df["Column1"] > 0])

# In Pandas, for filtering & is used instead of and operator. Also parenthesis for separating conditions are mandatory.
pretty_print(df[(df["Column1"] > 0) & (df["Column2"] > 0)])

# In Pandas, for filtering | is used instead of or operator. Also parenthesis for separating conditions are mandatory.
pretty_print(df[(df["Column1"] > 0) | (df["Column2"] > 0)])

df["Column4"] = pd.Series(randn(4), ["A", "B", "C", "D"])
df["Column5"] = randn(4)
df["Column6"] = ["new_value1", "new_value2", "new_value3", "new_value4"]
pretty_print(df)

# There is inplace parameter for set_index method, it is false as default
df.set_index("Column6")
pretty_print(df)

df.set_index("Column6", inplace=True)
pretty_print(df)

pretty_print(df.index.name)
pretty_print(df.index.names)
