--Write a query to create a view named "SFEmployees" for those salespeople who work in the San Francisco office. 
--Include the employee name (first, last), number, email, and job title.
--Query the SFEmployees view to count the number of employees in the San Francisco office.
CREATE VIEW SFEmployees AS
SELECT o.city, COUNT(e.employeeNumber) AS "Number of Employees"
FROM offices o, employees e 
WHERE e.officeCode = o.officeCode AND o.officeCode = '1';

--Write a query to create a view named "managers" to display all the managers. 
--Include the manager’s name (first, last), number, email,  job title, and office city.
--Query the managers view to show the number of managers in each city.
CREATE VIEW managers AS
SELECT e.reportsTo, e.firstName, e.lastname, e.extension, e.email, e.jobTitle, o.city
FROM employees e, offices o 
WHERE e.officeCode = o.officeCode
GROUP BY reportsTo;

--Write a query to create a view named "custByCity" to get a count of how many customers there are in each city.
--Query the custByCity view to show the number of customers in Singapore.
CREATE VIEW custByCity AS
SELECT city, COUNT(customerNumber) AS "Number of Customers"
FROM customers
WHERE city = "Singapore";

--Write a query to create a view named "paymentsByMonth" that calculates payments per month.
--You will have to group by multiple columns for this query: 
--month and year because payments from January 2004 and January 2005 should not be grouped together. 
--Remember the SQL month() and year() functions.
--Query the paymentsByMonth view to show payments in November 2004
CREATE VIEW paymentsByMonth AS
SELECT COUNT(checkNumber) AS "Payments per Month"
FROM payments
WHERE YEAR(paymentDate) = 2004 AND MONTH(paymentDate) = 11;

--Write a query to create a view named "orderTotalsByMonth" to calculate order totals (in dollars) per month.
--Query the orderTotalsByMonth view to show the order total in August 2004.
CREATE VIEW orderTotalsByMonth AS
SELECT SUM(od.quantityOrdered * od.priceEach) AS "Dollar Amount of Orders"
FROM orderdetails od, orders o
WHERE YEAR(orderDate) = 2004 AND MONTH(orderDate) = 8;

--Write a query to create a view named "salesPerLine" that calculates sales per product line.
--Query the salesPerLine view to show the total sales for the "Classic Cars" line.
CREATE VIEW salesPerLine
SELECT p.productline, SUM(od.quantityOrdered * od.priceEach) AS "Dollar Amount"
FROM products p, orderdetails od
WHERE p.productLine = "Classic Cars";

--Write a query to create a view named "productSalesYear" that calculates sales per product per year. 
--Include the product name, sales total, and year.
--Query the productSalesYear view to show the sales per year for the "2001 Ferrari Enzo"
CREATE VIEW productSlesYear AS
SELECT p.productName, YEAR(o.orderDate), SUM(od.quantityOrdered * od.priceEach)
FROM products p, orders o, orderdetails od
WHERE p.productCode = od.productCode AND o.orderNumber = od.orderNumber AND p.productName = "2001 Ferrari Enzo"
GROUP BY p.productName, YEAR(o.orderDate);

--Write a query to create a view named "orderTotals" that displays the order total for each order. 
--Include order number, customer name, and total.
--Query the orderTotals view to select the top 15 orders.
CREATE VIEW orderTotals AS
SELECT o.ordernumber, c.customerName, SUM(od.quantityOrdered) AS "ORDER TOTAL"
FROM customers c, orders o, orderdetails od
WHERE c.customerNumber = o.customerNumber AND o.orderNumber = od.orderNumber
GROUP BY o.orderNumber
ORDER BY SUM(od.quantityOrdered) DESC
LIMIT 15;

--Write a query to create a view named "salesPerRep" that calculates total sales for each sales rep.
CREATE VIEW salesPerRep AS 
SELECT c.salesRepEmployeeNumber, SUM(p.amount)
FROM customers c, payments p
WHERE c.customerNumber = p.customerNumber
GROUP BY c.salesRepEmployeeNumber;

--Write a query to create a view named "salesPerOffice" that displays sales per office.
CREATE VIEW salesPerOffice AS
SELECT e.officeCode, SUM(p.amount) AS "TOTAL SALES"
FROM employees e, customers c, payments p
WHERE e.employeeNumber = c.salesRepEmployeeNumber AND c.customerNumber = p.customerNumber
GROUP BY e.officeCode;