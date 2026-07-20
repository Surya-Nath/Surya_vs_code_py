#print the csv data first
with open("weather_data.csv") as data_file:
    data = data_file.read()
    print(data)
#getting only temp data
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
#using pandas
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
#doing other things with pandas
data_dict = {
    "students": ["jack", "sunny", "james", "angela"],
    "age": [25, 18, 19, 23]
}
data = pandas.DataFrame(data_dict)
#make a new csv file
data.to_csv("new_data.csv")
print(data)

