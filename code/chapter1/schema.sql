
    drop table if exists html;
    create table html (
    id integer primary key autoincrement,
    url text not null,
    html text not null
    );
    