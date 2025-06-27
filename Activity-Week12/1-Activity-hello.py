# Activity W12-1: Develop an initial web App using Flask
#
# Develop a simple web application that displays a message in the browser. (10 minutes time).
# Share the GitHub link and your result screenshot.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


'''
if __name__ == '__main__':
    app.run(debug=True)
    '''
