/*
  Find all documents that have more than 300 total terms, including duplicate
  terms.
*/


SELECT count(*) 
FROM
    (SELECT docid
     FROM Frequency
     GROUP BY docid
     HAVING sum(count) > 300);
