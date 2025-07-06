# Things to remember from the SQL 50 Study Plan on LeetCode
### Select Q: Find customer referee
Table: Customer

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| referee_id  | int     |


Find the names of the customer that are not referred by the customer with id = 2.

Solution: 
**select name from Customer where referee_id <> 2 or referee_id is null;**

<> : not equal to 

# Learn and explain joins here better

### Joins Q: Replace employee id with unique Id 
Table: Employees

| Column Name   | Type    |
|---------------|---------|
| id            | int     |
| name          | varchar |


Table: EmployeeUNI

| Column Name   | Type    |
|---------------|---------|
| id            | int     |
| unique_id     | int     |

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Solution:
**select unique_id,name from Employees LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id;**

### Joins Q: Product Sales Analysis I 
Table: Sales

| Column Name | Type  |
|-------------|-------|
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |

Table: Product

| Column Name  | Type    |
|--------------|---------|
| product_id   | int     |
| product_name | varchar |

Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Solution:

**select product_name,year,price from Sales INNER JOIN Product on Sales.product_id = Product.product_id;**

**select product_name,year,price from Sales NATURAL JOIN Product;**

First way is to use equi join which returns only the records where the comparing columns have equal values

Second is to use natural join, which returns columns with the same name of associated tables will appear once only once, automatically identifies the common column.

### Joins Q: Customer Who Visited but Did not make any transactions 
Table: Visits

| Column Name | Type    |
|-------------|---------|
| visit_id    | int     |
| customer_id | int     |

Table: Transactions

| Column Name    | Type    |
|----------------|---------|
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |


Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits



### Joins Q: Rising Temperature

|Column Name   | Type    |
|---------------|---------|
| id            | int     |
| recordDate    | date    |
| temperature   | int     |

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Solution: 

**select w1.id from Weather w1, Weather w2 where DATEDIFF(w1.recordDate,w2.recordDate)=1 and w1.temperature > w2.temperature;**

**select w1.id from Weather w1 JOIN Weather w2 ON DATEDIFF(w1.recordDate,w2.recordDate)=1 WHERE w1.temperature > w2.temperature;**


- Weather w1, Weather w2: Creates two copies (aliases) of the Weather table (w1 and w2) using old-style cross join.

- DATEDIFF(w1.recordDate, w2.recordDate) : Calculates number of days between w1.recordDate and w2.recordDate.

- DATEDIFF(w1.recordDate, w2.recordDate) = 1	: Filters to keep only rows where w1 is exactly 1 day after w2.

- w1.temperature > w2.temperature	: Filters to keep only rows where today's (w1) temperature is higher than yesterday's (w2) temperature.

#### Joins Q: Average Time of process per machine
There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.

select a.machine_id, round(avg(b.timestamp - a.timestamp),3) as processing_time from Activity a INNER JOIN Activity b on a.machine_id = b.machine_id and a.process_id = b.process_id and a.activity_type = 'start' and b.activity_type = 'end' group by a.machine_id;

### Aggregate Functions Q: Not Boring movies

| Column Name    | Type     |
|----------------|----------|
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Solution:
**select * from Cinema where MOD(id,2) = 1 and description <> "boring" order by rating desc;**


MOD(id,2) : checks for divisibility with 2

### Sorting : Product Sales Analysis III 

| Column Name | Type  |
|-------------|-------|
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |

Write a solution to find all sales that occurred in the first year each product was sold. For each product_id, identify the earliest year it appears in the Sales table.Return all sales entries for that product in that year. Return a table with the following columns: product_id, first_year, quantity, and price. Return the result in any order.

select product_id, year as first_year, quantity, price from Sales where (product_id, year) in (select product_id, min(year) from Sales group by product_id);



### Aggregate func: Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

**select Prices.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) as average_price from Prices LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id and purchase_date between start_date and end_date group by Prices.product_id;**





