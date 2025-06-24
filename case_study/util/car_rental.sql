create database car_rental
use car_rental

create table vehicle(
vehicle_id int primary key identity(1,1),
vehicle_make varchar(20),
vehicle_model varchar(20),
daily_rate decimal(4,2),
vehicle_status varchar(20),
passenger_capacity int,
engine_capacity int
);

create table customer(
customer_id int primary key identity(1,1),
first_name varchar(20),
last_name varchar(20),
email varchar(50),
phone_number varchar(12)
);

create table lease(
lease_id int primary key identity(1,1),
vehicle_id int,
customer_id int,
start_date date,
end_date date,
type varchar(10),
foreign key (vehicle_id) references vehicle(vehicle_id),
foreign key (customer_id) references customer(customer_id)
);

create table payment(
payment_id int primary key identity(1,1),
lease_id int,
payment_date date,
amount decimal(6,2)
foreign key (lease_id) references lease(lease_id)
);

