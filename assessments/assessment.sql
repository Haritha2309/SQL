create database assessment
use assessment;

create table vehicle(
car_id int primary key identity(1,1),
make varchar(20),
model varchar(20),
year int,
daily_rate decimal(4,2),
available int,
passenger_capacity int,
engine_capacity int
);
insert into vehicle(make,model,year,daily_rate,available,passenger_capacity,engine_capacity)
values('Toyota','Camry',2022,50.00,1,4,1450),
      ('Honda','Civic',2023,45.00,1,7,1500),
      ('Ford','Focus',2022,48.00,0,4,1400),
      ('Nissan','Altima',2023,52.00,1,7,1200),
      ('Chevrolet','Malibu',2022,47.00,1,4,1800),
      ('Hyundai','Sonata',2023,49.00,0,7,1400),
      ('BMW','3 Series',2023,60.00,1,7,2499),
      ('Mercedes','C-Class',2022,58.00,1,8,2599),
      ('Audi','A4',2022,55.00,0,4,2500),
      ('Lexus','ES',2023,54.00,1,4,2500);

select* from vehicle

create table customer(
customer_id int primary key identity(1,1),
first_name varchar(20),
last_name varchar(20),
email varchar(50),
phonenumber varchar(12)
);

insert into customer ( first_name,last_name,email,phonenumber)
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

select* from customer

create table lease(
lease_id int primary key identity(1,1),
car_id int,
customer_id int,
startdate date,
end_date date,
lease_type varchar(10)
foreign key(car_id) references vehicle(car_id),
foreign key (customer_id) references customer(customer_id)
);

insert into lease(car_id,customer_id,startdate,end_date,lease_type)
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

select* from lease

create table payment(
payment_id int primary key identity(1,1),
lease_id int,
payment_date date,
amount decimal(7,2),
foreign key(lease_id) references lease(lease_id)
);

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

select * from payment

--queries

-- 1. daily rate of mercedes to 68
update vehicle set daily_rate = 68
where make = 'Mercedes'
select daily_rate
from vehicle
where make = 'Mercedes'

--2. delete a customer
 delete from payment
 where lease_id in (select lease_id from lease where customer_id=2)
 delete from lease
 where customer_id =2
 delete from customer
 where customer_id=2
 select* from customer

--3. rename payment date to transaction date
EXEC sp_rename 'Payment.payment_Date','transaction_Date','COLUMN'
select* from payment

--4. FIND SPECIFIC CUSTOMER BY EMAIL
select*
from customer
where email = 'robert@example.com'

--5. get active lease 
update lease
set end_date='2025-07-03'
where customer_id=3

select*
from lease
where end_date>='2025-06-17'

--6. payment made by specific phno
select phonenumber, SUM(amount) as total_amount
from lease
join payment on payment.lease_id=lease.lease_id
join customer on customer.customer_id=lease.customer_id
group by phonenumber

--7. average daily rate of cars
select AVG(daily_rate) as average
from vehicle

--8. highest daily rate 
select *
from vehicle
where daily_rate=(select max(daily_rate)
from vehicle)

--9. all cars leased by specific customer
select lease.customer_id, count(vehicle.car_id) as total_cars
from lease
join customer on lease.customer_id=customer.customer_id
join vehicle on lease.car_id= vehicle.car_id
group by lease.customer_id 
order by total_cars desc

--10. details of most recent lease
select *
from lease
order by end_date desc

--11. all payments made in 2023
select * 
from payment
where payment_date>='2023-01-01'

--12. customers not made any payment
select * 
from customer
where customer_id not in (select customer_id
from lease
where lease_id  in ( select lease_id
from payment)
)

--13. car details and their total payment
select v.car_id,v.make,v.model,v.year, v.daily_rate,v.passenger_capacity,v.engine_capacity,sum(p.amount)as total
from vehicle v 
join lease l on l.car_id=v.car_id
join payment p on p.lease_id=l.lease_id
group by v.car_id,v.make,v.model,v.year, v.daily_rate,v.passenger_capacity,v.engine_capacity

--14. total payment for each customer
select customer.customer_id, first_name+last_name as name,email,phonenumber,sum(amount)as total
from  customer
join lease on lease.customer_id=customer.customer_id
join payment on payment.lease_id=lease.lease_id
group by customer.customer_id,customer.first_name,customer.last_name,customer.email,customer.phonenumber

--15. car details for each lease
select l.lease_id, v.car_id,v.make,v.model,v.year, v.daily_rate,v.passenger_capacity,v.engine_capacity
from lease l
join vehicle v on l.car_id=v.car_id

--16. car and customer details with active leases
select l.lease_id,
       c.first_name +' ' +last_name as name,
       c.email,
       c.phonenumber,
       v.make,
       v.model,
       v.daily_rate
from lease l
join customer c on l.customer_id=c.customer_id
join vehicle v on l.car_id=v.car_id
where end_date>='2025-06-17'

--17.  customer spent most on leases
select top 1 c.*, sum(p.amount) as maxm
from customer c
join lease l on l.customer_id=c.customer_id
join payment p on p.lease_id=l.lease_id
group by c.customer_id,c.email,c.phonenumber,c.first_name,c.last_name
order by maxm desc
 
--18. all cars with current lease info
select v.*
from vehicle v
join lease l on l.car_id=v.car_id
where l.end_date>='2025-06-17'

--Find employees whose salaries are greater than the average salary of their respective departments (using a join in the subquery)
emp id, salary name, deptid

select e.emp_id,e_salary

where e.salary>(select avg(salary)
from employees ee
join departments dd on dd.dept_id = ee.dept_id)