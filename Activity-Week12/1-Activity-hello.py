# Activity W12-1: Develop an initial web App using Flask
#
# Develop a simple web application that displays a message in the browser. (10 minutes time).
# Share the GitHub link and your result screenshot.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Goodbye, Flask!</p>"


@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello, {name} is learning Flask!</p>"


if __name__ == "__main__":
    app.run(debug=True)
