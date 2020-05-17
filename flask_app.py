from flask import Flask, render_template, request, make_response
from main_2 import run_example
app = Flask(__name__)


@app.route("/")
def welcome():
    """
    If user goes to the main route, opens index.html
    :return:
    """
    return render_template("welcome.html")


@app.route("/plot", methods=["POST"])
def plot():
    return render_template('layout.html', img_source=run_example())


if __name__ == "__main__":
    app.run(debug=True)

