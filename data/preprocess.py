import pandas as pd
import csv

def fullCheck(fileName):
    # read csv file with all columns viewed as string
    city_data = pd.read_csv("./data/csv original/" + fileName, dtype = str)
    # drop column chinese_name
    city_data = city_data.drop(columns = ["name_chinese"])
    # check if there is a null value in data
    length_of_check = len(city_data.columns)
    for i in range(length_of_check):
        if city_data.iloc[:, i].isnull().values.any():
            print("There is a null value in the column " + city_data.columns[i])
            break
    # write to csv
    city_data.to_csv("./data/csv new/" + fileName, index = False)

def partialCheck(fileName, checkLength):
    # read csv file with all columns viewed as string
    city_data = pd.read_csv("./data/csv original/" + fileName, dtype = str)
    # check if there is a null value in data
    for i in range(checkLength):
        if city_data.iloc[:, i].isnull().values.any():
            print("There is a null value in the column " + city_data.columns[i])
            break
    print(len(city_data), "original")
    # deduplicate on columns less than checkLength
    city_data = city_data.drop_duplicates(subset = city_data.columns[0:checkLength])

    print(len(city_data), "deduplicated")  
    city_data.to_csv("./data/csv new/" + fileName, index = False)

if __name__ == '__main__':
    checkList1 = ["city.csv", "district.csv", "station.csv"]
    for checkitem in checkList1:
        fullCheck(checkitem)
    checkList2 = ["meteorology.csv", "airquality.csv"]
    for checkitem in checkList2:
        partialCheck(checkitem, 2)
    partialCheck("weatherforecast.csv", 3)