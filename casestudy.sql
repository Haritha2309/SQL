create database case_study
use case_study

create table vehicle(
vehicle_id int primary key identity(1,1),
vehicle_make varchar(20),
vehicle_model varchar(20),
vehicle_year int,
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

insert into vehicle(vehicle_make,vehicle_model,vehicle_year,daily_rate,vehicle_status,passenger_capacity,engine_capacity)
values('Toyota','Camry',2022,50.00,'Available',4,1450),
      ('Honda','Civic',2023,45.00,'Available',7,1500),
      ('Ford','Focus',2022,48.00,'Available',4,1400),
      ('Nissan','Altima',2023,52.00,'Available',7,1200),
      ('Chevrolet','Malibu',2022,47.00,'Available',4,1800),
      ('Hyundai','Sonata',2023,49.00,'Available',7,1400),
      ('BMW','3 Series',2023,60.00,'Not Available',7,2499),
      ('Mercedes','C-Class',2022,58.00,'Not Available',8,2599),
      ('Audi','A4',2022,55.00,'Not Available',4,2500),
      ('Lexus','ES',2023,54.00,'Available',4,2500);

insert into customer ( first_name,last_name,email,phone_number)
values('John','Doe','johndoe@example.com','555-555-5555'),
      ('Jane','Smith','janesmith@example.com','555-123-4567'),
      ('Robert','Johnson','robert@example.com','555-789-1234'),
      ('Sarah','Brown','sarah@example.com','555-456-7890'),
      ('David','Lee','david@example.com','555-987-6543'),
      ('Laura','Hall','laura@example.com','555-234-5678'),
      ('Michael','Davis','michael@example.com','555-876-5432'),
      ('Emma','Wilson','emma@example.com','555-432-1098'),
      ('William','Taylor','william@example.com','555-321-6547'),
      ('Olivia','Adams','olivia@example.com','555-765-4321');

insert into lease(vehicle_id,customer_id,start_date,end_date,type)
values(1,1,'2023-01-01','2023-01-05','Daily'),
      (2,2,'2023-02-12','2023-02-28','Monthly'),
      (3,3,'2023-03-10','2023-03-15','Daily'),
      (4,4,'2023-04-20','2023-04-30','Monthly'),
      (5,5,'2023-05-05','2023-05-10','Daily'),
      (6,3,'2023-06-15','2023-06-30','Monthly'),
      (7,7,'2023-07-01','2023-07-10','Daily'),
      (8,8,'2023-08-12','2023-08-15','Monthly'),
      (3,3,'2023-09-07','2023-09-10','Daily'),
      (10,10,'2023-10-10','2023-10-31','Monthly');

insert into payment( lease_id,payment_date,amount)
values(1,'2023-01-02',200.00),
      (2,'2023-02-20',1000.00),
      (3,'2023-03-12',75.00),
      (4,'2023-04-25',900.00),
      (5,'2023-05-07',60.00),
      (6,'2023-06-18',1200.00),
      (7,'2023-07-03',40.00),
      (8,'2023-08-14',1100.00),
      (9,'2023-09-09',80.00),
      (10,'2023-10-25',1500.00);

ALTER TABLE vehicle
ALTER COLUMN daily_rate NUMERIC(10,2)

select * from vehicle