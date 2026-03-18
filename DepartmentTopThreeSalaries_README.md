Department Top Three Salaries (SQL)
A specialized SQL solution for identifying the top 3 unique earners within each department. This approach is designed to handle salary ties gracefully using window functions.

Problem Overview
The goal is to extract a list of employees who earn one of the top three salaries in their respective departments. This requires grouping data by department and ranking salaries in descending order while ensuring that ties do not skip ranking positions.

The Logic
The query uses a layered approach to process the data:

Partitioning: Data is split into logical "buckets" by departmentId.

Ranking: Within each bucket, the DENSE_RANK() function assigns a rank based on the salary. Unlike RANK(), DENSE_RANK() ensures that if two employees share the #1 spot, the next highest salary is still ranked #2.

Joining: The ranked subquery is joined with the Department table to replace ID codes with human-readable department names.

Filtering: A final WHERE clause limits the output to only those with a rank of 3 or higher.

Key Query Features
Window Functions: Utilizes OVER (PARTITION BY ... ORDER BY ...) for efficient row-level calculations.

Tie-Handling: Guaranteed to include all employees who fall within the top three unique salary brackets.

Scalability: This pattern is the industry standard for "Top-N" reporting in PostgreSQL, MySQL (8.0+), and SQL Server.

Example Output

Department      Employee      Salary
  IT              Joe          85000
  IT              Max          90000
  Sales           Henry        80000
  Sales           Sam          60000
