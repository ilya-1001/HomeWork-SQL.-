INSERT INTO genre(name)
VALUES ('Pank'), ('Pop'), ('Jazz'), ('Reggae');

INSERT INTO executor(name)
VALUES ('Sex Pistols'), ('Nelly Furtado'), ('Coldplay'), 
	   ('Duke Ellington'), ('Bill Evans Trio'), ('Bob Marley');

INSERT INTO genre_executor(genre_id, executor_id)
VALUES (1,1), (2,2), (2,3), (3,4), (3,5), (4,6);

INSERT  INTO album(name, release_year)
VALUES ('Never Mind the Bollocks, Here’s the Sex Pistols', 1977),
	   ('Whoa, Nelly!', 2000), ('Everyday Life', 2019), ('Anatomy Of a Murder', 1959), 
	   ('Explorations', 1961), ('Confrontation', 1983);

INSERT INTO executor_album (executor_id, album_id)
VALUES (1,1), (2,2), (3,3), (4,4), (5,5), (6,6);

INSERT INTO track (name, duration, album_id)
VALUES ('Anarchy in the U.K.', 212, 1), ('Holidays in the Sun', 202, 1),
	   ('I’m Like a Bird', 243, 2), ('My Love Grows Deeper', 261, 2),
	   ('Champion of the World', 257, 3), ('Everyday Life', 258, 3),
	   ('Main Title and Anatomy of a Murder', 236, 4), 
	   ('Beautiful Love', 305, 5), ('Buffalo Soldier', 256, 6),
	   ('myself', 50, 1), ('by myself', 102, 1), ('bemy self', 70, 2), 
	   ('myself by', 201, 2), ('by myself by', 107, 3), ('beemy', 154, 4), 
	   ('premyne', 129, 5), ('my', 140, 2), ('мой sql', 20, 1);

INSERT INTO collection (name, release_year)
VALUES ('Collection vol.1', 1980), ('Collection vol.2', 2021),
	   ('Collection vol.3', 2012), ('Collection vol.4', 2016),
	   ('Collection vol.5', 2019), ('Collection vol.6', 2020),
	   ('Collection vol.7', 2015), ('Collection vol.8', 2023);

INSERT INTO collection_track (collection_id, track_id)
VALUES (1,1), (1,2), (2,3), (2,4), (3,7), (3,8), (4,1), (4,7), (8,18),
	   (5,5), (5,6), (6,7), (6,9), (7,3), (7,5), (8,1), (8,7), (8,9),
	   (1,10), (1,11), (5,12), (3,13), (4,14), (8,15), (6,16), (7,17);
	
