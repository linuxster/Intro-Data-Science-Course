import sys
import json
import string,re

def clean(tweet):
        tweet = tweet.lower()
        tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
        words = tweet.split()
        return words

def main():
   #get tweet data and sentiment dict
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #set up scores dict
   scores = {}
   for line in sent_file.readlines():
        term, score = line.split('\t')
        scores[term] =int(score)


   #get tweets and calculate scores
   for line in tweet_file.readlines():
        tweet_line = json.loads(line)
        eachtweet= tweet_line.get('text', '')
        if eachtweet:
           words = clean(eachtweet)
           score = 0
           for word in words:
               word = word.encode('utf-8')
               score += scores.get(word,0)
        print word,float(score)


if __name__ == '__main__':
    main()
