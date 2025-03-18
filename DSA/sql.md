### Find 3rd highest salary from employee table 
select distinct salary from employee order by salary desc limit N-1,1;
The N-1 is the limit and it skips the top N-1 values, and the 1 fetches the next value(count).

### To find top n records only
select * from employee order by salary desc limit 5;

### To find the count of employees working in department 'Admin'
select count(*) from employee where department = 'Admin';

### To find only odd rows from employee table
select * from employee where MOD(employee_id,2)<>0;
MOD(n,m) - returns n by m 
<> - not equal operator in SQL


