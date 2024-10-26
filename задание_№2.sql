create table if not exists genre(
	id serial primary key,
	name varchar(80) not null
);
create table if not exists executor(
	id serial primary key,
	name varchar(80) not null
);
create table if not exists genre_executor(
	genre_id integer references genre(id),
	executor_id integer references executor(id),
	constraint genre_executor_pk primary key (genre_id, executor_id)
);
create table if not exists album(
	id serial primary key,
	name varchar(80) not null,
	release_year smallint not null
);
create table if not exists executor_album(
	album_id integer references album(id),
	executor_id integer references executor(id),
	constraint executor_album_pk primary key (album_id, executor_id)
);
create table if not exists track(
	id serial primary key,
	name varchar(80) not null,
	duration integer not null,
	album_id integer references album(id)
);
create table if not exists collection(
	id serial primary key,
	name varchar(80) not null,
	release_year smallint not null
);
create table if not exists collection_track(
	collection_id integer references collection(id),
	track_id integer references track(id),
	constraint collection_track_pk primary key (collection_id, track_id)
);


