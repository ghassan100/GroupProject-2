drop table if exists link;
    create table link (
        id integer primary key,
        Date  DATE not null,
        Time Time  not null,
        Transection integer not null,
        Item Text not null
);

