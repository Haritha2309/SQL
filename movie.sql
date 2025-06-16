USE Movies;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Movie_cast;
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Seat;
DROP TABLE IF EXISTS Screen;
CREATE TABLE Screen(
Screen_ID int identity(1,1) PRIMARY KEY,
name varchar(50),
class_type varchar(10), 
capacity int
);
INSERT INTO Screen(name, class_type, capacity)
VALUES('john', 'gold', 5),
		('joel', 'siler', 5),
		('riya', 'iron', 5),
		('neetha', 'gold', 5),
		('karthi', 'iron', 5);
CREATE TABLE Seat(
Seat_id INT PRIMARY KEY,
Seat_no varchar(10),
Screen_ID INT,
FOREIGN KEY(Screen_ID) REFERENCES Screen(Screen_ID)
);
INSERT INTO Seat(Seat_ID,Seat_no,Screen_ID)
VALUES(123,'10a',1),
		(456,'10b',2),
		(789,'10c',3),
		(112,'10d',4);
/*SELECT *
FROM Seat;*/
CREATE TABLE Movie(
Movie_ID int Primary key,
title varchar(255),
genre varchar(50),
rating DECIMAL(3,1),
status VARCHAR(20),
POSTER VARCHAR(255),
);
INSERT INTO Movie(Movie_ID,title,genre,rating,Status,poster)
VALUES(989,'thug life', 'overrated', 2.5, 'bad', 'urlll'),
	(789,'maaran', 'okie', 9.5, 'good', 'urlll'),
	(456,'maaman', 'good', 5.5, 'avg', 'urlll'),
	(890,'KGF', 'mass', 8.5, 'fine', 'urlll');
/*Select*
from Movie;*/
CREATE TABLE Movie_cast(
Cast_ID int PRIMARY KEY,
Movie_ID int FOREIGN KEY REFERENCES Movie(Movie_ID),
person varchar(100),
role varchar(100),
);
INSERT INTO Movie_cast(Cast_ID, Movie_ID, person,role)
VALUES(209,989,'simb', '2nd lead'),
	(210,789,'simb', '2nd lead'),
	(211,456,'trisha', '2nd lead'),
	(212,890,'trisha', '2nd lead');
SELECT Count(*) AS trisha
FROM Movie_cast
WHERE person = 'trisha';

UPDATE Movie_cast
SET person = 'SAM'
WHERE person='trisha';
--Select person, cOUNT(*) AS Total_persons
Select*
from Movie_cast
--GROUP BY person
--ORDER BY Movie_ID DESC
ORDER BY Cast_ID 
--OFFSET 1 ROWS FETCH NEXT 3 ROWS ONLY

/*CREATE TABLE Review(
review_ID int primary key,
content text,
review_date date,
reviewer_name varchar(100),
Movie_ID int foreign key references Movie(Movie_ID)
);

INSERT INTO Review(review_ID,content,review_date,reviewer_name,Movie_ID)
VALUES(765,'WOW', '2003-09-23','MAARAN',890),
	(775,'WOW', '2003-09-23','MAARAN',789),
	(785,'WOW', '2003-09-23','MAARAN',456),
	(735,'WOW', '2003-09-23','MAARAN',909),
	(795,'WOW', '2003-09-23','MAARAN',989);
----****** INNER JOIN ****------
/*SELECT Movie.Movie_ID,
	Movie.title,
	Movie.rating,
	Review.reviewer_name,
	Review.content
FROM Movie
INNER JOIN Review
ON Review.Movie_ID = Movie.Movie_ID;*/

--------****** FULL OUTER JOIN***-----
/*SELECT*
FROM Review
Full outer join Movie
on Review.Movie_ID = Movie.Movie_ID;*/

-------***** LEFT JOIN ****----
/*SELECT *
FROM Movie
Left join Review
ON Review.Movie_ID = Movie.Movie_ID;*/

-----*** RIGHT JOIN*** ----
/*SELECT *
FROM Review
Right join Movie
ON Movie.Movie_ID = Review.Movie_ID;*/

CREATE TABLE SHOW(
Show_ID int Primary key,
Show_date string,
Screen_ID int FOREIGN KEY REFERENCES Screen(Screen_ID),
Movie_ID int foreign KEY REFERENCES Movie(Movie_ID)
);
*/
SELECT *, COUNT(*) AS noum
FROM Movie_cast
WHERE Movie_ID IN (SELECT Movie_ID
FROM Movie
WHERE genre='overrated')
GROUP BY person