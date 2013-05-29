'''
Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet.
The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

Example:
    
    $ python tweet_sentiment.py <sentiment_file> <tweet_file>

'''

import sys
import json

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Get the scores
    scores = {}
    for line in sentiment_file:
        term, score = line.split('\t')
        scores[term] = int(score)

    # Get the tweets
    tweetTexts = []
    for line in tweet_file:
        tweetTexts.append(json.loads(line).get(u'text'))

    # Process the tweets
    for text in tweetTexts:
        score = 0.0
        if text != None:
            words = text.split()
            for word in words:
                score += scores.get(word, 0)
        print score


if __name__ == '__main__':
    main()
