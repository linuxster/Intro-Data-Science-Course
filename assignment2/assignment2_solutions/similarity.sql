/**
    Term-document matrix

    The reuters dataset can be considered a term-document matrix, which is an 
    important representation for text analytics.
    Each row of the matrix is a document vector, with one column for every term
    in the entire corpus. Naturally, some documents may not contain a given 
    term, so this matrix is sparse. The value in each cell of the matrix is the
    term frequency. 

    For Example:
        Doc  | is | do | will | then

        doc1 | 1  | 0  | 0    | 1
        doc2 | 0  | 1  | 1    | 0
    
    Just multiply the matrix with its own transpose S = DDT, and you have an 
    (unnormalized) measure of similarity.
    
    The result is a square document-document matrix, where each cell represents
    the similarity. Here, similarity is pretty simple: if two documents both
    contain a term, then the score goes up by the product of the two term
    frequencies. This score is equivalent to the dot product of the two document
    vectors.

    Compute the similarity matrix DD'.
    Hint:The query could take some time to run if you compute the entire result.

    Return the similarity of the tow documents '10080_txt_crude' and 
    '17035_txt_earn'.
**/



SELECT similarity
FROM(
    SELECT  F1.docid as docid1, 
            F2.docid as docid2, 
            SUM(F1.count * F2.count) as similarity 
    FROM Frequency as F1, Frequency as F2
    WHERE F1.term = F2.term AND
          F1.docid = '10080_txt_crude' AND 
          F2.docid = '17035_txt_earn'
   GROUP BY F1.docid, F2.docid);


/** TO DO
    
    1.Use tf-idf insted of raw frequency to weight term frequnecy
    2.Use cosine similarity to normalize the similarity.
    
    These need to write extended sqlite functions
    
**/
