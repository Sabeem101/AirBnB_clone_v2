#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import render_template
from models.state import State
from models import storage
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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Starting the Flask web application.
    With "/number_odd_or_even/<n>" route,
    to display an HTML page only if "n" is an integer.
    """
    if n % 2 == 0:
        p = "even"
    else:
        p = "odd"
    return render_template("6-number_odd_or_even.html", number=n, parity=p)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Starting the Flask web application.
    With "/states_list" route, to display an HTML page.
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close(error):
    """
    Closing the storage.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
