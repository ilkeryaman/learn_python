# => GroupBy
import pandas as pd
from introduction.modules.printer_module import pretty_print

dataset = {
    "Department": ["IT", "HR", "Finance", "Finance", "IT", "HR"],
    "Employee": ["Ilker", "Erhan", "Ali", "Serdar", "Esra", "Recep"],
    "Salary": [3000, 3500, 2500, 4500, 4000, 2000]
}

df = pd.DataFrame(dataset)
pretty_print(df)

dep_group = df.groupby("Department")
pretty_print(dep_group)
pretty_print(dep_group.sum())
pretty_print(dep_group.mean())
pretty_print(dep_group.mean().loc["IT"])
pretty_print(int(dep_group.mean().loc["IT"]))

pretty_print(dep_group.count())
pretty_print(dep_group.max())
pretty_print(dep_group.min())
pretty_print(dep_group.min()["Salary"][0])
pretty_print(dep_group.min()["Salary"]["Finance"])


