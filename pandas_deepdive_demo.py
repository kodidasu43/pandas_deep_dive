
Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


Using csv library
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# Using the pandas library
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print(data)
print(data.head())
print(data.describe())

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.condition== "Sunny"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]#filtering the dataframe where day = Monday
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv",index=False)


#Central Park Squirrel Data Analysis

SQ_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(SQ_data[SQ_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(SQ_data[SQ_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(SQ_data[SQ_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")







