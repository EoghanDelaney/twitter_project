import tweepy as tw
import re, csv
import textblob as tb
from tweepy import OAuthHandler
from textblob import TextBlob
from datetime import datetime, timedelta

consumer_key = 'rOmb7myVdbdY7B5ah1YTMev8d'
consumer_secret = 't074h7YozMiTndn4TbJScAtIvIruxnnzBUMBhQxFwe7TmZQEKZ'
access_token = '3091692196-VFmVlipwi5PahGGJMsSJDxyrIJzMowI3Q941dPP'
access_secret= 'FvADxKkdvquAlKCcTwJFlE5cAU245HgA1iuuyOC16egrD'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)

#search_term = ["Arsenal", "Chelsea", "Liverpool", "Man Utd", "Man City", "Spurs", "Wolves", "Everton", "Fulham", "West Ham", "Leicester", "Newcastle", "Watford", "Swansea", "Crystal Palace", "Burnley", "Cardiff", "Brigthon", "Huddersfield", "Bournemouth"]
search_term = ["Arsenal",	"Bournemouth",	"Brighton",	"Burnley",	"Cardiff",	"Chelsea",	"Crystal Palace",	"Everton",	"Fulham",	"Huddersfield",	"Leicester",	"Liverpool",	"Man City",	"Man Utd",	"Newcastle",	"Southampton",	"Spurs",	"Watford",	"West Ham",	"Wolves"]

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
    
f = open('data/sentiment.csv','a')

yesterday = datetime.now() - timedelta(1)

def twitter(lookup, num):
    for x in lookup:
        tweets = tw.Cursor(api.search,q=x,lang="en", since=yesterday.strftime('%Y-%m-%d')).items(num)
        tweets_no_url = [remove_url(tweet.text) for tweet in tweets]
        sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_url]
        
        for i in range(0,len(sentiment_objects)):
            f.write(str(i) + ", " + yesterday.strftime('%Y-%m-%d') + "," + x +  ", " + str(round(sentiment_objects[i].polarity,2)) + ", " + str(sentiment_objects[i]) + "\n")
    f.close()

twitter(search_term, 100)