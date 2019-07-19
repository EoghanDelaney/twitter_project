import pandas as pd
import csv
from datetime import datetime as dt

today = dt.now()

weeklytotal = pd.read_csv('data/TESTweekly-totals.csv')
#group = weeklytotal[weeklytotal.Date == today.strftime('%Y-%m-%d')]
group = weeklytotal[weeklytotal.Date == '01/04/2019']