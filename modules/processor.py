from structures.stock_adt import Stock
from modules.stock_plotting import StockPlotting


def plot_portfolio(stocks_names, start=None, end=None, invest_num=None):
    s, e = start, end
    stocks = [Stock(name) for name in stocks_names]
    plotter = StockPlotting(stocks, 'Adj Close', s, e, invest_num)
    return plotter.plot_portfolio()


def plot_ratio_change(stocks_names, start=None, end=None, invest_num=None):
    s, e = start, end
    stocks = [Stock(name) for name in stocks_names]
    plotter = StockPlotting(stocks, 'Adj Close', s, e, invest_num)
    return plotter.plot_ratio()


# print(date_start)