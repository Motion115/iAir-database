# file load from csv
SHOW variables like '%secure%' ;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/city.csv'
into table city
fields terminated by ',' ;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/district.csv'
into table district
fields terminated by ',' ;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/station.csv'
into table station
fields terminated by ',' ;

delete from air_quality;
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/airquality.csv'
into table air_quality
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n'
(station_id, tod, @pm2, @pm10, @no2, @co, @o3, @so2)
set
pm2 = NULLif(@pm2,''),
pm10 = NULLif(@pm10,''),
no2 = NULLif(@no2,''),
co = NULLif(@co,''),
o3 = NULLif(@o3,''),
so2 = NULLif(@so2,'')
;

#### not solved
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/meteorology.csv'
into table meteorology
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(station_id, tod, @weather, @temperature, @pressure, @humidity, @wind_speed, @wind_direction)
set
weather = NULLif(@weather,''),
temperature = NULLif(@temperature,''),
pressure = NULLif(@pressure,''),
humidity = NULLif(@humidity,''),
wind_speed = NULLif(@wind_speed,''),
wind_direction = NULLif(@wind_direction,'')
;