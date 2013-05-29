/*
  We can represent sparse matrices' each cell as a record (i,j,value). 
  The benefit is that you only need one record for every non-zero element of a
  matrix.
  
  For Example:
  
  Matrix:
      0 | 2 | 1
      1 | 0 | 0
      0 | 0 | 0
      0 | 0 | 0

  can be represented as a table:
      +---- +-----+-------+
      | row | col | value |
      +---- +-----+-------+
      | 1   | 1   | 2     |
      +---- +-----+-------+
      | 1   | 3   | 1     |
      +----+------+-------+
      | 2   | 1   | 1     |
      +---- +-----+-------+

  Within matrix.db, there are two matrices A and B represented as follows:
  A(row_num, col_num, value)
  B(row_num, col_num, value)


  Express matrix multiplication as a SQL query, return the value of the
  cell (2,3)
*/


SELECT value 
FROM(
    SELECT A.row_num                as row_num, 
           B.col_num                as col_num, 
           SUM(A.value * B.value)   as value
    FROM A, B
    WHERE A.col_num = B.row_num
    GROUP BY A.row_num, B.col_num)
WHERE row_num = 2 AND col_num = 3;
