#!/usr/bin/env python
# encoding: utf-8
"""
tweet_sentiment.py

Created by Pete Colligan on 2013-05-10.
Copyright (c) 2013 Peter Colligan. All rights reserved.

File Inputs: AFINN-111.txt output.txt

"""

import sys
import json
import string,re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def clean(tweet):
    tweet = tweet.lower()
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    words = tweet.split()
    return words

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = {}
    for sent in sent_file:
        phrase = sent.split()
        if len(phrase) == 2:
            sent_dict[phrase[0]] = float(phrase[1])
        else:
            key = ""
            length = len(phrase)
            for e in range(0, length - 1):
                key += phrase[e]
            sent_dict[key] = float(phrase[-1])
    sent_file.close()
    #a = 1
    for t in tweet_file:
        tweet = json.loads(t)
        eachtweet= tweet.get('text', '')
        if eachtweet:
            t_text = clean(eachtweet)
            score = 0.0
            for word in t_text:
                word = word.encode('utf-8')
                if word in sent_dict:
                    score += sent_dict[word]
            # if a == 2:
                # print t_text
            print score
            # a += 1
    tweet_file.close()
    # print a
    #hw()
    #lines(sent_file)
    #lines(tweet_file)


if __name__ == '__main__':
    main()
