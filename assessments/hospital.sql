create database hospital
use hospital
create table patient(
patient_id int primary key,
first_name varchar(20),
last_name varchar(20),
dob date,
gender varchar(6),
contact_number varchar(12),
address varchar(50)
);
create table doctor(
doctor_id int primary key,
first_name varchar(20),
last_name varchar(20),
specialization varchar(20),
contact_number varchar(12)
);

create table appointment(
appointment_id int primary key identity(1,1),
patient_id int,
doctor_id int,
appointment_date date,
description varchar(20),
foreign key (patient_id) references patient(patient_id),
foreign key (doctor_id) references doctor(doctor_id)
);

INSERT INTO patient(patient_id,first_name,last_name,dob,gender,contact_number,address)
VALUES (1,'HARITHA','HARI','2003-09-23','FEMALE','9944459662','Pollchi'),
	   (2,'ANBU','D','2006-08-20','FEMALE','9562148623','Pollchi'),
	   (3,'ZUHI','A','1995-07-31','FEMALE','8610489995','Pollchi'),
	   (4,'JOHN','MATHEW','1986-06-29','MALE','9500335123','Pollchi'),
	   (5,'MATHEW','SINGH','2020-05-24','MALE','9487016235','Pollchi')

INSERT INTO doctor(doctor_id,first_name,last_name,specialization,contact_number)
values(1,'HARI','H','CARDIO','9612486235'),
	  (2,'LOKK','J','GENERAL','8436512795'),
	  (3,'RASS','R','ORTHO','7612549832')

INSERT INTO appointment(patient_id,doctor_id,appointment_date,description)
VALUES(1,1,'2025-06-27','surgery'),
	  (2,2,'2025-06-27','general checkup'),
	  (3,3,'2025-05-08','general checkup')