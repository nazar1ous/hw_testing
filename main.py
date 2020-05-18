from stock_adt import Stock
from stock_plotting import StockPlotting


def main():
    a = Stock('AAPL')
    print(a._data)
    stocks = [Stock('AAPL'), Stock('MSFT'), Stock('GOLD')]
    plotter = StockPlotting(stocks, 'Adj Close')
    return plotter.plot_portfolio()
    # plotter.plot_ratio()
    # plotter.plot_portfolio()


def main2():
    a = Stock('AAPL')
    print(a._data)
    stocks = [Stock('AAPL'), Stock('MSFT'), Stock('GOLD')]
    plotter = StockPlotting(stocks, 'Adj Close')
    return plotter.plot_ratio()
    # plotter.plot_ratio()
    # plotter.plot_portfolio()
