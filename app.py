from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iair:iair@localhost:3306/iair'
db = SQLAlchemy(app)


@app.route('/')
def index_page():
    # check the table city in db
    cities = db.session.execute('select * from city where city_id > "300"')
    #print(cities.all())
    # concat the string in cities list
    cities = [city[0] for city in cities]
    cities = ", ".join(cities)
    return cities

