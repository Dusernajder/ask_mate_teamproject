from flask import Flask, render_template, redirect, request
import data_manager


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
