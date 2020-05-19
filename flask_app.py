from flask import Flask, render_template, request, redirect
from modules.processor import plot_portfolio, plot_ratio_change
import time
from modules.getter_data import get_names_from_data
import datetime
# from main import run_example
app = Flask(__name__)




@app.route("/")
def welcome():
    """
    If user goes to the main route, opens index.html
    :return:
    """
    return render_template("welcome.html")


@app.route("/plot", methods=["POST", "GET"])
def plot():
    # print(users_stocks)
    d_number = imp_numbers['days_number']
    if d_number:
        try:
            start = (datetime.date.today() - datetime.timedelta(days=int(d_number))).strftime("%Y-%m-%d")
        except ValueError:
            start = datetime.datetime(2016, 1, 1).strftime("%Y-%m-%d")
    else:
        start = datetime.datetime(2016, 1, 1).strftime("%Y-%m-%d")

    end = datetime.date.today().strftime("%Y-%m-%d")
    invest_num = imp_numbers['inv_number']
    return render_template('layout.html', img_source1=plot_portfolio(users_stocks, start, end, invest_num),
                           img_source2=plot_ratio_change(users_stocks, start, end, invest_num))


@app.route("/check", methods=["POST"])
def check():
    for cb_stock_name in cb_stock_names:
        value = request.form.get(cb_stock_name)
        if value:
            users_stocks.append(value)
    for cb_for_name in cb_for_names:
        value = request.form.get(cb_for_name)
        if value:
            users_stocks.append(value)
    for cb_cur_name in cb_cur_names:
        value = request.form.get(cb_cur_name)
        if value:
            users_stocks.append(value)
    for cb_com_name in cb_com_names:
        value = request.form.get(cb_com_name)
        if value:
            users_stocks.append(value)
    inv_number = request.form.get("investing_number")
    days_number = request.form.get("days_number")
    imp_numbers['inv_number'] = inv_number
    imp_numbers['days_number'] = days_number
    return redirect("/plot")


@app.route("/stock_options", methods=["GET"])
def stock_options():
    return render_template('stock_options.html', len_st=len(stocks_names),
                           stocks_names=stocks_names, cb_stock_names=cb_stock_names, len_com=len(com_names),
                           com_names=com_names, cb_com_names=cb_com_names, len_for=len(stocks_names),
                           for_names=for_names, cb_for_names=cb_for_names, len_cur=len(cur_names),
                           cur_names=cur_names, cb_cur_names=cb_cur_names)


if __name__ == "__main__":
    # Create local data server
    lst = []
    stocks_names = get_names_from_data('sources/stocks.csv')
    com_names = get_names_from_data('sources/commodities.csv')
    for_names = get_names_from_data('sources/forex.csv')
    cur_names = get_names_from_data('sources/crypto_currency.csv')

    cb_stock_names = ['cb_st' + str(i) for i in range(len(stocks_names))]
    cb_com_names = ['cb_com' + str(i) for i in range(len(com_names))]
    cb_for_names = ['cb_for' + str(i) for i in range(len(for_names))]
    cb_cur_names = ['cb_cur' + str(i) for i in range(len(cur_names))]
    users_stocks = []
    imp_numbers = {}

    s = time.time()
    app.run(debug=True)
    print(time.time() - s)

