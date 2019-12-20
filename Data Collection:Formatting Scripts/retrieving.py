djia = ['JPM', 'MSFT', 'JNJ', 'UNH', 'CAT',	'AABA',	'HD', 'CVX', 'MMM', 'AMZN',	'CSCO','XOM', 'VZ', 'WMT', 'GS', 'AAPL', 'AXP', 'GOOGL', 'UTX', 'KO', 'MRK', 'TRV',	'IBM', 'INTC', 'PFE', 'GE',	'DIS', 'PG', 'BA', 'MCD', 'NKE']

import pandas as pd
import pandas_datareader.data as web
import datetime as dt

for i in djia:
    start = dt.datetime(1990,1,1)
    end = dt.datetime(2019, 12, 16)
    df = web.DataReader(i, 'yahoo', start, end)
    df.to_csv("djia_long/" + i + ".csv")
print(df.head())