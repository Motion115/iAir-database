import json

def get_city_data(db):
    # get data from database
    city = db.session.execute('select * from city')
    # expand city
    city = city.fetchall()
    # transform city into json format
    city = [dict(row) for row in city]
    # list to json
    city = json.dumps(city)
    # print(city)
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