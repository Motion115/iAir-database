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
    # iterate through the rows
    for index, row in city_data.iterrows():
        # read the second column
        content = row[1]
        # split content with " "
        content = content.split(" ")
        # for content[0], split with "-"; for content[1], split with ":"
        content[0] = content[0].split("-")
        content[1] = content[1].split(":")
        # concatenate the content
        content = content[0] + content[1]
        # join content with noting
        content = "".join(content)
        city_data.iloc[index, 1] = content

    '''
    # if tod exists, add a single quote to the front and the end
    if "time_forecast" in city_data.columns:
        city_data['time_forecast'] = city_data['time_forecast'].apply(lambda x: "'" + x + "'")
    if "time_future" in city_data.columns:
        city_data['time_future'] = city_data['time_future'].apply(lambda x: "'" + x + "'")
    if "time" in city_data.columns:
        city_data['time'] = city_data['time'].apply(lambda x: "'" + x + "'")
    '''
    print(len(city_data), "deduplicated")  
    city_data.to_csv("./data/csv new/" + fileName, index = False)

if __name__ == '__main__':
    checkList1 = ["city.csv", "district.csv", "station.csv"]
    for checkitem in checkList1:
        fullCheck(checkitem)
    checkList2 = ["meteorology.csv"]
    for checkitem in checkList2:
        partialCheck(checkitem, 2)
    partialCheck("weatherforecast.csv", 3)