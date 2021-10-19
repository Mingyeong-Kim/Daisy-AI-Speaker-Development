select from_station_name, count(*) from divvy_2015 group by from_station_name order by count(*) desc;
select gender, avg(tripduration) from divvy_2015 group by gender;
select usertype, avg(tripduration) from divvy_2015 group by usertype;
select birthyear, count(*) from divvy_2015 group by birthyear;
