/**
    If we can compute the similarity of two documents, we can compute the 
    similarity of a query with a document. You can imagine taking the union of
    the keywords represented as a small set of (docid, term, count) tuples with
    the set of all documents in the corpus, then recomputing the similarity
    matrix.

    Find the best matching document to the keyword query:
    "washington taxes treasury"
**/


CREATE VIEW Frequency_with_query AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


SELECT MAX(similarity)
FROM(
    SELECT F2.docid as docid, SUM(F1.count * F2.count) as similarity 
    FROM Frequency_with_query as F1, Frequency_with_query as F2
    WHERE F1.term = F2.term AND
          F1.docid = 'q' 
    GROUP BY F1.docid, F2.docid);

