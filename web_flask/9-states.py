#!/usr/bin/python3
"""Starts Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Calls storage.close()"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page: (inside the tag BODY)."""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays all cities within a state."""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def states_id(id):
    """Display a State with a specific id."""
    state = storage.all('State').get(id)
    print(state)
    return render_template('9-states.html', state=state) 




if __name__ == "__main__":
    app.run(host="0.0.0.0")
