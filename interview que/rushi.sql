CREATE TABLE  Employee {
	emp_id INT PRIMARY KEY,
	emp_name VARCHAR(50),
	dept_id INT
};

CREATE TABLE  Departments {
	dep_id INT PRIMARY KEY,
	dep_name VARCHAR(50),
};

INSERT INTO Employee (emp_id ,emp_name , dept_id) VALUES
(1 ,"rushi",10),
(2 ,"ankit",20),
(3 ,"rohan",30),
(4 ,"Nilu",NULL);

INSERT INTO  Departments (dep_id ,dep_name) VALUES
(10,"HR")
(20,"IT")
(30,"sales");

SELECT * FROM Employee;


