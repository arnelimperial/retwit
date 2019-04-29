from twython import Twython,TwythonStreamer
import tweepy
from dotenv import load_dotenv, find_dotenv
import requests
import time
import os

#Load environment variables
load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TOKEN_SECRET') 



# # Instatiate env variable 
twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, TOKEN_SECRET)




tar = input("Enter a word or phrase: ")
twi = twitter.search(q = tar,result_type='recent', count=100, extended=True)

finder = twi['statuses']


coder = '@ArnelGImperial'
for i in finder:
    id = i['id_str']
    tweet = i['text']
    j = i['user']
    username = j['screen_name']
    print('{} RT {}:\n\n{}\n\nRT by: {}\n\n'.format(id, username, tweet, coder))
    #print('{}\n\n{}\n\n{}'.format(id, username, tweet))

    
    twitter.update_status(status='RT {}:\n\n{}\n\nBy: {}'.format(username, tweet, coder))
    #twitter.retweet(id = id)
    #twitter.create_favorite(id = id)


#Find by ID
# status = twitter.show_status(id = '1121882631254237185')
# twitter.retweet(id = '1121882631254237185')
# twitter.create_favorite(id = '1121882631254237185')
# print(status['text'])


        

# Tweepy

# auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
# auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)



