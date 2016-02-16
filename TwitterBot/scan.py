import tweepy, random, time
from keys import *

auth = tweepy.OAuthHander(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class Scanner:
	# consumer_key= keys['consumer_key']
	# consumer_secret= keys['consumer_secret']
	# access_token= keys['access_token']
	# access_token_secret= keys['access_token_secret']
    def scanner(self):
        while True:
            trends = api.trends_place(12589066) #WOE
            hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]
            print("Searching...")
            trend_hashes = hashtags[0]
            tweetSearchResults = api.search(q=trend_hashes, count = 50)
            print(hashtags)
            sleepTime = random.randint(120, 600)
            print("Sleeping...")
            time.sleep(sleepTime)

scan = Scanner()
scan.scanner()