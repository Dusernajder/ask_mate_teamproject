from flask import Flask, render_template, redirect, request
import data_handler


app = Flask(__name__)


@app.route("/")
def home():
    questions = data_handler.read_elements_csv(data_handler.QUESTION_DATA_FILE_PATH)
    return render_template('home.html', questions=questions)


if __name__ == "__main__":
    app.run()
