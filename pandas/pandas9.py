# => Read dataset from file (kaggle.com)
import pandas as pd
from introduction.modules.printer_module import pretty_print

pd.set_option('display.max_columns', 10)  # Max how many columns will be shown at print output

dataset = pd.read_csv("data/USvideos.csv")
pretty_print(dataset)

newdataset1 = dataset.drop(["video_id", "trending_date"], axis=1)
pretty_print(newdataset1)

newdataset1.to_csv("data/USvideos_new.csv")                 # writes to file with index
newdataset1.to_csv("data/USvideos_new2.csv", index=False)   # writes to file without index

# => Read from internet (Reads all tables and puts them to array)
new = pd.read_html("https://www.contextures.com/xlSampleData01.html", header=0)  # header=0 means, first row is header
pretty_print(new)
pretty_print(new[0])
