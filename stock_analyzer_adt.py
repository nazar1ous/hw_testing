from arrays import Array
from stock_adt import Stock
import pandas as pd


class StockAnalyzer:
    def __init__(self, stocks, start=None, end=None, invest_num=None):
        self._stocks = Array(len(stocks))
        for i, stock in enumerate(stocks):
            self._stocks[i] = Stock(stock.name, start, end)
        self._profitable = None
        self._invest_num = invest_num

    def process_stocks(self, tracker):
        stocks_rate = {}
        for stock in self._stocks:
            if not stock.profit:
                stocks_rate[stock] = stock.calculate_growth(tracker)
        most_profitable = sorted(stocks_rate.items(), key=lambda x: -x[1])
        self._profitable = Array(len(most_profitable))
        self._profitable.push_list(most_profitable)
        if not self._invest_num:
            return self._profitable
        return self._profitable[:self._invest_num]

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
        sum_list = []
        for index in combined_df.index:
            sum_money = 0
            for col in combined_df.columns:
                sum_money += combined_df.loc[index][col]
            sum_list.append(sum_money)
        portfolio_df = pd.DataFrame(sum_list, columns=['Portfolio'])
        return portfolio_df


if __name__ == '__main__':
    a = StockAnalyzer(['AAPL', 'MSFT'])
    print(a.process_stocks('Adj Close'))