import pandas as pd

df = pd.read_csv('flaskapp/dashboard1/yfinance/nasdaqtraded.txt', sep = '|')
valid_tickers = df['Symbol'].to_list()
