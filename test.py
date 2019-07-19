import tweepy as tw
import re, csv
import textblob as tb
from tweepy import OAuthHandler
from textblob import TextBlob
from datetime import datetime, timedelta

consumer_key = 'tSPldIATTB6mMx9Q7crvpfJGj'
consumer_secret = 'qqy4VCmDvG776HgNxjREecqJeHJV0eweYS8LsoC4dKELSqtcwm'
access_token = '3091692196-DBUXTMIpv4I7ytlgiVSVfbE4qJVzP4EHzNJB5Iv'
access_secret= 'HzYOriqDT15ytwzGeDjeQb0rbSE0Nyli6bfQ3menawDxN'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_term = ["#loveisland"]


def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
    
f = open('data/eoghanhasisland.csv','a')

#yesterday = datetime.now() - timedelta(1)

def twitter(search_term, num):
    tweets = tw.Cursor(api.search,q=search_term,lang="en").items(num)
    for x in tweets:
        f.write(str(x.created_at) + "," + str(TextBlob(remove_url(x.text)).polarity)  + "," + str(TextBlob(remove_url(x.text))) + "\n")

twitter(search_term, 1000)


#tweepy.Cursor(api.search, q="cool", since="2015-01-30", until="2015-02-01", lang="en").items(100):