'''
Returns the name of the happiest state as a string.
Script should print the two letter state abbreviation to stdout.

Example:
    $ python happiest_state.py <sentiment_file> <tweet_file>

Output:
    CA

'''

import sys
import json

def main():

    sentimentFile = open(sys.argv[1])
    tweetFile = open(sys.argv[2])

    # Get the scores
    scores = {}
    for line in sentimentFile:
        term, score = line.split('\t')
        scores[term] = int(score)


    # Get the tweet with state information
    stateTweets = []
    for line in tweetFile:
        tweet = json.loads(line)
        if tweet.get('text') == None : continue


        # Get state
        state = None
        if tweet.get('place') != None:
            if tweet['place'].get('country_code') != 'US' and tweet['place'].get('country') != 'United States':
                continue

            placeFullName = tweet['place'].get('full_name')
            if placeFullName != None : 
                try:
                    state = placeFullName.split()[1]
                except IndexError:
                    print placeFullName
                    return

        elif tweet['user'].get('loaction') != None:
            state = tweet['user'].get('loaction')

        if state == None: continue

        if len(state) == 2:
            stateTweets.append((state, tweet['text']))

    stateScores = {}
    for stateTweet in stateTweets:
        state = stateTweet[0]
        text = stateTweet[1]

        score = 0.0
        words = text.split()
        for word in words:
            score += scores.get(word, 0)

        if state in stateScores:
            stateScores[state] += score
        else:
            stateScores[state] = score

    happiestState = (None, 0)
    for state, score in stateScores.iteritems():
        if score > happiestState[1]:
            happiestState = state, score

    print happiestState[0]


if __name__ == '__main__':
    main()

        
        


    


        


        
        

    



