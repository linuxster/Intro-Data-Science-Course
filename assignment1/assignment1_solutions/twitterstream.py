import oauth2 as oauth
import urllib2 as urllib
import pycurl

# Proxy using Goagent to able to access Twitter in this script
#proxy_handler = urllib.ProxyHandler({"http": "http://127.0.0.1:8087"})  
#proxy_opener = urllib.build_opener(proxy_handler)  
#urllib.install_opener(proxy_opener)



# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "313980745-rr5BX9QxnW1NA9HVp0UmfkMCoqCuFsxAwIhTSAyr"
access_token_secret = "lmr1OKAyLQ2fXudY4neyPdtdbIB6okbIZffo9jOZNY"

consumer_key = "8cef21fsukOKuqiMJ3cBhw"
consumer_secret = "0p0MAkjwfU1Rn1mwig0G5tJvCcG7jow1ImXC49N1o"

_debug = 0



oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    
    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()
    #opener = urllib.OpenerDirector()
    
    proxy_handler = urllib.ProxyHandler({"https" : "http://127.0.0.1:8118"})  
    opener = urllib.build_opener(proxy_handler)  
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)
    #c1 = pycurl.Curl()
    #c1.setopt(pycurl.URL, url) 
    #c1.setopt(pycurl.HTTPHEADER, encoded_post_data)
    #c1.setopt(pycurl.PROXY, 'localhost')
    #c1.setopt(pycurl.PROXYPORT, 7070)
    #c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)

    #response = c1.perform()

    return response

def fetchsamples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    print "Writing data to the file..."
    outputFile = open('output.json', 'w')
    try:
        count = 0
        for line in response:
            outputFile.write(line.strip() + '\n')
            print 'Writing' + '.' * (count % 3 + 1) 
    except KeyboardInterrupt:
        outputFile.close()
        print "User exit."
        raise



if __name__ == '__main__':
    fetchsamples()
