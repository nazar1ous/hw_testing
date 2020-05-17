import pandas as pd
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import numpy as np


class Stock:
    """Represent a stock for financial purposes"""
    def __index__(self, name):
        pass


def get_stock_dataframe(stocks_namelist, target_data, start, end=None):
    stocks_frames = []
    for stock_name in stocks_namelist:
        stock_frame = yf.download(stock_name, start=start, end=end)
        stocks_frames.append((stock_name, stock_frame))

    combined_frame = pd.DataFrame({item[0]: item[1][target_data]
                                   for item in stocks_frames})
    combined_frame.head()
    return combined_frame


def get_img_source(plot_figure):
    img = io.BytesIO()
    plot_figure.savefig(img, format='png',
                        bbox_inches='tight')
    img.seek(0)
    encoded = base64.b64encode(img.getvalue())
    source_to_img = 'data:image/png;base64, {}'.format(encoded.decode('utf-8'))
    return source_to_img


def run_example():
    start = datetime.datetime(2020, 1, 1)
    end = datetime.date.today()
    stocks_names = ['MSFT', 'GOOG', 'AAPL']
    df = get_stock_dataframe(stocks_names, 'Adj Close', start, end)
    df.plot(grid=True)
    plot_figure = plt.figure(1)
    img_source = get_img_source(plot_figure)
    return img_source


def main():
    pass
