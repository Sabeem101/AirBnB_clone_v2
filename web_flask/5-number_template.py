#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Starting the Flask web application.
    With "/" route, to display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Starting the Flask web application.
    with "/hbnb" route, to display "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Starting the Flask web application.
    With "/c/<text>" route,
    to display "C", followed by the value of <text>.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Starting the Flask web application.
    With "/python/<text>" route,
    to display "Python", followed by the value of <text>.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Starting the Flask web application.
    With "/number/<n>" route,
    to display "n is a number", only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    Displays an HTML page only if "n" in an integer.
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
