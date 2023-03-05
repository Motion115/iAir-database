import pandas as pd

def data2dml(filename, tableName, columnDict):
    # read csv
    data = pd.read_csv(filename, dtype = str)
    # concat columnSet to a string, with a comma in between
    columnSetstr = ", ".join(columnDict.keys())
    starter = "insert into " + tableName + "(" + columnSetstr + ") values ("
    #print(starter)
    # create file
    f = open("./data/dml/" + tableName + ".sql", "w")
    for index, row in data.iterrows():
        instruction = starter
        types = list(columnDict.values())
        buffer = []
        for i in range(len(row)):
            if types[i] == str:
                buffer.append("'" + row[i] + "'")
            else:
                buffer.append(str(row[i]))
        instruction += ", ".join(buffer)

        instruction += ");"
        # write to file
        f.write(instruction + "\n")
    f.close()

    


if __name__ == '__main__':
    src = "./data/csv new/"
    csv2db = {
        "city.csv": "city",
        "district.csv": "district",
        "station.csv": "station",
        "airquality.csv": "air_quality",
        "meteorology.csv": "meteorology",
        "weatherforecast.csv": "forecast"
    }

    listOfDicts = []
    city_dict = {
        "city_id": str,
        "city_name": str,
        "latitude": float,
        "longitude": float,
        "cluster_id": int
    }
    listOfDicts.append(city_dict)

    district_dict = {
        "district_id": str,
        "district_name": str,
        "city_id": str
    }
    listOfDicts.append(district_dict)

    station_dict = {
        "station_id": str,
        "station_name": str,
        "district_id": str,
        "latitude": float,
        "longitude": float
    }
    listOfDicts.append(station_dict)

    airquality_dict = {
        "station_id": str,
        "tod": str,
        "pm2": float,
        "pm10": float,
        "no2": float,
        "co": float,
        "o3": float,
        "so2": float
    }
    listOfDicts.append(airquality_dict)

    meteorology_dict = {
        "station_id": str,
        "tod": str,
        "weather": int,
        "temperature": float,
        "pressure": float,
        "humidity": float,
        "wind_speed": float,
        "wind_direction": int
    }
    listOfDicts.append(meteorology_dict)

    forecast_dict = {
        "district_id": str,
        "tod": str,
        "tof": str,
        "frequency": int,
        "weather": int,
        "high_temp": float,
        "low_temp": float,
        "wind_direction": float,
        "wind_level": float
    }
    listOfDicts.append(forecast_dict)

    for i in range(len(listOfDicts)):
        print("Processing " + list(csv2db.keys())[i] + "...")
        data2dml(src + list(csv2db.keys())[i], list(csv2db.values())[i], listOfDicts[i])




