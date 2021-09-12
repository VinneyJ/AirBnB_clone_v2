#!/usr/bin/python3
'''
script that starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb_one():
    ''' THe root route '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    ''' THe hbnb route '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    ''' c is what '''
    if '_' in text:
        return "C {}".format(text.replace('_', ' '))
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
