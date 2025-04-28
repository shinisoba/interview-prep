# Things to remember from the SQL 50 Study Plan on LeetCode
#### Select Q: Find customer referee
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

#### Joins Q: Replace employee id with unique Id 
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

#### Joins Q: Product Sales Analysis I 
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

#### Joins Q: Customer Who Visited but Did not make any transactions 
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











#### Aggregate Functions Q: Not Boring movies

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




