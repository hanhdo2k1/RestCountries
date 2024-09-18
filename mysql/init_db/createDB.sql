-- create database dbCountries;
use dbCountries;
create table country
(
	id int auto_increment primary key,
    name varchar(50),
    independent bit,
    status varchar(255),
    region varchar(100),
    area double,
    googleMaps text,
    population long,
    timezones varchar(100),
    continents varchar(100),
    flag text
);
create table currency
(
	id_currency int auto_increment primary key,
    type varchar(50),
    name varchar(200),
    symbol varchar(50),
    id_country int,
    foreign key(id_country) references country(id) ON DELETE CASCADE
);

create table capital
(
	id_capital int auto_increment primary key,
    name varchar(255),
    id_country int,
    foreign key(id_country) references country(id) ON DELETE CASCADE
);