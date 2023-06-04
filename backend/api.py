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

def api_get_station_distribution(db):
    # get data from database
    station_distribution = db.session.execute("select * from station where district_id in (select district_id from district where city_id = (select city_id from city where city_name = 'Beijing'));")
    # expand station_distribution
    station_distribution = station_distribution.fetchall()
    # transform station_distribution into json format
    station_distribution = [dict(row) for row in station_distribution]
    

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
