'''
Computes the ten most frequently occurring hash tags from the data.

Example:
    $ python top_ten.py <tweet_file>

Output:
    baz 30.0

'''

import sys
import json

from operator import itemgetter

def main():

    tweetFile = open(sys.argv[1])

    allHashtags= []

    for line in tweetFile:
        tweet = json.loads(line)
        
        if 'entities' not in tweet: continue
        
        hashtags = tweet['entities'].get('hashtags')
        if hashtags == None or hashtags == []: continue

        for hashtag in hashtags:
            allHashtags.append(hashtag['text'])


    hashtagCounts = {}
    for hashtag in allHashtags:
        if hashtag not in hashtagCounts : hashtagCounts[hashtag] = 1.0
        else                            : hashtagCounts[hashtag] += 1.0


    top10Counts = sorted(hashtagCounts.iteritems(), key = itemgetter(1), reverse = True)[:10]

    for hashtag, count in top10Counts:
        print hashtag, count   

if __name__ == '__main__':
    main()


