DROP TABLE IF EXISTS orders
DROP TABLE IF EXISTS customer
DROP TABLE IF EXISTS products
CREATE TABLE customer(
c_id int primary key identity(1,1),
c_name varchar(50),
email varchar(50),
city varchar(20),
c_date date
);
insert into customer(c_name,email,city,c_date)
values('john','hohn@gmail.com','pollachi','2025-09-01'),
	  ('jerom','jerom@gmail.com','chennai','2025-09-01'),
	  ('josh','josh@gmail.com','tripur','2025-09-01');

create table products(
p_id int primary key  identity(1,1),
p_name varchar(50),
p_category varchar(50),
price decimal(7,2),
stock int
);
insert into products(p_name,p_category,price,stock)
values('laptop','electronics',45000.00,50),
      ('phone','electronics',30000.00,12),
	  ('table','furniture',15000.00,30);

create table orders(
o_id int primary key identity(1,1),
c_id int,
p_id int,
quantity int,
o_date date,
t_price decimal(9,2),
foreign key(c_id) references customer(c_id),
foreign key(p_id) references products(p_id)
);
insert into orders(c_id,p_id,quantity,o_date,t_price)
values(1, 1, 3,'2025-09-01',350000.00),
      (2, 2, 4,'2025-06-01',450000.00),
	  (3, 3, 3,'2025-08-01',350500.00);

select* from customer;
select * from products;
select * from orders;

-- join practise
select c_name AS customers,
c_date, o_date,t_price,quantity,p_category
from customer
join orders on customer.c_id = orders.c_id
 join products on products.p_id = orders.p_id
 order by p_category

 -- distinct
 select distinct p_category , quantity
 from products
 join orders on orders.p_id= products.p_id
 where quantity between 2 and 3 

 -- sum
 select sum(t_price) as profit , p_category
 from orders
 join products on products.p_id = orders.p_id
 group by p_category

 -- c_name of the customer with high price bsd on ctry
 select top 1
 MAX(t_price) as maxim,c_name,p_category
 from orders
 join products on orders.p_id =products.p_id
 join customer on orders.c_id = customer.c_id
 group by c_name,p_category
-- order by t_price 
-- fetch 1 row only

-- 2nd highest
select  top 1 t_price as maxm,c_name,p_category
from orders
join products on orders.p_id =products.p_id
 join customer on orders.c_id = customer.c_id
 where t_price<(select max(t_price)
 from orders)
 --group by c_name,p_category
 order by t_price desc

 select c_id,c_name,email,(select count (*)
 from orders
 where orders.c_id=customer.c_id) as total
 from customer

 alter table customer 
 add  ref_id int ;

 update customer
 set ref_id = NULL
 where c_id=1

 update customer
 set ref_id=1
 where c_id=2
 
 update customer 
 set ref_id =2
 where c_id=3

/* with ref_tree as(
 select c_id,c_name,ref_id,
 0 as level
 from customer
 where ref_id null
 union all

 select c_id,c_name,ref_id,ref_tree+1 as level
 from customer
 join ref_tree on customer.ref_id=ref_tree.c_id
 )
 select c_id,c_name,ref_id,level
 from customer
 order by level,c_id*/

  select*
  from customer

  create procedure cus_city @ city nvarchar(50)
  as
  begin
  select c_id,c_name,email,city,c_date
  from customer
  where city = @city;
  end;
