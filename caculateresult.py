import pandas
import csv
from datetime import datetime as dt

today = dt.now()

weeklytotal = pandas.read_csv('data/TESTweekly-totals.csv')
#group = weeklytotal[weeklytotal.Date == today.strftime('%Y-%m-%d')]
group = weeklytotal[weeklytotal.Date == '16/03/2019']