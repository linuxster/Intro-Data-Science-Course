#!/usr/bin/env python
# encoding: utf-8
"""
term_sentiment.py

Created by Pete Colligan on 2013-05-10.
Copyright (c) 2013 Peter Colligan. All rights reserved.

File Inputs: AFINN-111.txt output.txt

"""
import sys
import json
import string,re

def clean(tweet):
        #tweet = tweet.lower()
        #tweet = re.sub('[%s]'%re.escape(string.punctuation), '', tweet)
        words = tweet.split()
        return words

def main():
   #get tweet data and sentiment dict
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #initialize result dict
   result = {}

   #set up scores dict
   scores = {}
   for line in sent_file.readlines():
        term, score = line.split('\t')
        scores[term] = int(score)

    #get tweets and calculate scores
   for line in tweet_file.readlines():
        tweet_line = json.loads(line)
        eachtweet= tweet_line.get('text', '')
        words = clean(eachtweet)
        if words:
          score = 0
          templist = []
          for word in words:
            word = word.encode('utf-8')
            try:
                score += scores[word]
            except:
                templist.append(word)


          #define scores for words not in dict
          if score == 0:
             tweetscore = 0
          elif score > 0:
             tweetscore = 1
          else:
             tweetscore = -1

          #store scores in result dict
          for word in templist:
             result[word] = result.get(word,0) + tweetscore

    #print out result
   for key in result:
        print "%s %.3f"%(key,result[key])

if __name__ == '__main__':
    main()