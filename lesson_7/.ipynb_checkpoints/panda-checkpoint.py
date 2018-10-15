import panda as pd


df = pd.read_csv("temperatures.csv")
df.head(2) #(2) stands for how many rows you want it to show

df.head() # shows only the head list

df.tail() # 

df.values

df["temperature"]
df["day"].head()

df["temperature"] > 20 # shows all the temperatures below 20 degrees from the temperatures.csv file
df["temperature"] < 0 # shows all the temperatures below 0 degrees from the file

df_cool = df[df["temperature"] < 0]
df_cool.head()

df_cool.to_csv("cool.csv") # saves a new csv file named cool.csv

#save stuff into a new file
df["temperature"].mean() # this shows the average
df["temperature"].max() # this shows the maximum temperature
df["temperature"].min() # this shows the minimum temperature
df["temperature"].value_counts() # it counts how many times a certain value occurs in a row/list

df["temperature"].value_counts().head()
snacks = pd.Series(["Mars", "Twix", "Oreo"])
snacks.value_counts()


df["temperature"].plot() # shows a table of content thing (grafiek)

