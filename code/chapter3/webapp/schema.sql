drop table if exists store;
create table store(
	id integer primary key autoincrement,
	name text not null,
	email text not null
);
