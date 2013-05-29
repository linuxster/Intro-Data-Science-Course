'''
Compute the term frequency histogram of the livestream data.

The frequency of a term can be calculate with the following formula:
    [# of occurrences of the term in all tweets]/
    [# of occurrences of all terms in all tweets]

Example:
    $ python frequency.py <tweet_file>

Output:
    <term:string> <frequency:float>

'''

import sys
import json

def main():

    tweetFile = open(sys.argv[1])

    allWords = []

    for line in tweetFile:
        tweetText = json.loads(line).get(u'text')
        if tweetText != None:
            allWords.extend(tweetText.split())

    totalWordsNum = len(allWords)

    termNums = {}
    for word in allWords:
        if word not in termNums : termNums[word] = 1.0
        else                    : termNums[word] += 1.0

    termFrequencies = {}
    for term, termNum in termNums.iteritems():
        termFrequencies[term] = termNum / totalWordsNum
        print term, termFrequencies[term]

if __name__ == '__main__':
    main()



