import json
import pandas as pd
from backend.utils import AQI_calculator
from backend.predict import gaussian_process_regressor

def api_get_city_data(db):
    # get data from database
    city = db.session.execute('select * from city')
    # expand city
    city = city.fetchall()
    # transform city into json format
    city = [dict(row) for row in city]
    for i in range(len(city)):
        if city[i]["cluster_id"] == 1:
            city[i]["cluster_id"] = "Capital Urban Agglomeration"
        elif city[i]["cluster_id"] == 2:
            city[i]["cluster_id"] = "Greater Bay Area"
    city = json.dumps(city)
    return city

def api_get_a_table(db, table_name):
    # get data from database
    table = db.session.execute('select * from ' + table_name)
    # expand table
    table = table.fetchall()
    # transform table into json format
    table = [dict(row) for row in table]
    table = json.dumps(table)
    return table

def api_get_table_length(db, table_name):
    # get data from database
    num = db.session.execute('select count(*) from ' + table_name)
    # expand num
    num = num.fetchall()
    # transform num into json format
    num = [dict(row) for row in num]
    num = num[0]["count(*)"]
    return str(num)

def api_get_city_groups(db):
    # get data from database
    city_groups = db.session.execute('select count(*) from (select distinct(cluster_id) from city) as temp')
    # expand city_groups
    city_groups = city_groups.fetchall()
    # transform city_groups into json format
    city_groups = [dict(row) for row in city_groups]
    # list to json
    city_groups = city_groups[0]["count(*)"]
    return str(city_groups)

def api_get_station_distribution(db, city_name):
    # get data from database
    station_distribution = db.session.execute("select * from station where district_id in (select district_id from district where city_id = (select city_id from city where city_name = '" + city_name + "'));")
    # expand station_distribution
    station_distribution = station_distribution.fetchall()
    # transform station_distribution into json format
    station_distribution = [dict(row) for row in station_distribution]
    
    # get the district table from database
    district = db.session.execute("select * from district where city_id = (select city_id from city where city_name = '" + city_name + "');")
    # expand district
    district = district.fetchall()
    # transform district into json format
    district = [dict(row) for row in district]

    # for each content in station_distribution, replace the district_id with district_name
    for i in range(len(station_distribution)):
        for j in range(len(district)):
            if station_distribution[i]["district_id"] == district[j]["district_id"]:
                station_distribution[i]["district_id"] = district[j]["district_name"]
                break

    station_distribution = json.dumps(station_distribution)
    return station_distribution

def api_get_distinct_city(db):
    # get data from database
    distinct_city = db.session.execute("select distinct(city_name) from city;")
    # expand station_distribution
    distinct_city = distinct_city.fetchall()
    # transform station_distribution into json format
    distinct_city = [dict(row) for row in distinct_city]
    distinct_city = json.dumps(distinct_city)
    return distinct_city


def api_get_city_statistics(db, city_name):
    sql_query = "select DATE(tod) as tod, avg(pm2) as pm2, avg(pm10) as pm10, avg(no2) as no2, avg(co) as co, avg(o3) as o3, avg(so2) as so2 from air_quality where station_id in (select station_id from station where district_id in (select district_id from district where city_id = (select city_id from city where city_name = '" + city_name + "'))) group by DATE(tod) order by DATE(tod);"
    # get data from database
    city_statistics = db.session.execute(sql_query)
    # expand city_statistics
    city_statistics = city_statistics.fetchall()
    # transform city_statistics into json format
    city_statistics = [dict(row) for row in city_statistics]
    # turn datetime format into string
    for i in range(len(city_statistics)):
        city_statistics[i]["tod"] = str(city_statistics[i]["tod"])
    # if the key is pm2, replace with pm2.5
    for i in range(len(city_statistics)):
        for key in city_statistics[i]:
            if key == "pm2":
                city_statistics[i]["pm2.5"] = city_statistics[i][key]
                del city_statistics[i][key]

    # calculate AQI
    for i in range(len(city_statistics)):
        # create a dict to input AQI_calculator
        indicators = {
            'PM2.5': city_statistics[i]["pm2.5"],
            'PM10': city_statistics[i]["pm10"],
            'SO2': city_statistics[i]["so2"],
            'NO2': city_statistics[i]["no2"],
            'O3': city_statistics[i]["o3"],
            'CO': city_statistics[i]["co"]
        }
        city_statistics[i]["AQI"] = AQI_calculator(indicators)

    # print(city_statistics[0].keys())
    city_statistics = json.dumps(city_statistics)
    return city_statistics


def api_get_meteo_data(db, city_name):
    sql_query = "select * from city_meteorology where city_id in (select city_id from city where city_name = '" + city_name + "') group by tod order by tod;"
    # get data from database
    meteo_data = db.session.execute(sql_query)
    # expand meteo_data
    meteo_data = meteo_data.fetchall()
    # transform meteo_data into json format
    meteo_data = [dict(row) for row in meteo_data]
    # turn datetime format into string
    for i in range(len(meteo_data)):
        meteo_data[i]["tod"] = str(meteo_data[i]["tod"])
    meteo_data = json.dumps(meteo_data)
    return meteo_data

