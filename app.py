from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin


import requests

from backend.api import get_city_data

app = Flask(__name__)
# connect to database with variable db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://iair:iair@localhost:3306/iair'
db = SQLAlchemy(app)
# enable REST API
api = Api(app)

cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/data')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index_page():
    city = get_city_data(db)
    return city

if __name__ == '__main__':
    app.run(debug=True)

