from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def about():
    return "This Is A Test For A Simple Web Server!"


@app.route("/contact")
def contact():
    return "Captian Obvious, 6969 Willing Way Portland OR, Badtouch@gmail.com"


if __name__ == "__main__":
    app.run()
