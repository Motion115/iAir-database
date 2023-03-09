from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import requests
from backend.api import *

app = Flask(__name__)
# connect to database with variable db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iair:iair@localhost:3306/iair'
db = SQLAlchemy(app)
# enable REST API
api = Api(app)
cors = CORS(app)

@app.route('/getCityTable')
def index_page():
    city = get_city_data(db)
    return city

@app.route('/getTableLength/<table_name>')
def get_table_length(table_name):
    table_length = api_get_table_length(db, table_name)
    return table_length

@app.route('/getCityGroups')
def get_city_groups():
    table_length = api_get_city_groups(db)
    return table_length

if __name__ == '__main__':
    app.run(debug=True)

