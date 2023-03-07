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