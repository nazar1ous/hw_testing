import pandas as pd
import yfinance as yf
import io
import base64


class StockAnalyzer:
    def __init__(self, stock_names_lst):
        self._stock_names = stock_names_lst

    def get_combined_stock_dataframe(self, target_data, start, end=None):
        stocks_frames = []
        for stock_name in self._stock_names:
            stock_frame = yf.download(stock_name, start=start, end=end)
            stocks_frames.append((stock_name, stock_frame))

        combined_frame = pd.DataFrame({item[0]: item[1][target_data]
                                       for item in stocks_frames})
        combined_frame.head()
        return combined_frame

    @staticmethod
    def get_img_source(plot_figure):
        img = io.BytesIO()
        plot_figure.savefig(img, format='png',
                            bbox_inches='tight')
        img.seek(0)
        encoded = base64.b64encode(img.getvalue())
        source_to_img = 'data:image/png;base64, {}'.format(encoded.decode('utf-8'))
        return source_to_img


if __name__ == '__main__':
    a = StockAnalyzer(['SUCKAKAKFDFDSD'])
