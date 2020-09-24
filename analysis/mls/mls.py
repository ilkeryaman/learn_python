import pandas as pd
import numpy as np
from introduction.modules.printer_module import pretty_print

pd.set_option('display.max_columns', 10)  # Max how many columns will be shown at print output
pd.set_option('display.width', 200)  # It puts a new line after some spaces. This option sets output width.
pd.set_option('display.max_colwidth', 30)  # Sets maximum data with for printing

df = pd.read_csv("data/mls-salaries-2017.csv")

# Read first 10 data
pretty_print(df.head(10))

# Find how many data
pretty_print(df.index.size, heading="### Row Count ###")
pretty_print(len(df.index), heading="### Row Count with len Function ###")

# Find average of all salaries
def get_average_salary(dataframe):
    cl = "base_salary"
    missing_value_count = dataframe[cl].isnull().sum()
    count_of_valid_value = df[cl].size - missing_value_count
    total_of_valid_value = dataframe[cl].dropna().sum()
    return total_of_valid_value / count_of_valid_value


pretty_print(df["base_salary"].sum() / df.index.size,
             heading="### Dangerously-Calculated Average ###")  # dangerously-calculated average

pretty_print(df["base_salary"].isnull().sum(), heading="### Count of Missing Values ###")  # count of missing values

pretty_print(get_average_salary(df), heading="### Safe-Calculated Average ###")  # safe-calculated average

pretty_print(df["base_salary"].mean(), heading="### Average with Usual Way")

# Find maximum salary
pretty_print(df["base_salary"].max(), heading="### Maximum Salary ###")

# Find details of footballer with maximum salary
pretty_print(df.iloc[df["base_salary"].argmax()], heading="### Footballer with Maximum Salary ###")
# or
pretty_print(df.iloc[[df["base_salary"].argmax()]],
             heading="### Footballer with Maximum Salary (Attention! Check difference with previous approach.) ###")
# or
pretty_print(df[df["base_salary"] == df["base_salary"].max()], heading="### Footballer with Maximum Salary ###")

# Find last name of footballer with highest compensation
pretty_print(df.iloc[df["guaranteed_compensation"].argmax()], heading="### Footballer with Highest Compensation ###")
# or
pretty_print(df[df["guaranteed_compensation"] == df["guaranteed_compensation"].max()],
             heading="### Footballer with Highest Compensation ###")
pretty_print(df.iloc[df["guaranteed_compensation"].argmax()]["last_name"],
             heading="### Last Name of Footballer with Highest Compensation ###")


# Find position of Will Johnson
pretty_print(df[(df["first_name"] == "Will") & (df["last_name"] == "Johnson")],
             heading="### Details of Will Johnson ###")
pretty_print(df[(df["first_name"] == "Will") & (df["last_name"] == "Johnson")]["position"],
             heading="### Position of Will Johnson ###")
pretty_print(df[(df["first_name"] == "Will") & (df["last_name"] == "Johnson")]["position"].iloc[0],
             heading="### Real Value of Position of Will Johnson ###")

# Find average salaries for positions
pretty_print(df.groupby("position")["base_salary"].mean(), heading="### Average Salaries for Positions ###")

# Number of unique positions
pretty_print(len(df.groupby("position")), heading="### Number of Unique Positions ###")
# or
pretty_print(df["position"].nunique(), heading="### Number of Unique Positions ###")

# Find number of footballer for each position
pretty_print(df["position"].value_counts())

# Find number of footballers for each club
pretty_print(df["club"].value_counts())


# Find footballers that first name starts with Pa
def starts_with(first_name, letters):
    if first_name is np.nan:
        return False
    elif first_name.lower().startswith(letters.lower()):
        return True
    else:
        return False


pretty_print(df[df["first_name"].apply(starts_with, letters="pa")])

