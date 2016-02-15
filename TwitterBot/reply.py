import tweepy, time, os
from keys import *
from random import randint
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing"
api.update_status(status = status)
