import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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
        if "text" in tweet:
            score = 0.0
            t_text = tweet["text"].split()
            for word in t_text:
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
