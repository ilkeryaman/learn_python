import pandas as pd
import numpy as np
from introduction.modules.printer_module import pretty_print

pd.set_option('display.max_columns', 20)  # Max how many columns will be shown at print output
pd.set_option('display.width', 500)  # It puts a new line after some spaces. This option sets output width.
pd.set_option('display.max_colwidth', 50)  # Sets maximum data with for printing

df = pd.read_csv("data/USvideos.csv")

# Drop Following Columns:   trending_date, channel_title, publish_time, thumbnail_link, comments_disabled,
#                           ratings_disabled, video_error_or_removed, description
df.drop(["trending_date", "channel_title", "publish_time", "thumbnail_link", "comments_disabled", "ratings_disabled",
         "video_error_or_removed", "description"], axis=1, inplace=True)

# Read first 5 data
pretty_print(df.head())

# Find current column and row count
pretty_print(df.index.size, heading="### Row Count ###")
pretty_print(len(df.index), heading="### Row Count with len function ###")
pretty_print(df.columns.size, heading="### Column Count ###")
pretty_print(len(df.columns), heading="### Column Count with len function ###")

# Find average of likes and dislikes
pretty_print(df["likes"].mean(), heading="### Average of Likes ###")
pretty_print(df["dislikes"].mean(), heading="### Average of Dislikes ###")

# Find title of video with most views
pretty_print(df[(df["views"] == df["views"].max())], heading="### Video with Most Views ###")
pretty_print(df[(df["views"] == df["views"].max())]["title"], heading="### Title of Video with Most Views ###")
pretty_print(df[(df["views"] == df["views"].max())]["title"].iloc[0],
             heading="### Real Value of Title of Video with Most Views ###")

# Find title of video with least views
pretty_print(df[(df["views"] == df["views"].min())], heading="### Video with Least Views ###")
pretty_print(df[(df["views"] == df["views"].min())]["title"], heading="### Title of Video with Least Views ###")
pretty_print(df[(df["views"] == df["views"].min())]["title"].iloc[0],
             heading="### Real Value of Title of Video with Least Views ###")

# Find average of comments count for each category
pretty_print(df.groupby("category_id")["comment_count"].mean(), heading="### Average of Comments Count ###")

# Find video count for each category
pretty_print(df["category_id"].value_counts(), heading="### Video Count for Each Category ###")

# Add a new column that shows length of title for each video
df["title_length"] = df["title"].apply(len)
pretty_print(df, heading="### New Column as title_length ###")


# Add a new column that shows tag count for each video
def count_tags(tag):
    return len(tag.split(sep="|"))


df["tag_count"] = df["tags"].apply(count_tags)
pretty_print(df, heading="### New Column as tag_count ###")

# Order Videos By Likes In Descending Order
pretty_print(df.sort_values("likes", ascending=False))

# Order Videos By Likes / Dislikes Ration (Descending Order)
pretty_print(df["likes"].iteritems(), heading="### IterItems for Likes Column ###")  # iteritems creates a tuple that contains likes information for each row
pretty_print(list(df["likes"].iteritems()), heading="### Structure of IterItems for Likes Column ###")  # Lets see the structure


def get_likes_dislikes_ratio(likes, dislikes):
    """ Function to calculcate likes / dislikes ratio for each row """
    likes_list = []
    for key, value in likes.iteritems():
        likes_list.append(value)

    dislikes_list = []
    for key, value in dislikes.iteritems():
        dislikes_list.append(value)

    ratio_list = []
    for likes_count, dislikes_count in list(zip(likes_list, dislikes_list)):
        if likes_count == 0 and dislikes_count == 0:
            ratio_list.append(0)
        else:
            ratio_list.append(likes_count / (likes_count + dislikes_count))

    return ratio_list


df["likes_dislikes_ratio"] = get_likes_dislikes_ratio(df["likes"], df["dislikes"])

pretty_print(df, "### Dataframe with Likes / Dislikes Ratio ###")

pretty_print(df.sort_values("likes_dislikes_ratio", ascending=False),
             heading="### Dataframe Ordered by Likes / Dislikes Ratio ###")  # sort by like / dislike ratio
