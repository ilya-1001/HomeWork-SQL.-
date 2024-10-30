SELECT g."name" , count(executor_id) 
  FROM genre g 
       JOIN genre_executor ge 
         on g.id = ge.genre_id 
   GROUP BY g."name"; 

SELECT a."name" , a.release_year , count(t.id) 
  FROM album a 
       JOIN track t 
         ON a.id = t.id 
      WHERE a.release_year BETWEEN 2019 and 2020
   GROUP BY a."name", a.release_year; 

SELECT a."name" , AVG(t.id) 
  FROM album a 
       JOIN track t 
         ON a.id = t.album_id 
   GROUP BY a."name"; 

SELECT e."name" 
  FROM executor e 
       JOIN executor_album ea 
         ON e.id = ea.executor_id 
       JOIN album a 
         ON a.id = ea.album_id
      WHERE a.release_year != 2020;

SELECT c."name" 
  FROM collection c
       JOIN collection_track ct 
         ON c.id = ct.collection_id 
       JOIN track t 
         ON t.id = ct.track_id 
       JOIN album a 
         ON a.id = t.album_id
       JOIN executor_album ea 
         ON a.id = ea.album_id 
       JOIN executor e 
         ON e.id = ea.executor_id 
      WHERE e."name" LIKE '%Nelly Furtado%';


  
