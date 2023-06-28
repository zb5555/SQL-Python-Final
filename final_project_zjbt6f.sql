--Write a query to create a view named “EmployeesPerRegion” 
--that shows the region_name and the number of employees from that region in a column called “Number of Employees”.
CREATE VIEW EmployeesPerRegion AS
SELECT r.region_name, COUNT(e.employee_id) AS "Number of Employees"
FROM employees e, departments d, locations l, countries c, regions r
WHERE e.department_id = d.department_id AND d.location_id  = l.location_id AND l.country_id = c.country_id AND c.region_id = r.region_id
GROUP BY  r.region_name;

-- 1 Query the EmployeesPerRegion to show the number of employees from the Americas.
SELECT * FROM EmployeesPerRegion WHERE region_name = 'Americas';

-- for final project
SELECT * FROM EmployeesPerRegion;

--Write a query to create a view named “managers” to display all the managers. 
--Include the manager’s name (first, last), phone number, email, job title, and department name.
CREATE VIEW managers AS 
SELECT e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
FROM employees e, jobs j, departments d 
WHERE j.job_id = e.job_id AND e.department_id = d.department_id AND e.employee_id IN (SELECT manager_id FROM employees);

-- 2 Query the managers view to show the number of managers in each department.
SELECT department_name, COUNT(first_name) FROM managers GROUP BY department_name;

--Write a query to create a view named “DependentsByDepartment” to get a count of how many dependents there are in each department.
CREATE VIEW DependentsByDepartment AS 
SELECT d.department_name, COUNT(de.dependent_id) AS "Number_of_Dependents"
FROM departments d, dependents de, employees e 
WHERE d.department_id = e.department_id AND e.employee_id = de.employee_id
GROUP BY d.department_name;

--Query the DependentsByDepartment view to show the department with the largest number of dependents. 
-- 3 This should show the department name and the number of dependents.
SELECT * FROM DependentsByDepartment ORDER BY Number_of_Dependents DESC LIMIT 2;

--for final project
SELECT * FROM DependentsByDepartment;

--Write a query to create a view named “HiresByYear” that calculates the number of employees hired each year. Remember the SQL $year function.
CREATE VIEW HiresByYear AS
SELECT YEAR(hire_date) AS "Year" , COUNT(employee_id) AS "Number_of_Employees_hired"
FROM employees 
GROUP BY Year;

-- 4 Query the HiresByYear view to show the number of hires in 1997.
SELECT * FROM HiresByYear;

--Write a query to create a view named “SalaryByDepartment” to calculate total salaries for each department.
CREATE VIEW SalaryByDepartment AS 
SELECT d.department_name, SUM(e.salary) 
FROM employees e, departments d 
WHERE e.department_id = d.department_id
GROUP BY d.department_name;

-- 5 Query the SalaryByDepartment view to show the total salary for the Finance department.
SELECT * FROM SalaryByDepartment WHERE department_name = 'Finance';

--Write a query to create a view named “SalaryByJobTitle” to calculate total salaries for each job title.
CREATE VIEW SalaryByJobTitle AS 
SELECT j.job_title, SUM(e.salary) AS "Total_Salary"
FROM jobs j, employees e 
WHERE j.job_id = e.job_id
GROUP BY j.job_title;

-- 6 Query the SalaryByJobTitle view to show the job title and total salary for the title with the highest total salary.
SELECT * FROM SalaryByJobTitle;

--Write a query to create a view named “EmployeeDependents” that calculates the number of dependents each employees has. 
--This query should show employees even if they have 0 dependents. 
--Display the employee name (first, last), email, phone number, and number of dependents. Hint: left or right join.
CREATE VIEW EmployeeDependents AS
SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.dependent_id) AS "Number_of_Dependents"
FROM employees e 
LEFT JOIN dependents d ON e.employee_id = d.employee_id
GROUP BY e.first_name, e.last_name, e.email, e.phone_number;

--  7 Query the EmployeeDependents view to show employees with no children". 
--Show employee name (first, last), email, phone number, and number of dependents.
SELECT * FROM EmployeeDependents;

--Write a query to create a view named “CountryLocation” that calculates the number of locations in each country. 
--This query should show countries even if they have 0 locations. Display the country name and number of locations.
CREATE VIEW CountryLocation AS
SELECT c.country_name, COUNT(l.location_id) AS "Number_of_Locations"
FROM countries c
LEFT JOIN locations l ON c.country_id = l.country_id
GROUP BY c.country_name;

--  8 Query the CountryLocation view to show countries with no locations". Show country name and number of locations.
SELECT * FROM CountryLocation;