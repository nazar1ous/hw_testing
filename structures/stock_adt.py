import pandas as pd
import datetime
import yfinance as yf
import numpy as np


class Stock:
    def __init__(self, stock_name, start=None, end=None):
        self.name = stock_name
        self._data = pd.DataFrame()
        self.start, self.end = start, end
        self.process_yf()
        self._ratio_change = None
        self.profit = None

    def process_yf(self):
        self._data = yf.download(self.name, start=self.start, end=self.end)

    def calculate_change_ratio(self):
        s_change_ratio_data = self._data.apply(lambda x: np.log(x) - np.log(x.shift(1)))
        self._ratio_change = s_change_ratio_data
        return s_change_ratio_data

    def calculate_growth(self, column_name):
        if not self._ratio_change:
            self.calculate_change_ratio()
        self.profit = self._ratio_change[column_name].sum()
        return self.profit


if __name__ == "__main__":
    Stoc1 = Stock("AAPL")
    a = Stoc1.calculate_change_ratio()
    print(a)

    print(Stoc1.calculate_growth('Adj Close'))

