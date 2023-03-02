create table city (
	city_id char(3) not null,
    city_name varchar(20) not null,
    latitude float not null,
    longitude float not null,
    cluster_id int not null,
    primary key(city_id)
    );
    
create table district (
	district_id char(5) not null,
    district_name varchar(20) not null,
    city_id char(3) not null,
    primary key(district_id),
    foreign key (city_id) references city(city_id)
    );

create table station (
	station_id char(6) not null,
    station_name varchar(20) not null,
    latitude float not null,
    longitude float not null,
    district_id char(5) not null,
    primary key(station_id),
    foreign key (district_id) references district(district_id)
    );

create table air_quality (
	station_id char(6) not null,
    tod datetime not null,
    pm2 float,
    pm10 float,
    no2 float,
    co float,
    o3 float,
    so2 float,
    primary key(station_id, tod),
    foreign key (station_id) references station(station_id)
    );

create table meteorology (
	station_id char(6) not null,
    tod datetime not null,
    weather int,
    temperature float,
    pressure float,
    humidity float,
    wind_speed float,
    wind_direction int,
    primary key(station_id, tod),
    foreign key (station_id) references station(station_id)
    );

create table forecast (
	district_id char(5) not null,
    tod datetime not null,
    tof datetime not null,
    frequency int,
    weather int,
    high_temp float,
    low_temp float,
    wind_direction float,
    wind_level float,
    primary key(district_id, tod, tof),
    foreign key (district_id) references district(district_id)
    );
    
desc city;
desc district;
desc station;
desc air_quality;
desc meteorology;
desc forecast;

show tables;