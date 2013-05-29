#!/usr/bin/env python
# encoding: utf-8
"""
happiest_state.py

Created by Pete Colligan on 2013-05-10.
Copyright (c) 2013 Peter Colligan. All rights reserved.

File Inputs: output.txt

"""
import sys
import json
import string,re

def get_score(tweet, dic):
    eachtweet= tweet.get('text', '')
    if eachtweet:
        t_text = clean(eachtweet)
    score = 0.0
    for word in t_text:
        if word in dic:
            score += dic[word]
    return score

def clean(tweet):
    tweet = tweet.lower()
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    words = tweet.split()
    return words

def get_dic(sent_file):
    dic = {}
    for entry in sent_file:
        entry_list = entry.split()
        if len(entry_list) == 2:
            dic[entry_list[0]] = float(entry_list[1])
        else:
            entry_name = ""
            for i in range(0, len(entry_list) - 1):
                entry_name += entry_list[i]
            dic[entry_name] = float(entry_list[-1])
    return dic


def find_state(dic, tweet_file):
    hash_state = {}
    for line in tweet_file:
        t = json.loads(line)
        if "text" in t:
            place = t["place"]
            if place != None:
                if place["country_code"] == "US":
                    state = place["full_name"][-2:]
                    score = get_score(t, dic)
                    if state in hash_state:
                        hash_state[state] += score
                    else:
                        hash_state[state] = score
    if len(hash_state) == 0:
        print "none"
    max = -100000
    hap = ""
    for state in hash_state:
        if hash_state[state] > max:
            max = hash_state[state]
            hap = state
    print hap






def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dic = get_dic(sent_file)
    sent_file.close()
    find_state(dic, tweet_file)
    tweet_file.close()




if __name__ == '__main__':
    main()