SELECT name, duration 
  FROM track t 
 WHERE duration = 
       (SELECT max(duration) FROM track t2);

SELECT name, duration 
  FROM track t 
 WHERE duration >= 210;

SELECT name, release_year 
  FROM collection c 
 WHERE release_year BETWEEN 2018 AND 2020;

SELECT name 
  FROM executor e 
 WHERE name NOT LIKE '% %';

SELECT name 
  FROM track t 
 WHERE name LIKE '%my%' OR name LIKE '%мой%';
	