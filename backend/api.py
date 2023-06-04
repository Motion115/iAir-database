import json

def get_city_data(db):
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
            city[i]["cluster_id"] = "Greater Bay Aera"
    # for attribute cluster_id, replace all 1s with "Capital Urban Agglomeration" and all 2s with "Greater Bay Aera"
    #for i in range(len(city)):
     #   if city[i].cluster_id == "1":
       #     city[i].cluster_id = "Capital Urban Agglomeration"
      #  elif city[i].cluster_id == "2":
        #    city[i].cluster_id = "Greater Bay Aera"
    # list to json
    city = json.dumps(city)
    return city

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

    # print(city_statistics[0].keys())
    city_statistics = json.dumps(city_statistics)
    return city_statistics