def api_get_forecast_data(db, city_name):
    sql_query = "select * from city_forecast where city_id in (select city_id from city where city_name = '" + city_name + "') group by tod order by tod;"
    # get data from database
    forecast_data = db.session.execute(sql_query)
    # expand forecast_data
    forecast_data = forecast_data.fetchall()
    # transform forecast_data into json format
    forecast_data = [dict(row) for row in forecast_data]
    # turn datetime format into string
    for i in range(len(forecast_data)):
        forecast_data[i]["tod"] = str(forecast_data[i]["tod"])
        forecast_data[i]["tof"] = str(forecast_data[i]["tof"])
    forecast_data = json.dumps(forecast_data)
    return forecast_data

def api_download_data(db, mode):
    # judge the mode, call the respective api to get the data
    if mode == "city":
        datum = api_get_city_data(db)
    elif mode == "district":
        datum = api_get_a_table(db, "district")
    elif mode == "station":
        datum = api_get_a_table(db, "station")
    return datum


def api_download_city_specific_data(db, mode, city_name):
    # judge the mode, call the respective api to get the data
    if mode == "AQI":
        datum = api_get_city_statistics(db, city_name)
    elif mode == "meteo":
        datum = api_get_meteo_data(db, city_name)
    elif mode == "forecast":
        datum = api_get_forecast_data(db, city_name)
    return datum

def api_get_city_statistics_with_prediction(db, city_name):
    sql_query = "select DATE(tod) as tod, avg(pm2) as pm2, avg(pm10) as pm10, avg(no2) as no2, avg(co) as co, avg(o3) as o3, avg(so2) as so2 from air_quality where station_id in (select station_id from station where district_id in (select district_id from district where city_id = (select city_id from city where city_name = '" + city_name + "'))) group by DATE(tod) order by DATE(tod);"
    # get data from database
    city_statistics = db.session.execute(sql_query)
    # expand city_statistics
    city_statistics = city_statistics.fetchall()
    # transform city_statistics into json format
    city_statistics = [dict(row) for row in city_statistics]
    # turn datetime format into string
    for i in range(len(city_statistics)):
        city_statistics[i]["tod"] = str(city_statistics[i]["tod"])
    # if the key is pm2, replace with pm2.5
    for i in range(len(city_statistics)):
        for key in city_statistics[i]:
            if key == "pm2":
                city_statistics[i]["pm2.5"] = city_statistics[i][key]
                del city_statistics[i][key]

    # calculate AQI
    for i in range(len(city_statistics)):
        # create a dict to input AQI_calculator
        indicators = {
            'PM2.5': city_statistics[i]["pm2.5"],
            'PM10': city_statistics[i]["pm10"],
            'SO2': city_statistics[i]["so2"],
            'NO2': city_statistics[i]["no2"],
            'O3': city_statistics[i]["o3"],
            'CO': city_statistics[i]["co"]
        }
        city_statistics[i]["AQI"] = AQI_calculator(indicators)
    
    # use pandas to transform city_statistics into dataframe
    city_statistics_dframe = pd.DataFrame(city_statistics)
    # print(city_statistics_dframe["AQI"])
    time_length = len(city_statistics_dframe)
    y_pred = gaussian_process_regressor(time_length, city_statistics_dframe["AQI"])
    # print y_pred in integers
    y_pred = [int(i) for i in y_pred]
    # add y_pred to city_statistics
    for i in range(len(city_statistics)):
        city_statistics[i]["AQI_prediction"] = y_pred[i]
    
    # create a copy of city_statistics, only preserving tod and AQI
    city_statistics_copy_AQI = []
    city_statistics_copy_predict_AQI = []

    for i in range(len(city_statistics)):
        city_statistics_copy_AQI.append({"tod": city_statistics[i]["tod"], "AQI": city_statistics[i]["AQI"], "category": "AQI"})
        city_statistics_copy_predict_AQI.append({"tod": city_statistics[i]["tod"], "AQI": city_statistics[i]["AQI_prediction"], "category": "AQI_prediction"})

    city_statistics = city_statistics_copy_AQI + city_statistics_copy_predict_AQI

    city_statistics = json.dumps(city_statistics)
    return city_statistics


def api_validification(db, token):
    # get user data from database
    user_data = db.session.execute("select token from identification;")
    # expand user_data
    user_data = user_data.fetchall()
    # transform user_data into json format
    user_data = [dict(row) for row in user_data]
    # if token is in user_data, return True
    for i in range(len(user_data)):
        if token == user_data[i]["token"]:
            return True
    return False

def api_is_manager(token):
    if token == "admin":
        return True
    return False

def api_add_user(db, token):
    # add token to database
    db.session.execute("insert into identification (token) values ('" + token + "');")
    db.session.commit()

def api_delete_user(db, token):
    # delete token from database
    db.session.execute("delete from identification where token = '" + token + "';")
    db.session.commit()