CREATE TABLE  Employee (
	emp_id INT PRIMARY KEY,
	emp_name VARCHAR(50),
	salary INT ,
	dept_id INT
);

CREATE TABLE  Departments (
	dep_id INT PRIMARY KEY,
	dep_name VARCHAR(50)
);

INSERT INTO Employee (emp_id ,emp_name , dept_id, salary) VALUES
(1 ,"rushi",10,20000),
(2 ,"ankit",20,30000),
(3 ,"rohan",30,40000),
(4,"rohan",40,30000),
(5 ,"Nilu",NULL,50000);

INSERT INTO  Departments (dep_id ,dep_name) VALUES
(10,"HR"),
(20,"IT"),
(30,"sales");

DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Departments;

SELECT * FROM Employee;
SELECT * FROM Departments;

/*    2nd highest salary       */
SELECT MAX(salary)
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

/*    max salary       */
SELECT MAX(salary)
FROM Employee

/*   whoes max salary       */
SELECT emp_name , salary
FROM Employee
WHERE salary = (SELECT MAX(salary) From Employee);

/*   3rd High salary       */
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

/*  JOIN Combines row from 2 or more table
INNER jOIN - return matching value from both table    */
SELECT e.emp_id , e.emp_name , d.dep_name
FROM Employee e 
INNER JOIN Departments d 
ON e.dept_id=d.dep_id;

/*   LEFT jOIN - return  all row from left table
and matching value from Right table    */


SELECT e.emp_id , e.emp_name , d.dep_name
FROM Employee e
LEFT JOIN Departments d 
ON e.dept_id=d.dep_id;

/*   RIGHT jOIN - return  all row from right table
and matching value from Left table    */

SELECT e.emp_id , e.emp_name , d.dep_name
FROM Departments d
LEFT JOIN  Employee e   /*  Here RIGHT JOIN is not supported hence we tried to exchnage table  */
ON e.dept_id=d.dep_id;

/* FULL OUTER JOIN - return  all row from both table matching & nonmatching table    */

/* CROSS JOIN--> Join each row of 1st table with each row of table 2nd  */
SELECT e.dept_id ,e.emp_id ,d.dep_name
FROM Employee e
CROSS JOIN Departments d;

/* Self join -- table join it self   */



SELECT emp_name, COUNT(*)
FROM Employee 
GROUP By emp_name
HAVING COUNT(*)>1;

