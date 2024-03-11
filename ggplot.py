import yfinance as yf
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
# start = dt.datetime(2015, 1, 1)
# end = dt.datetime(2020, 12, 31)

# # Fetch historical data using yfinance
# df = yf.download('TSLA', start=start, end=end)
# df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# print(df.head())
df['Adj Close'].plot()
plt.show()