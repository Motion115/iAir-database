# file load from csv
SHOW variables like '%secure%';
# the files should be in the safe folder first
# always ignore 1 row because of the title for each csv

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/city.csv'
into table city
fields terminated by ',' ignore 1 rows;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/district.csv'
into table district
fields terminated by ',' ignore 1 rows;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/station.csv'
into table station
fields terminated by ',' ignore 1 rows;

# the following table might have null values, so the termination code should be modified
delete from air_quality;
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/n_airquality.csv'
into table air_quality
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(station_id, tod, @pm2, @pm10, @no2, @co, @o3, @so2)
set
pm2 = NULLif(@pm2,''),
pm10 = NULLif(@pm10,''),
no2 = NULLif(@no2,''),
co = NULLif(@co,''),
o3 = NULLif(@o3,''),
so2 = NULLif(@so2,'')
;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/n_meteorology_c.csv'
into table city_meteorology
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(city_id, tod, @weather, @temperature, @pressure, @humidity, @wind_speed, @wind_direction)
set
weather = NULLif(@weather,''),
temperature = NULLif(@temperature,''),
pressure = NULLif(@pressure,''),
humidity = NULLif(@humidity,''),
wind_speed = NULLif(@wind_speed,''),
wind_direction = NULLif(@wind_direction,'')
;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/n_meteorology_d.csv'
into table district_meteorology
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(district_id, tod, @weather, @temperature, @pressure, @humidity, @wind_speed, @wind_direction)
set
weather = NULLif(@weather,''),
temperature = NULLif(@temperature,''),
pressure = NULLif(@pressure,''),
humidity = NULLif(@humidity,''),
wind_speed = NULLif(@wind_speed,''),
wind_direction = NULLif(@wind_direction,'')
;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/n_weatherforecast_c.csv'
into table city_forecast
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(city_id, tod, tof, @frequency, @weather, @high_temp, @low_temp, @wind_direction, @wind_level)
set
frequency = NULLif(@frequency,''),
weather = NULLif(@weather,''),
high_temp = NULLif(@high_temp,''),
low_temp = NULLif(@low_temp,''),
wind_direction = NULLif(@wind_direction,''),
wind_level = NULLif(@wind_level,'')
;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/n_weatherforecast_d.csv'
into table district_forecast
fields terminated by ',' OPTIONALLY ENCLOSED BY '"' lines terminated by '\r\n' ignore 1 rows
(district_id, tod, tof, @frequency, @weather, @high_temp, @low_temp, @wind_direction, @wind_level)
set
frequency = NULLif(@frequency,''),
weather = NULLif(@weather,''),
high_temp = NULLif(@high_temp,''),
low_temp = NULLif(@low_temp,''),
wind_direction = NULLif(@wind_direction,''),
wind_level = NULLif(@wind_level,'')
;