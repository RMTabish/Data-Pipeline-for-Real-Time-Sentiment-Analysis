
import tweepy
import pandas as pd 
from pymongo import MongoClient, ASCENDING, TEXT


access_token='1129351733715570688-CblRgAL7R5Pk0yFzS3QMaVccEgs8Vq'
access_secret='Sy7yLyyQEVATDKja1eg0pJKZFiMevHq2j5G9LHq3rNKMA'

consumer_key='2rFTPEzyUKyXdvgjsDj5zd5T6'
consumer_secret='n0zVa1iDaWr3rDmxfHerqaN5I3Cdtq06L5OV4ef9NxXAIOycJc'

#connecting with mongodb cluster

mongodb_conn=MongoClient('mongodb+srv://raimuhammadtabish:Z7tfY4E0kQQidP3B@twittersentiment.arfyts3.mongodb.net/?retryWrites=true&w=majority&appName=twitterSentiment')
db=mongodb_conn.demo
tweet_collection=db.tweet_collection
