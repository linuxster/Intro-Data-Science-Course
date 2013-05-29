#!/usr/bin/env python
# encoding: utf-8
"""
frequency.py

Created by Pete Colligan on 2013-05-10.
Copyright (c) 2013 Peter Colligan. All rights reserved.

File Inputs: output.txt

"""

import sys
import json
import string,re



def get_dic(tweet_file):
    dic = {}
    count = 0.0
    for t in tweet_file:
        tweet = json.loads(t)
        eachtweet= tweet.get('text', '')
        if eachtweet:
            t_text = clean(eachtweet)
            for word in t_text:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
                count += 1
    return count, dic

def clean(tweet):
    tweet = tweet.lower()
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    words = tweet.split()
    return words

def print_fre(count, dic):
    for word in dic:
        print word.encode("utf-8"), dic[word]/count

def main():
    tweet_file = open(sys.argv[1])
    count, dic = get_dic(tweet_file)
    print_fre(count, dic)
    tweet_file.close()

if __name__ == '__main__':
    main()
