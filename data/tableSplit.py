import pandas as pd
import os

src = "./data/csv new/"
print(os.listdir(src))

# split the table for meteorology and weatherforecast
def splitTable(fileName):
    # read csv file with all columns viewed as string
    city_data = pd.read_csv(fileName, dtype = str)
    # create a new data frame
    city_level = pd.DataFrame(columns = city_data.columns)
    district_level = pd.DataFrame(columns = city_data.columns)
    # check the column id, if the length of id is 3, then copy to city_level, else, copy to district_level
    # use numpy to solve the issue, this is thousands time faster than simple loop
    city_level = city_level.append(city_data[city_data['id'].str.len() == 3])
    district_level = district_level.append(city_data[city_data['id'].str.len() == 5])
    # change the column name of the first column
    city_level = city_level.rename(columns = {"id": "city_id"})
    district_level = district_level.rename(columns = {"id": "district_id"})
    # split fileName by dot
    fileName = fileName.split(".")
    # write to csv
    city_level.to_csv("." + fileName[1] + "_c.csv", index = False)
    district_level.to_csv("." + fileName[1] + "_d.csv", index = False)

if __name__ == '__main__':
    splitTable(src + "meteorology.csv")
    splitTable(src + "weatherforecast.csv")