#!/usr/bin/python3
"""
Starts a Flask web application, listening on 0.0.0.0, port 5000.
With routes: '/', '/hbnb', '/c/<text>'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Starting the Flask web application.
    With '/' route, to display 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Starting the Flask web application.
    With '/hbnb' route, to display 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Starting the Flask web application.
    With '/c/<text>' route,
    to display 'C followed by the value of <text>'.
    """
    return 'C {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
