__author__ = 'i809999'

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

pyresponse = json.load(response)

results = pyresponse["results"]

for i in range(10):
    print results[i]["text"]