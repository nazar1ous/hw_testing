import pandas as pd
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

start = datetime.datetime(2010, 1, 1)
end = datetime.date.today()
# print(str(start))
apple = yf.download("AAPL", start=start, end=end)
apple["20d"] = np.round(apple["Adj Close"].rolling(window = 20, center = False).mean(), 2)
apple["50d"] = np.round(apple["Adj Close"].rolling(window = 50, center = False).mean(), 2)
apple["200d"] = np.round(apple["Adj Close"].rolling(window = 200, center = False).mean(), 2)
apple["20d"].plot()
apple["50d"].plot()
apple["200d"].plot()
plt.show()
# print(apple)
# n = start.day
# d = datetime.date.today() - datetime.timedelta(days=20)
# df1 = yf.download("AAPL", start=d, end=end)["Adj Close"]
# print(df1)
# df1["20d"] = np.round(yf.download("AAPL", start=d, end=end)["Adj Close"].rolling(window=1, center=False).mean(), 2)
# print(df1["20d"])
# print(d)
# apple["20d"] = np.round(apple["Adj Close"].rolling(window=20, center=False).mean(), 2)
# print(apple["20d"])

# pandas_candlestick_ohlc(apple.loc['2016-01-04':'2016-12-31', :], otherseries="20d", adj=True)
