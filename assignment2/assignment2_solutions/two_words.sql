/*
   Count the number of unique documents that contain both the word 
   'transactions' and the word 'world'.
*/


SELECT count(docid)
FROM Frequency
WHERE 
    term = 'transactions' AND 
    docid in(
        SELECT docid 
        FROM Frequency
        WHERE term = 'world');
