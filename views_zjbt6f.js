//Write a query to create a view named "custByCity" to get a count of how many customers there are in each city.
//Query the custByCity view to show the number of customers in Singapore.
db.createView(
    "custByCity",
    "customers",
    [
    {$match:{"city" : "Singapore"}},
    {$group:{_id: "$city", numberOfCustomers:{$sum:1}}},
    {$sort: {numberOfCustomers:-1}}
]
)

//Write a query to create a view named "paymentsByMonth" that calculates payments per month. 
//You will have to group by multiple columns for this query: month and year because payments from January 2004 and January 2005 should not be grouped together. Remember the SQL month() and year() functions.
//Query the paymentsByMonth view to show payments in November 2004
db.createView(
    "paymentsByMonth",
    "customers",
    [
    {$unwind:"$payments"},
    {$addFields:{"Year": {$year:"$payments.paymentDate"}, "Month":{$month:"$payments.paymentDate"}}},
    {$match:{"Month":11, "Year": 2004}},
    {$group:{_id:"$Month", TotalPayments:{$sum:1}}},
    {$sort:{TotalPayments: 1}}
])

//Write a query to create a view named "orderTotalsByMonth" to calculate order totals (in dollars) per month.
//Query the orderTotalsByMonth view to show the order total in August 2004.
db.createView(
    "orderTotalsByMonth",
    "orders",
    [
    {$unwind:"$orderDetails"},
    {$addFields:{"Year": {$year:"$orderDate"}, "Month":{$month:"$orderDate"}}},
    {$match:{"Month":8, "Year": 2004}},
    {$group:{_id: "$Month"}}, 
    {$project:{totalValue:{$multiply:["$orderDetails.priceEach", "$orderDetails.quantityOrdered"]}}}
])

//Write a query to create a view named "productSalesYear" that calculates sales per product per year. 
//Include the product name, sales total, and year.
//Query the productSalesYear view to show the sales per year for the "2001 Ferrari Enzo"
db.createView(
    "productSalesYear",
    "orders",
    [
    {$unwind:"$orderDetails"},
    {$addFields:{"Year": {$year:"$orderDate"}, "Month":{$month:"$orderDate"}}},
    {$match:{"orderDetails.productName": "2001 Ferrari Enzo" }},
    {$group:{_id: "$Year"}}, 
    {$project:{totalValue:{$multiply:["$orderDetails.priceEach", "$orderDetails.quantityOrdered"]}}}
])

//Write a query to create a view named "orderTotals" that displays the order total for each order. 
//Include order number, customer name, and total.
//Query the orderTotals view to select the top 15 orders.
db.createView(
    "orderTotals",
    "orders",
    [
    {$unwind:"$orderDetails"},
    {$group:{_id:"$customerName", Total:{$sum:1}}},
    {$sort: {Total:-1}},
    {$project:{_id:1, customerName:1, Total:1}},
    {$limit:15}
])