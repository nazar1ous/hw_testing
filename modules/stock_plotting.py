import io
import base64
import matplotlib.pyplot as plt
from structures.stock_analyzer_adt import StockAnalyzer
from structures.stock_adt import Stock


class StockPlotting:
    def __init__(self, lst_stocks, target_data, start, end, invest_num):
        self._stocks = lst_stocks
        self.analyzer = StockAnalyzer(lst_stocks, start, end, invest_num=invest_num)
        self._data = StockAnalyzer.get_combined_stock_dataframe(lst_stocks, target_data)
        self.tracker = target_data

    @staticmethod
    def get_img_source(plot_figure):
        img = io.BytesIO()
        plot_figure.savefig(img, format='png',
                            bbox_inches='tight')
        img.seek(0)
        encoded = base64.b64encode(img.getvalue())
        source_to_img = 'data:image/png;base64, {}'.format(encoded.decode('utf-8'))
        return source_to_img

    def get_plot_figure(self):
        self._data.plot(grid=True)
        figure = plt.figure(1)
        return figure

    def plot_portfolio(self):
        portfolio_df = self.analyzer.get_portfolio_df(self.tracker)
        portfolio_df.plot(grid=True)
        fig = plt.figure(1)
        return self.get_img_source(fig)

    def plot_ratio(self):
        data_ratio = self.analyzer.get_ratio_df(self.tracker)
        data_ratio.plot(grid=True).axhline(y=1, color="black", lw=2)
        fig = plt.figure(2)
        return self.get_img_source(fig)


def main():
    a = Stock('AAPL')
    print(a._data)
    stocks = [Stock('AAPL'), Stock('MSFT'), Stock('GOLD')]
    plotter = StockPlotting(stocks, 'Adj Close')
    # plotter.plot_ratio()
    plotter.plot_portfolio()

# main()