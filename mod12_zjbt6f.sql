--Write a query to calculate the payments each sales agent is responsible for. Display the agent name and the total payments.
SELECT a.agent_name, SUM(c.payment_amt) AS "Total Payments"
FROM agents a, customer c
WHERE a.agent_code = c.agent_code
GROUP BY a.agent_code;

--Write a query to calculate payments for each sales agent by country of the sales agent. 
--Display the agent country and total payments.
SELECT a.country, SUM(c.payment_amt) AS "Total Payments"
FROM agents a, customer c
WHERE a.agent_code = c.agent_code 
GROUP BY a.country;

--Calculate the commission for each order. Display order id, customer name, agent name, and commission amount.
SELECT o.ord_num, c.cust_name, a.agent_name, SUM(a.commission) AS "Commision Amount"
FROM agents a, customer c, orders o
WHERE a.agent_code = c.agent_code AND c.agent_code = o.agent_code
GROUP BY o.ord_num, c.cust_name;

--In the customers table, for customers from New York update the CUST_CITY value to change it from “New York” to “NY”.
UPDATE customer
SET cust_city = 'NY'
WHERE cust_city = 'New York';
--A. Now write an query to select all customers from New York City.
SELECT cust_name, cust_city
FROM customer
WHERE cust_city = 'NY';

--Increase the commission for sales agents from London by 20%.
UPDATE agents
SET commission = commission *.20
WHERE country = 'London';

--B. Calculate the commission for each order where the agent is from London. 
--Display order id, customer name, agent name, and commission amount.
SELECT o.ord_num, c.cust_name, a.agent_name, SUM(a.commission) AS "Commision Amount"
FROM agents a, customer c, orders o
WHERE a.agent_code = c.agent_code AND c.agent_code = o.agent_code AND a.country = 'London'
GROUP BY o.ord_num, c.cust_name;

--Update customers with grade 2 to grade 3.
UPDATE customer
SET grade = 3
WHERE grade = 2;

--C. Select all customers names and customer codes with grade 3.
SELECT cust_name, cust_code, grade
FROM customer
WHERE grade = 3;

--Delete sales agents from Bangalore.
DELETE FROM agents
WHERE working_area = 'Bangalore';

--E. Write a query to select all columns for all sales agents
SELECT * FROM agents;

--Delete customers whose name begins with the letter “S”.
DELETE FROM customer
WHERE cust_name LIKE 'S%';
--F. Select all columns for all customers.
SELECT * FROM customer;