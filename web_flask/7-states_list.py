#!/usr/bin/python3
''' starts a Flask web application  '''
from models import *
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
        Displays States list HTML page
    '''
    states = sorted(list(storage.all('State').values()), key=lamda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run()
