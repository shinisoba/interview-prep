### Things to remember from the SQL 50 Study Plan on LeetCode
#### Q: Find customer referee
Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
Find the names of the customer that are not referred by the customer with id = 2.

Solution: 
*select name from Customer where referee_id <> 2 or referee_id is null;*
<> : not equal to 

