import tweepy as tw
import re, csv
from tweepy import OAuthHandler
from textblob import TextBlob
from datetime import datetime, timedelta

consumer_key = '####'
consumer_secret = '####'
access_token = '####'
access_secret= '####'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_term = ["Arsenal", "Chelsea", "Liverpool", "Man Utd"]

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
    
f = open('myfile.txt','a')

yesterday = datetime.now() - timedelta(1)

def twitter(lookup):
    for x in lookup:
        tweets = tw.Cursor(api.search,q=x,lang="en", since=yesterday.strftime('%Y-%m-%d')).items(50)
        tweets_no_url = [remove_url(tweet.text) for tweet in tweets]
        sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_url]
        
        for i in range(0,len(sentiment_objects)):
            f.write(str(i) + ", " + yesterday.strftime('%Y-%m-%d') + "," + x +  ", " + str(round(sentiment_objects[i].polarity,2)) + ", " + str(sentiment_objects[i]) + "\n")
    f.close()

twitter(search_term)