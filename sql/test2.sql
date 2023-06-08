select city_id from city
where city_name = 'Beijing';

select district_id from district
where city_id = (select city_id from city where city_name = 'Beijing');


select station_id from station
where district_id in (select district_id from district
where city_id = (select city_id from city where city_name = 'Beijing'));

select DATE(tod) as tod, avg(pm2) as pm2, avg(pm10) as pm10, avg(no2) as no2, avg(co) as co, avg(o3) as o3, avg(so2) as so2 from air_quality
where station_id in (
select station_id from station
where district_id in (select district_id from district
where city_id = (select city_id from city where city_name = 'Beijing'))
)
group by DATE(tod)
order by DATE(tod)
;

select count(*) from 
(select distinct(cluster_id) from city) as temp;

select * from city;

select * from city_meteorology
where city_id in (select city_id from city where city_name = 'Beijing')
group by tod
order by tod
;

select * from city_forecast
where city_id in (select city_id from city where city_name = 'Beijing')
group by tod
order by tod
;