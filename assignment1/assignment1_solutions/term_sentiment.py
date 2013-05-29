'''
Computes the sentiment for the terms that do not appear in the file AFINN-111.txt
We can use certain words to deduce the sentiment of a tweet. Once you know the sentiment of the tweet, you can assign a sentiment to the other words in the tweet.

Example:
    $ python term_sentiment.py <sentiment_file> <tweet_file>

'''
import sys
import json


def computeTermSentiment(scores, tweetTexts):

    newscores = {}
    for text in tweetTexts:
        if text == None: continue

        score = 0.0
        words = text.split()
        unscored = []
        for word in words:
            if word in scores:
                score += scores[word]
            else:
                unscored.append(word)

        if len(unscored) == len(words): continue
                
        for word in unscored:
            if word in newscores:
                newscores[word].append(score)
            else:
                newscores[word] = [score]

    
    for term, score in newscores.iteritems():
        newscores[term] = sum(score) / len(score)

    #print len(newscores)

    return newscores




def main():

    sentimentFile = open(sys.argv[1], 'r')
    tweetFile = open(sys.argv[2], 'r')
    
    # Get the scores
    scores = {}
    for line in sentimentFile:
        line = unicode(line, 'utf-8')
        term, score = line.split('\t')
        scores[term] = int(score)

    # Get the tweets
    tweetTexts = []
    for line in tweetFile:
        line = unicode(line ,'utf-8')
        tweetTexts.append(json.loads(line).get(u'text'))

    sentimentFile.close()
    tweetFile.close()

    # Process the tweets
    for i in range(10):
        newscores = computeTermSentiment(scores, tweetTexts)
        scores = dict(scores, **newscores)
    
    # Output the terms' scores
    for term, score in scores.iteritems():
        term = term.replace(' ','')
        term = term.encode('utf-8')
        print term, score




if __name__ == '__main__':
    main()
    
