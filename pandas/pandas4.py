# => Multi-index grouping of Dataframes
import pandas as pd
from numpy.random import randn
from introduction.modules.printer_module import pretty_print
outer_index = ["Group1", "Group1", "Group1", "Group2", "Group2", "Group2", "Group3", "Group3", "Group3"]
inner_index = ["Index1", "Index2", "Index3", "Index1", "Index2", "Index3", "Index1", "Index2", "Index3"]
hierarchy = list(zip(outer_index, inner_index))
pretty_print(hierarchy)

hierarchy = pd.MultiIndex.from_tuples(hierarchy)
pretty_print(hierarchy)

df = pd.DataFrame(randn(9, 3), hierarchy, columns=["Column1", "Column2", "Column3"])
pretty_print(df)

pretty_print(df["Column1"])
pretty_print(df.loc["Group1"])
pretty_print(df.loc[["Group1", "Group2"]])
pretty_print(df.loc["Group1"].loc["Index1"])
pretty_print(df.loc["Group1"].loc["Index1"]["Column1"])

pretty_print(df.index.names)
df.index.names = ["Groups", "Indexes"]
pretty_print(df.index.names)
pretty_print(df)

pretty_print(df.loc["Group1"])
pretty_print(df.xs("Group1"))
pretty_print(df.xs("Group2").xs("Index1").xs("Column1"))

pretty_print(df.xs("Index1", level=1))
pretty_print(df.xs("Index1", level="Indexes"))
