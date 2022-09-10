set global sql_mode = 'ansi';

drop database if exists library;
create database library;
use library;

create table user
(
    id       int auto_increment,
    name     varchar(200)     not null,
    admin    bool default (0) not null,
    password varchar(50)      not null,
    primary key (id)
);

create table user_phone
(
    id    int,
    phone varchar(15),
    primary key (id, phone),
    foreign key (id) references user (id)
);

create table author
(
    id   int,
    name varchar(200) not null,
    primary key (id)
);


create table  publisher
(
    id int,
    name varchar(200),
    primary key(id)
);

create table category
(
    id  int,
    name varchar(200) not null,
    primary key(id)
);


create table book
(
    issn         int,
    title        varchar(200) not null,
    submission   date         not null,
    edition      int          not null,
    price_buy    int          not null,
    price_borrow int,
    author       int          not null,
    publisher int,
    category int not null,
    primary key (issn),
    foreign key (author) references author (id),
    foreign key (publisher) references publisher (id),
    foreign key (category) references category(id)
);

create table client
(
    id int,
    primary key (id),
    foreign key (id) references user (id)
);

create table address
(
    id      int auto_increment,
    client  int          not null,
    address varchar(500) not null,
    primary key (id),
    foreign key (client) references client (id)
);

create table shipping_officer
(
    id              int,
    wages_per_order decimal(15, 2) not null,
    vehicle_type    varchar(100)   not null,
    primary key (id),
    foreign key (id) references user (id)
);

create table orders
(
    id     int auto_increment,
    client int                    not null,
    rate   int check(rate >= 1 and  rate <= 5),
    status enum ('Order', 'Done'),
    date_  date default(current_date) not null,
    primary key (id),
    foreign key (client) references client (id)
);

create table orders_book
(
    orders int,
    book   int,
    primary key (orders, book),
    foreign key (orders) references orders(id),
    foreign key (book) references book(issn)
);

create table shipping
(
    id int,
    status enum('any'),
    delivery_date date,
    address int not null,
    primary key(id),
    foreign key (id) references orders(id),
    foreign key (address) references address(id)
);


create  table bills
(
    id int auto_increment,
    date_ date default(current_date),
    publisher int not null,
    primary key(id),
    foreign key (publisher) references publisher(id)
);


create table supply
(
    count int not null,
    price_per_unit decimal(15, 2),
    book int not null,
    bills int not null,
    primary key(book, bills),
    foreign key (book) references book(issn),
    foreign key (bills) references bills(id)
);


create table payment
(
    order_ int,
    total decimal(15, 2) not null,
    type  enum('cash', 'Visa', 'MasterCard') not null,
    primary key (order_),
    foreign key (order_) references orders(id)
);


create table borrow
(
    order_ int,
    expected_return date,
    actual_return date,
    primary key (order_),
    foreign key (order_) references orders(id)
);


#  A be should 16 tables (11-02-2022 8:42 PM)
show tables;

