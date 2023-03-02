from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iair:iair@localhost:3306/iair'
db = SQLAlchemy(app)


@app.route('/')
def index_page():
    # check the table city in db
    cities = db.session.execute('select * from city')
    #print(cities.all())
    tables = db.session.execute('show tables')
    # show the content in tables
    for table in tables:
        print(table)
    return "Hello World!"

