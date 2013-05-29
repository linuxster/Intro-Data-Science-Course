/*
   Write a SQL statement to count the number of documents containing the word
   “parliament”
*/

SELECT count(docid)
FROM Frequency
WHERE term = 'parliament';
