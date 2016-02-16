import tweepy, time, os
from keys import *
from random import randint
from datetime import datetime, timedelta


CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
argfile = str("liners.txt")
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

while True:
    trends = api.trends_place(12589066) 
    hashtags = [x['name'] for x in trends[0]['trends'] if x['name'].startswith('#')]

    trend_hashtag = hashtags[0]

    tweetSearchResults = api.search(q=trend_hashtag,count=50)     
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()
    
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
 
 
    for tweet in tweetSearchResults:
        screenName = tweet.user.screen_name
        message = f[randint(0,len(f)-1)] 
        message = "@{0}, {1} {2}".format(sn, message,trend_hashtag) 
        print message
        status = api.update_status(status=m, in_reply_to_status_id = tweet.id)
        
        TimeToSleep = randint(120,480)
        time.sleep(TimeToSleep)
    
    
    TimeToSleep = randint(3600,4000)
    time.sleep(TimeToSleep)