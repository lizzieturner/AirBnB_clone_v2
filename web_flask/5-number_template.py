#!/usr/bin/python3
''' starts a Flask web application  '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def slash():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def slash_c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def slash_python(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def slash_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def slash_number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
