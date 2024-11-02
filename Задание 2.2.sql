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

--SELECT name 
  --FROM track t 
 --WHERE name ILIKE '%my%' OR name LIKE '%мой%';

SELECT t."name" 
  FROM track t 
 WHERE t."name" ILIKE 'my %'
    OR t."name" ILIKE '% my'
    OR t."name" ILIKE '% my %'
    OR t."name" ILIKE 'my'
    OR t."name" ILIKE 'мой %'
    OR t."name" ILIKE '% мой'
    OR t."name" ILIKE '% мой %'
    OR t."name" ILIKE 'мой';
    
SELECT t."name" 
  FROM track t
 WHERE string_to_array(lower(t."name"), ' ') && array ['my', 'мой'];
 
SELECT t."name" 
  FROM track t 
 WHERE t."name" ~* '\mmy\M' or t."name" ~* '\mмой\M';
	
