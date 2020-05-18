from flask import Flask, render_template, request, make_response
from main import main, main2
# from main import run_example
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
    return render_template('layout.html', img_source=main(), img_source_2=main2())


if __name__ == "__main__":
    app.run(debug=True)

