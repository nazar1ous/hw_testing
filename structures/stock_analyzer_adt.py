from structures.arrays import Array
from structures.stock_adt import Stock
import pandas as pd
import datetime


class StockAnalyzer:
    def __init__(self, stocks, start=None, end=None, invest_num=None):
        self._stocks = Array(len(stocks))
        for i, stock in enumerate(stocks):
            self._stocks[i] = Stock(stock.name, start, end)
        self._profitable = None
        if invest_num:
            try:
                self._invest_num = int(invest_num)
            except ValueError:
                self._invest_num = None
        else:
            self._invest_num = None

    def process_stocks(self, tracker):
        stocks_rate = {}
        for stock in self._stocks:
            if not stock.profit:
                stocks_rate[stock] = stock.calculate_growth(tracker)
        most_profitable = sorted(stocks_rate.items(), key=lambda x: -x[1])
        self._profitable = Array(len(most_profitable))
        self._profitable.push_list(most_profitable)
        if not self._invest_num or self._invest_num >= len(self._stocks):
            return self._profitable
        return self._profitable.slice(0, self._invest_num)

    @staticmethod
    def get_combined_stock_dataframe(stocks, target_data):
        stocks_frames = []
        for stock in stocks:
            stock_name = stock.name
            stock_frame = stock._data
            stocks_frames.append((stock_name, stock_frame))

        combined_frame = pd.DataFrame({item[0]: item[1][target_data]
                                       for item in stocks_frames})
        return combined_frame

    def get_ratio_df(self, tracker):
        if not self._profitable:
            self.process_stocks(tracker)
        combined_df = self.get_combined_stock_dataframe([item[0] for item in self._profitable],
                                                        target_data=tracker)
        return combined_df.apply(lambda x: x / x[0])

    def get_portfolio_df(self, tracker):
        if not self._profitable:
            self.process_stocks(tracker)
        combined_df = self.get_combined_stock_dataframe([item[0] for item in self._profitable],
                                                        target_data=tracker)
        portfolio_df = pd.DataFrame(combined_df.sum(axis=1, skipna=True), columns=['Portfolio'])
        return portfolio_df


if __name__ == '__main__':
    s, e = '2020-1-1', datetime.date.today().strftime('%Y-%m-%d')
    a = StockAnalyzer([Stock('AAPL', s, e), Stock('MSFT', s, e)])
    print(a.process_stocks('Adj Close'))
    print(a.get_portfolio_df('Adj Close'))