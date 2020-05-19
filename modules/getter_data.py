import os
import pandas as pd


def get_names_from_data(filename):
    names = []
    data = pd.read_csv(os.path.join(os.getcwd(), filename), sep=' ' * 2, engine='python')
    for name in data['Instrument']:
        names.append(name)
    return names


if __name__ == "__main__":
    print(get_names_from_data('../sources/stocks.csv'))