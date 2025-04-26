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
*select name from Customer where referee_id <> 2 or referee_id is null;*
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
*select unique_id,name from Employees LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id;*








