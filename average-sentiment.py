import pandas
import csv
from datetime import datetime as dt

today = dt.now()

def loaddaily():
    sentiment_file = pandas.read_csv('data/sentiment.csv')
    weeklytotal = open('data/weekly-totals.csv','a')
    group = (sentiment_file.groupby('Team')['Polar'].mean()).tolist()
    group.insert(0,today.strftime('%Y-%m-%d'))
    csv.writer(weeklytotal).writerow(group)
    weeklytotal.close()


loaddaily()