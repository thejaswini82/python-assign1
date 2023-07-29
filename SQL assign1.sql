CREATE DATABASE aka;
drop database aka;
USE aka;

CREATE TABLE SalesPeopl (
  Snum INT PRIMARY KEY,
  Sname VARCHAR(255) UNIQUE,
  City VARCHAR(255),
  Comm DECIMAL(5, 2)
);

SELECT COUNT(*) AS CountOfSalesperson
FROM SalesPeopl
WHERE Sname LIKE 'A%' OR Sname LIKE 'a%';

USE aka;

CREATE TABLE Customers (
  Cnum INT PRIMARY KEY,
  Cname VARCHAR(255),
  City VARCHAR(255) NOT NULL,
  Snum INT,
  FOREIGN KEY (Snum) REFERENCES SalesPeopl(Snum)
);

USE aka;

CREATE TABLE Orders (
  Onum INT PRIMARY KEY,
  Amt DECIMAL(8, 2),
  Odate DATE,
  Cnum INT,
  Snum INT,
  FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
  FOREIGN KEY (Snum) REFERENCES SalesPeopl(Snum)
);

INSERT INTO Customers (Cnum, Cname, City, Snum) VALUES
(2001, 'Hoffman', 'London', 1001),
(2002, 'Giovanni', 'Rome', 1003),
(2003, 'Liu', 'Sanjose', 1002),
(2004, 'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', 1001),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);


INSERT INTO Orders (Onum, Amt, Odate, Cnum, Snum) VALUES
(3001, 18.69, '1990-03-10', 2008, 1007),
(3003, 767.19, '1990-03-10', 2001, 1001),
(3002, 1900.10, '1990-03-10', 2007, 1004),
(3005, 5160.45, '1990-03-10', 2003, 1002),
(3006, 1098.16, '1990-03-10', 2008, 1007),
(3009, 1713.23, '1990-04-10', 2002, 1003),
(3007, 75.75, '1990-04-10', 2004, 1002),
(3008, 4273.00, '1990-05-10', 2006, 1001),
(3010, 1309.95, '1990-06-10', 2004, 1002),
(3011, 9891.88, '1990-06-10', 2006, 1001);

SELECT S.Snum, S.Sname
FROM SalesPeopl AS S
WHERE S.Snum IN (
    SELECT O.Snum
    FROM Orders AS O
    GROUP BY O.Snum
    HAVING SUM(O.Amt) > 2000
);


SELECT COUNT(*) AS CountOfSalespersonInNY
FROM SalesPeopl
WHERE City = 'Newyork';

SELECT City, COUNT(*) AS CountOfSalesperson
FROM SalesPeopl
WHERE City IN ('London', 'Paris')
GROUP BY City;


SELECT S.Snum, S.Sname, O.Onum, O.Odate
FROM SalesPeople AS S
JOIN Orders AS O ON S.Snum = O.Snum;



 

