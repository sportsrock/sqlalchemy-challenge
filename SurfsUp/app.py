# Import the dependencies.

from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create an instance of the Flask class
app = Flask(__name__)


#################################################
# Database Setup
#################################################

# Create an engine to connect to your SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


@app.route('/')
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    # Perform your precipitation analysis query here
    # Convert the result to a dictionary
    # Return the JSON representation using jsonify()

@app.route('/api/v1.0/stations')
def stations():
    # Query and return the list of stations

@app.route('/api/v1.0/tobs')
def tobs():
    # Query and return temperature observations for the most active station

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temperature_range(start, end=None):
    # Query and calculate temperature statistics for the specified date range
    # Return the JSON representation

if __name__ == '__main__':
    app.run(debug=True)

#################################################
# Flask Routes
#################################################


@app.route('/')
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    # Query the last 12 months of precipitation data and convert to a dictionary
    # Return the JSON representation using jsonify()

@app.route('/api/v1.0/stations')
def stations():
    # Query and return the list of stations
    # Return the JSON representation using jsonify()

@app.route('/api/v1.0/tobs')
def tobs():
    # Query temperature observations for the most active station over the last year
    # Return the JSON representation using jsonify()

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temperature_range(start, end=None):
    # Perform query to calculate temperature statistics for the specified date range
    # Return the JSON representation using jsonify()

if __name__ == '__main__':
    app.run(debug=True)
