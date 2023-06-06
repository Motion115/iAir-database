from flask import Flask, Response, jsonify, send_file
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

@app.route('/getStationDistribution/<city_name>')
def get_station_distribution(city_name):
    station_dist = api_get_station_distribution(db, city_name)
    return station_dist

@app.route('/getDistinctCity')
def get_distinct_city():
    distinct_city = api_get_distinct_city(db)
    return distinct_city

@app.route('/getCityStatistics/<city_name>')
def get_city_statistics(city_name):
    city_statistics = api_get_city_statistics(db, city_name)
    return city_statistics

@app.route('/getCityStatisticsWithPrediction/<city_name>')
def get_city_statistics_with_prediction(city_name):
    city_statistics = api_get_city_statistics_with_prediction(db, city_name)
    return city_statistics

@app.route('/downloader/<mode>', methods=['GET'])
def download(mode):
    datum = api_download_data(db, mode)
    # read json datum to df
    df = pd.read_json(datum)
    # Convert the data to a CSV string
    csv_string = df.to_csv(index=False)
    # Create a response object with the CSV string as the content
    response = Response(csv_string, mimetype='text/csv')
    # Set the appropriate headers to indicate that the response should be downloaded as a file
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    return response

@app.route('/downloader2/<mode>/<city_name>', methods=['GET'])
def download2(mode, city_name):
    datum = api_download_city_specific_data(db, mode, city_name)
    # read json datum to df
    df = pd.read_json(datum)
    # Convert the data to a CSV string
    csv_string = df.to_csv(index=False)
    # Create a response object with the CSV string as the content
    response = Response(csv_string, mimetype='text/csv')
    # Set the appropriate headers to indicate that the response should be downloaded as a file
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    return response


if __name__ == '__main__':
    app.run(debug=True)
    # api_get_city_statistics_with_prediction(db, "BeiJing")

