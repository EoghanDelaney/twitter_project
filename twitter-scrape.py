import tweepy as tw
import re, csv
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = 'xxxx'
consumer_secret = 'xxxxx'
access_token = 'xxxx'
access_secret= 'xxxxx'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tw.API(auth,wait_on_rate_limit=True)

search_term = "arsenal"

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())

tweets = tw.Cursor(api.search,q=search_term,lang="en", since='2019-03-01').items(100)


tweets_no_url = [remove_url(tweet.text) for tweet in tweets]


sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_url]


f = open('myfile.txt','r+')

for i in range(1,100):
    f.write(str(sentiment_objects[i]))

f.close()



#for tweet in tweets_no_url:
 #   f.write(str(tweet))

#f.close()