import tweepy
import pandas as pd 
from pymongo import MongoClient, ASCENDING, TEXT

# Twitter API credentials
access_token='1129351733715570688-CblRgAL7R5Pk0yFzS3QMaVccEgs8Vq'
access_secret='Sy7yLyyQEVATDKja1eg0pJKZFiMevHq2j5G9LHq3rNKMA'

consumer_key='2rFTPEzyUKyXdvgjsDj5zd5T6'
consumer_secret='n0zVa1iDaWr3rDmxfHerqaN5I3Cdtq06L5OV4ef9NxXAIOycJc'

# Accessing Twitter 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Increasing timeout limit and setting retries
api = tweepy.API(auth, wait_on_rate_limit=True, timeout=300, retry_count=3, retry_delay=5, retry_errors=set([503]))

try:
    api.verify_credentials()
    print("Authenticated")
except tweepy.TweepyException as e:
    print(f"Error during authentication: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
